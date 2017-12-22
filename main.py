#idee:
# los eerst de vlakken op
# die geven x mogelijke vlakken
# parse dan de vlakken aan elkaar
import numpy as np
import csv

with open("randen.csv") as infile:
    reader = csv.DictReader()







class vlak_wizird:
    def __init__(self):
        print "blaat"

class vectorize_


wizird = vlak_wizird()


arr = np.array([[ 0.96488889, 0.73641667, 0.67521429, 0.592875, 0.53172222],
                [ 0.78008333, 0.5938125, 0.481, 0.39883333, 0.]])

print arr.all(1)
print arr[arr.all(1)]
print arr

test = np.array([[0, 1, 1, 0, 1],
                 [1, 0, 0, 1, 1],
                 [0, 1, 1, 1, 0]])

vector = [0, 1, 0, 0, 0]

np.allclose(test, [1, 0, 0, 1, 1])

np.dot(test, vector)
np.outer(test, vector)

test
test-vector

test.sum(axis=1)
