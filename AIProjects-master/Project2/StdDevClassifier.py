# StdDevClassifier.py
#code that uses the dataClassifer to find the standard deviation and prediction test_umath_accuracy

import dataClassifier

import mostFrequent
import naiveBayes
import perceptron
import samples
import sys
import util
import os

import random

TEST_SET_SIZE = 100
DIGIT_DATUM_WIDTH=28
DIGIT_DATUM_HEIGHT=28
FACE_DATUM_WIDTH=60
FACE_DATUM_HEIGHT=70

FACE_MAX_TRAINING=450
DIGIT_MAX_TRAINING=5000

DEBUGING_MODE = False


def devClassifier(args, options):

    featureFunction = args['featureFunction']
    classifier = args['classifier']
    printImage = args['printImage']

    # Load data
    numTraining = options.training
    numTest = options.test

    iterations = 5
    percentCorrect = []
    correctAverage = 0

    for i in range(iterations):
        dataCollection = rLoadDataFile(options.data, numTraining, numTest)

        rawTrainingData = dataCollection['rawTrainingData']
        trainingLabels = dataCollection['trainingLabels']
        rawValidationData = dataCollection['rawValidationData']
        validationLabels = dataCollection['validationLabels']
        rawTestData = dataCollection['rawTestData']
        testLabels = dataCollection['testLabels']

        # Extract features
        #print("Extracting features...")
        trainingData = map(featureFunction, rawTrainingData)
        validationData = map(featureFunction, rawValidationData)
        testData = map(featureFunction, rawTestData)

        # Conduct training and testing
        print("Iteration: ", i)
        print("Training...")
        classifier.train(trainingData, trainingLabels, validationData, validationLabels)
        #print("Validating...")
        #guesses = classifier.classify(validationData)
        #correct = [guesses[i] == validationLabels[i] for i in range(len(validationLabels))].count(True)
        #print(str(correct), ("correct out of " + str(len(validationLabels)) + " (%.1f%%).") % (100.0 * correct / len(validationLabels)))
        print("Testing...")
        guesses = classifier.classify(testData)
        correct = [guesses[i] == testLabels[i] for i in range(len(testLabels))].count(True)
        print(str(correct), ("correct out of " + str(len(testLabels)) + " (%.1f%%).") % (100.0 * correct / len(testLabels)))

        percentCorrect.append(100.0 * correct / len(testLabels))
        correctAverage = correctAverage + (100.0 * correct / len(testLabels))
        #dataClassifier.analysis(classifier, guesses, testLabels, testData, rawTestData, printImage)

    correctAverage = correctAverage/iterations
    print "\nPercent accuracy -", correctAverage

    sumOfSquares = 0
    for i in range(iterations):
        sumOfSquares += (percentCorrect[i] - correctAverage) ** 2

    standardDeviation = sumOfSquares/iterations
    print "Standard deviation - ", standardDeviation



def rLoadDataFile(inputDataType, numTraining,numTest):
    dataCollection = {}
    dataCollection['rawTrainingData'] = []
    dataCollection['trainingLabels'] = []
    if(inputDataType == "faces"):
        maxTraining = FACE_MAX_TRAINING-1
        rawTrainingDataFile = samples.readlines("data/facedata/facedatatrain")
        trainingLabelsFile = samples.readlines("data/facedata/facedatatrainlabels")
        for i in range(numTraining):
            rand = random.randint(1, maxTraining)
            dataCollection['rawTrainingData'].append(load1Data(rawTrainingDataFile, rand, FACE_DATUM_WIDTH, FACE_DATUM_HEIGHT))
            dataCollection['trainingLabels'].append(load1Label(trainingLabelsFile, rand))

        dataCollection['rawValidationData'] = samples.loadDataFile("data/facedata/facedatatrain", numTest, FACE_DATUM_WIDTH, FACE_DATUM_HEIGHT)
        dataCollection['validationLabels'] = samples.loadLabelsFile("data/facedata/facedatatrainlabels", numTest)
        dataCollection['rawTestData'] = samples.loadDataFile("data/facedata/facedatatest", numTest, FACE_DATUM_WIDTH, FACE_DATUM_HEIGHT)
        dataCollection['testLabels'] = samples.loadLabelsFile("data/facedata/facedatatestlabels", numTest)

    elif(inputDataType == "digits"):
        maxTraining = DIGIT_MAX_TRAINING-1
        rawTrainingDataFile = samples.readlines("data/digitdata/trainingimages")
        trainingLabelsFile = samples.readlines("data/digitdata/traininglabels")
        for i in range(numTraining):

            rand = random.randint(1, maxTraining)
            dataCollection['rawTrainingData'].append(load1Data(rawTrainingDataFile, rand, DIGIT_DATUM_WIDTH, DIGIT_DATUM_HEIGHT))
            dataCollection['trainingLabels'].append(load1Label(trainingLabelsFile, rand))

        dataCollection['rawValidationData'] = samples.loadDataFile("data/digitdata/validationimages", numTest, DIGIT_DATUM_WIDTH, DIGIT_DATUM_HEIGHT)
        dataCollection['validationLabels'] = samples.loadLabelsFile("data/digitdata/validationlabels", numTest)
        dataCollection['rawTestData'] = samples.loadDataFile("data/digitdata/testimages", numTest, DIGIT_DATUM_WIDTH, DIGIT_DATUM_HEIGHT)
        dataCollection['testLabels'] = samples.loadLabelsFile("data/digitdata/testlabels", numTest)

    return dataCollection

def load1Data(file, n, width, height):
    #fin = samples.readlines(filename)
    #fin.reverse()
    data = []
    for j in range(height):
        data.append(list(file[(n*height)+j]))
        if (len(data[0]) < width-1):
        # we encountered end of file...
            print(("Truncating at %d examples (maximum)" % i))
            break
    item = samples.Datum(data,width,height)

    return item

def load1Label(file, n):
      #fin = list(samples.readlines(filename))
      return int(file[n])


if __name__ == '__main__':
  os.chdir(__file__[:-(len('StdDevClassifier.py'))])
  if DEBUGING_MODE:
    import pdb; pdb.set_trace()
  print(__file__[:-len('StdDevClassifier.py')])
  # Read input
  from time import time
  runtime = time()
  args, options = dataClassifier.readCommand( sys.argv[1:] )
  # Run classifier
  devClassifier(args, options)
  print(time()-runtime)
