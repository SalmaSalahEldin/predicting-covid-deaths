from main import PredictCovid

test = PredictCovid()
vaxed_transitionMatrix, unvaxed_transitionMatrix = test.transitionMatrix()

print(vaxed_transitionMatrix)
print(unvaxed_transitionMatrix)
# Testing that the csv file is read correctly
assert len(test.vaxxed_df.columns) == 4
assert len(test.unvaxxed_df.columns) == 4

# Testing that the transition matrix is correct
assert vaxed_transitionMatrix[2, 0] == 0
assert unvaxed_transitionMatrix[2, 2] == 1

# Printing the markov chain prediction for designated day
day = 6
predict_vax, predict_unvax = test.markovChain(day)

print(predict_vax)
print(predict_unvax)
