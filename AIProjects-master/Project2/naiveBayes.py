# naiveBayes.py
# -------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import util
import classificationMethod
import math
import statistics

class NaiveBayesClassifier(classificationMethod.ClassificationMethod):
  """
  See the project description for the specifications of the Naive Bayes classifier.
  
  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  def __init__(self, legalLabels):
    self.legalLabels = legalLabels
    self.type = "naivebayes"
    self.k = 1 # this is the smoothing parameter, ** use it in your train method **
    self.automaticTuning = False # Look at this flag to decide whether to choose k automatically ** use this in your train method **
    
  def setSmoothing(self, k):
    """
    This is used by the main method to change the smoothing parameter before training.
    Do not modify this method.
    """
    self.k = k

  def train(self, trainingData, trainingLabels, validationData, validationLabels):
    """
    Outside shell to call your method. Do not modify this method.
    """  
      
    # might be useful in your code later...
    # this is a list of all features in the training set.
    # presumably is pixel data in format determined in dataClass
    self.features = list(set([ f for datum in trainingData for f in datum.keys() ]))
    
    if (self.automaticTuning):
        kgrid = [0.001, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 20, 50]
    else:
        kgrid = [self.k]
        
    self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, kgrid)
      
  def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, kgrid):
    """
    Trains the classifier by collecting counts over the training data, and
    stores the Laplace smoothed estimates so that they can be used to classify.
    Evaluate each value of k in kgrid to choose the smoothing parameter 
    that gives the best accuracy on the held-out validationData.
    
    trainingData and validationData are lists of feature Counters.  The corresponding
    label lists contain the correct label for each datum.
    
    To get the list of all possible features or labels, use self.features and 
    self.legalLabels.
    """
    trainingClasses = dict()
    counter = 0


    for i in self.legalLabels:
      trainingClasses[i] = []
    #classify data by class for training
    #don't even know if we need this for now. keeping in case.
    for it in trainingData:
      trainingClasses[trainingLabels[counter]].append(it) 
      counter += 1
    dataStats = dict()
    for num in self.legalLabels:
      #instantiate empty list of digit objects per each class
      dataStats[num] = []
      #want to somehow compile all values within one pixel for each class and calculate mean/stdev
      #how to do? need to iterate down digit objects for each value.
      #get list of digit drawings.
      diglist = trainingClasses[num]
      pixNum = trainingClasses[num][0].keys()
      #iterate through each pixel
      for valid in pixNum:
        #calcList = []
        pixList = [0,0,0]
        #iterate through each digit object
        for obval in diglist:
          #add val found to list for stat calcs
          pix = obval[valid]
          pixList[pix] += 1
          #calcList.append(pix)
        for i in list(range(3)):
          pixList[i] = (pixList[i]+self.k)/(len(diglist)+self.k)

        #smooth values
        #calcList.append(self.k)
        #calculate stdev and mean for list
        #add small number to fudge for stdev
        #dataStats[num].append((statistics.mean(calcList),statistics.stdev(calcList)))
        #commenting above for now, trying to switch methods
        dataStats[num].append(pixList)
      #have to get counts of class for prior probability, append to end of array
      priprob = (len(trainingClasses[num])+self.k)/(len(trainingLabels)+self.k)
      dataStats[num].append(priprob)
    self.dataStats = dataStats
    #util.raiseNotDefined()
        
  def classify(self, testData):
    """
    Classify the data based on the posterior distribution over labels.
    
    You shouldn't modify this method.
    """
    guesses = []
    self.posteriors = [] # Log posteriors are stored for later data analysis (autograder).
    for datum in testData:
      posterior = self.calculateLogJointProbabilities(datum)
      guesses.append(posterior.argMax())
      self.posteriors.append(posterior)
    return guesses
      
  def calculateLogJointProbabilities(self, datum):
    """
    Returns the log-joint distribution over legal labels and the datum.
    Each log-probability should be stored in the log-joint counter, e.g.    
    logJoint[3] = <Estimate of log( P(Label = 3, datum) )>
    
    To get the list of all possible features or labels, use self.features and 
    self.legalLabels.
    """
    logJoint = util.Counter()
    #from what I can tell, the basic idea here is to calculate the probabilities for all labels and output a list with them.
    for label in self.legalLabels:
      condprob = 1
      counter = 0
      for feature in datum.values():
        condprob *= self.dataStats[label][counter][feature]
        #condprob *= self.GaussianPDF(feature,self.dataStats[label][counter][0],self.dataStats[label][counter][1])
        counter += 1
      #multiply by prior probability
      holder = self.dataStats[label][-1]
      logJoint[label] = condprob*holder #*self.dataStats[label][-1]
      
    return logJoint
  
  def GaussianPDF(self, feature, mean, stdev):
    """Gaussian probability density function"""
    principal = (1/(math.sqrt(2*math.pi)*stdev))*math.exp(-1*(math.pow(feature-mean,2)/(2*math.pow(stdev,2))))
    return principal
  
  def findHighOddsFeatures(self, label1, label2):
    """
    Returns the 100 best features for the odds ratio:
            P(feature=1 | label1)/P(feature=1 | label2) 
    
    Note: you may find 'self.features' a useful way to loop through all possible features
    """
    featuresOdds = []
    for i,j in dataStats[label1],dataStats[label2]:
      #generate normal distribution with mean and stdev from dataStats
      ndisti = statistics.NormalDist(i[0],i[1])
      ndistj = statistics.NormalDist(j[0],j[1])
      odds = (ndisti.cdf(2.0)-ndisti.cdf(1.0))/(ndistj.cdf(2.0)-ndistj.cdf(1.0))
      if len(featuresOdds) < 100:
        featuresOdds.append(odds)
      else:
        min = 2.0
        index = 0
        for i in list(range(featuresOdds)):
          if featuresOdds[i] < min:
            min = featuresOdds[i]
            index = i
        if min < odds:
          featuresOdds[index] = odds

    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    return featuresOdds
    

    
      
