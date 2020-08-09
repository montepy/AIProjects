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


  dataCollection = rLoadDataFile(options.data, numTraining)

  rawTrainingData = dataCollection['rawTrainingData']
  trainingLabels = dataCollection['trainingLabels']
  rawValidationData = dataCollection['rawValidationData']
  validationLabels = dataCollection['validationLabels']
  rawTestData = dataCollection['rawTestData']
  testLabels = dataCollection['testLabels']

  # Extract features
  print("Extracting features...")
  trainingData = map(featureFunction, rawTrainingData)
  validationData = map(featureFunction, rawValidationData)
  testData = map(featureFunction, rawTestData)

  # Conduct training and testing
  print("Training...")
  classifier.train(trainingData, trainingLabels, validationData, validationLabels)
  print("Validating...")
  guesses = classifier.classify(validationData)
  correct = [guesses[i] == validationLabels[i] for i in range(len(validationLabels))].count(True)
  print(str(correct), ("correct out of " + str(len(validationLabels)) + " (%.1f%%).") % (100.0 * correct / len(validationLabels)))
  print("Testing...")
  guesses = classifier.classify(testData)
  correct = [guesses[i] == testLabels[i] for i in range(len(testLabels))].count(True)
  print(str(correct), ("correct out of " + str(len(testLabels)) + " (%.1f%%).") % (100.0 * correct / len(testLabels)))
  analysis(classifier, guesses, testLabels, testData, rawTestData, printImage)

  # do odds ratio computation if specified at command line
  if((options.odds) & (options.classifier == "naiveBayes" or (options.classifier == "nb")) ):
    label1, label2 = options.label1, options.label2
    features_odds = classifier.findHighOddsFeatures(label1,label2)
    if(options.classifier == "naiveBayes" or options.classifier == "nb"):
      string3 = "=== Features with highest odd ratio of label %d over label %d ===" % (label1, label2)
    else:
      string3 = "=== Features for which weight(label %d)-weight(label %d) is biggest ===" % (label1, label2)

    print(string3)
    printImage(features_odds)

  if((options.weights) & (options.classifier == "perceptron")):
    for l in classifier.legalLabels:
      features_weights = classifier.findHighWeightFeatures(l)
      print(("=== Features with high weight for label %d ==="%l))
      printImage(features_weights)


def rLoadDataFile(inputDataType, numTraining):
    dataCollection = {}
    if(inputDataType == "faces"):
        maxTraining = FACE_MAX_TRAINING
        for i in range(numTraining)
            rand = random.randint(1, maxTraining)
            dataCollection['rawTrainingData'] = load1Data("data/facedata/facedatatrain", rand, FACE_DATUM_WIDTH, FACE_DATUM_HEIGHT)
            dataCollection['trainingLabels'] = load1Label("data/facedata/facedatatrainlabels", rand, FACE_DATUM_WIDTH, FACE_DATUM_HEIGHT)
            dataCollection['rawValidationData'] = load1Data("data/facedata/facedatatrain", rand, FACE_DATUM_WIDTH, FACE_DATUM_HEIGHT)
            dataCollection['rawValidationLabels'] = load1Label("data/facedata/facedatatrainlabels", rand, FACE_DATUM_WIDTH, FACE_DATUM_HEIGHT)
            dataCollection['rawTestData'] = load1Data("data/facedata/facedatatest", rand, FACE_DATUM_WIDTH, FACE_DATUM_HEIGHT)
            dataCollection['testLabels'] = load1Label("data/facedata/facedatatestlabels", rand, FACE_DATUM_WIDTH, FACE_DATUM_HEIGHT)
    elif(inputDataType == "digits"):
        maxTraining = DIGIT_MAX_TRAINING
        for i in range(numTraining)
            rand = random.randint(1, maxTraining)
            dataCollection['rawTrainingData'] = load1Data("data/digitdata/trainingimages", rand, DIGIT_DATUM_WIDTH, DIGIT_DATUM_HEIGHT)
            dataCollection['trainingLabels'] = load1Label("data/digitdata/traininglabels", rand, DIGIT_DATUM_WIDTH, DIGIT_DATUM_HEIGHT)
            dataCollection['rawValidationData'] = load1Data("data/digitdata/validationimages", rand, DIGIT_DATUM_WIDTH, DIGIT_DATUM_HEIGHT)
            dataCollection['rawValidationLabels'] = load1Label("data/digitdata/validationlabels", rand, DIGIT_DATUM_WIDTH, DIGIT_DATUM_HEIGHT)
            dataCollection['rawTestData'] = load1Data("data/digitdata/testimages", rand, DIGIT_DATUM_WIDTH, DIGIT_DATUM_HEIGHT)
            dataCollection['testLabels'] = load1Label("data/digitdata/testlabels", rand, DIGIT_DATUM_WIDTH, DIGIT_DATUM_HEIGHT)
    return dataCollection

def load1Data(filename, n, width, height):
    fin = samples.readlines(filename)
    #fin.reverse()
    data = []
    for j in range(height):
        data.append(list(fin[(n*height)+j]))
        if (len(data[0]) < width-1):
        # we encountered end of file...
            print(("Truncating at %d examples (maximum)" % i))
            break
    item = samples.Datum(data,width,height)

    return item

def load1Label(filename, n):
      fin = list(samples.readlines(filename))
      return fin[n]


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
