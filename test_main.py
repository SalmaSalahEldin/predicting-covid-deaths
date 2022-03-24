from cgi import test
from main import RetrieveData

test = RetrieveData()

# Testing that the csv file is read correctly
assert len(test.df.columns) == 4