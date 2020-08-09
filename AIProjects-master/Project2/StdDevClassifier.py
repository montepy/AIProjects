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

TEST_SET_SIZE = 100
DIGIT_DATUM_WIDTH=28
DIGIT_DATUM_HEIGHT=28
FACE_DATUM_WIDTH=60
FACE_DATUM_HEIGHT=70

DEBUGING_MODE = false

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


def devClassifier(args, options):

  featureFunction = args['featureFunction']
  classifier = args['classifier']
  printImage = args['printImage']

  # Load data
  numTraining = options.training
  numTest = 1

  if(options.data=="faces"):
    rawTrainingData = samples.loadDataFile("data/facedata/facedatatrain", numTraining,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
    trainingLabels = samples.loadLabelsFile("data/facedata/facedatatrainlabels", numTraining)
    rawValidationData = samples.loadDataFile("data/facedata/facedatatrain", numTest,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
    validationLabels = samples.loadLabelsFile("data/facedata/facedatatrainlabels", numTest)
    rawTestData = samples.loadDataFile("data/facedata/facedatatest", numTest,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
    testLabels = samples.loadLabelsFile("data/facedata/facedatatestlabels", numTest)
  else:
    rawTrainingData = samples.loadDataFile("data/digitdata/trainingimages", numTraining,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
    trainingLabels = samples.loadLabelsFile("data/digitdata/traininglabels", numTraining)
    rawValidationData = samples.loadDataFile("data/digitdata/validationimages", numTest,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
    validationLabels = samples.loadLabelsFile("data/digitdata/validationlabels", numTest)
    rawTestData = samples.loadDataFile("data/digitdata/testimages", numTest,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
    testLabels = samples.loadLabelsFile("data/digitdata/testlabels", numTest)


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
    if(inputDataType == "faces"):
        pass
    elif(inputDataType == "digits"):
        pass

def load1Data(filename, n, width, height):
    pass

def load1Label(filename, n, width, height):
      fin = samples.readlines(filename)
      i = 1
      label = 0
      for line in fin[:min(n, len(fin))]:
        if line == '':
            break
        if(i == n):
            label = int(line)
            break
        i+=1

      return label
