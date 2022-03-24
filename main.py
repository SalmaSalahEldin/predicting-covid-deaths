import pandas as pd

class RetrieveData:
    def __init__(self):
        """
        Reading csv file
        """
        try:
            self.df = pd.read_csv("byvax.csv")
        except FileNotFoundError as e:
            print(e)
