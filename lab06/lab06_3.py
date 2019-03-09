'''
Andrew Thomas
CS 344 Lab06
'''
import numpy
import keras.datasets.boston_housing as housing

(trainingX, trainingY), (testingX, testingY) = housing.load_data()

print("Training examples count: ", len(trainingX))
print("Testing examples count: ", len(testingX))
print()

print("Training Rank: ", trainingX.ndim)
print("Training Shape: ", testingX.shape)
print("Training Type: ", trainingX.dtype)
print("Testing Rank: ", testingX.ndim)
print("Testing Shape: ", testingX.shape)
print("Testing Type: ", testingX.dtype)