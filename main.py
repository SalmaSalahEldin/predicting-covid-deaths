import pandas as pd
import numpy as np


class PredictCovid:
    def __init__(self):
        """
        Reading csv file
        """
        try:
            # Read csv file
            df = pd.read_csv("/content/predicting-covid-deaths/resources/byvax.csv")

            # Store two dataframes based on vax status
            vaxxed = df['vaccination_status'] == 'Fully Vaccinated'
            unvaxxed = df['vaccination_status'] == 'Non-Fully Vaccinated'
            #converting to dataframe
            self.vaxxed_df = df[vaxxed]
            self.unvaxxed_df = df[unvaxxed]
            #we are using div() function to divide each value in ['count_of_case'] column as a kind of normalization
            self.unvaxxed_df['count_of_case'] =\
                self.unvaxxed_df['count_of_case'].div(2.2)


            # Initializing the transition matrix
            self.vaxxed_transMatrix = np.zeros((3, 3))
            self.unvaxxed_transMatrix = np.zeros((3, 3))

        except FileNotFoundError as e:
            print(e)


    def transitionMatrix(self):

        """
        Creates the two transition matrices
        based on vax status where each transition matrix has three states:
        noncritical, critical (ICU), and death

                            Non-Critical    ICU     Death
                            ------------------------------
        Non-Critical    |
        ICU             |
        Death           |
        ------
        Returns two 2x2 matrices
        """
        # Creating matrix for vaxxed
        vax_deceased = self.vaxxed_df.loc[self.vaxxed_df['clinicalstatus'] == 'Deceased (based on date of death)', 'count_of_case'].mean().round(2)
                                          #loc to get a column by its label 
                                          #Round a number to only two decimals
                                          #loc[rows,col]
                                          #vax_deceased is a number represents the mean of dead persons who was vaccinated

        vax_icu = self.vaxxed_df.loc[self.vaxxed_df['clinicalstatus'] =='ICU', 'count_of_case'].mean().round(2)
                                          #vax_icu is a number represents the mean of Critical persons who was vaccinated

        vax_noncritical = 1 - vax_deceased - vax_icu
                                          #vax_icu is a number represents the mean of noncritical persons who was vaccinated

        self.vaxxed_transMatrix = np.matrix([[vax_noncritical, vax_icu, vax_deceased], [0.12, 0.4, 0.46], [0, 0, 1]])



        # Creating matrix for unvaxxed
        unvax_deceased =\
            self.unvaxxed_df.loc[self.unvaxxed_df['clinicalstatus'] ==
                                 'Deceased (based on date of death)',
                                 'count_of_case'].mean().round(2)

        unvax_icu = self.unvaxxed_df.loc[self.unvaxxed_df['clinicalstatus'] ==
                                         'ICU', 'count_of_case'].mean().round(2)

        unvax_noncritical = 1 - unvax_deceased - unvax_icu

        self.unvaxxed_transMatrix =\
            np.matrix([[unvax_noncritical, unvax_icu, unvax_deceased],
                      [0.05, 0.2, 0.75],
                      [0, 0, 1]])

        return self.vaxxed_transMatrix, self.unvaxxed_transMatrix

    def markovChain(self, days):
        """
        Predicts the future days' fatality and ICU
        based on vax status
        """
        vax_predicted = np.linalg.matrix_power(self.vaxxed_transMatrix, days).round(2)
        unvax_predicted = np.linalg.matrix_power(self.unvaxxed_transMatrix, days).round(2)
        return vax_predicted, unvax_predicted
