from cgi import test
from main import PredictCovid

test = PredictCovid()
vaxed_transitionMatrix, unvaxed_transitionMatrix = test.transitionMatrix()

# Testing that the csv file is read correctly
assert len(test.vaxxed_df.columns) == 4
assert len(test.unvaxxed_df.columns) == 4

# Testing that the transition matrix is correct
assert vaxed_transitionMatrix[2][0] == 0
assert unvaxed_transitionMatrix[2][2] == 1
