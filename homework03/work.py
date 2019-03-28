from keras.datasets import boston_housing
import numpy
import keras
import pandas

(training, labels), (testX, testingLabel) = boston_housing.load_data()

print('Training X # of decisions: ' + str(training.ndim))
print('Training X Shape: ' + str(training.shape))
print('Training Labels # of dimensions: ' + str(labels.ndim))
print('Training Labels Shape: ' + str(labels.shape))

trainingX = training[120:]
trainingLabels = labels[120:]
validationX = training[:120]
validationLabels = labels[:120]

df = pandas.DataFrame(trainingX)
# Index of radial highway accessibility multiplied by distance to employment center
# This assumes a low index is good access, which I can't find specified
# If a low index is bad, it would be easy to invert
# This would should how easy it is to get to work, a useful feature for looking at housing prices
easeOfCommute = df[7] * df[8]
df['easeOfComm'] = easeOfCommute
