import pandas as pd
import numpy as np


class PredictCovid:
    def __init__(self):
        """
        Reading csv file
        """
        try:
            # Read csv file
            df = pd.read_csv("byvax.csv")

            # Store two dataframes based on vax status
            vaxxed = df['vaccination_status'] == 'Fully Vaccinated'
            unvaxxed = df['vaccination_status'] == 'Non-Fully Vaccinated'
            self.vaxxed_df = df[vaxxed]
            self.unvaxxed_df = df[unvaxxed]

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
        vax_deceased = self.vaxxed_df.loc[self.vaxxed_df['clinicalstatus'] ==
                                          'Deceased (based on date of death)',
                                          'count_of_case'].mean()

        vax_icu = self.vaxxed_df.loc[self.vaxxed_df['clinicalstatus'] ==
                                     'ICU', 'count_of_case'].mean()

        vax_noncritical = 1 - vax_deceased - vax_icu

        self.vaxxed_transMatrix = [[vax_noncritical, vax_icu, vax_deceased],
                                   [0.45, 0.4, 0.15],
                                   [0, 0, 1]]

        # Creating matrix for unvaxxed
        unvax_deceased =\
            self.unvaxxed_df.loc[self.unvaxxed_df['clinicalstatus'] ==
                                 'Deceased (based on date of death)',
                                 'count_of_case'].mean()

        unvax_icu = self.unvaxxed_df.loc[self.unvaxxed_df['clinicalstatus'] ==
                                         'ICU', 'count_of_case'].mean()

        unvax_noncritical = 1 - unvax_deceased - unvax_icu

        self.unvaxxed_transMatrix =\
            [[unvax_noncritical, unvax_icu, unvax_deceased],
             [0.1, 0.5, 0.4],
             [0, 0, 1]]

        return self.vaxxed_transMatrix, self.unvaxxed_transMatrix

    def markovChain(self, days):
        """
        Predicts the upcoming months's fatality and ICU
        based on vax status
        """
        pass
