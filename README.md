# Promoter Discovery Machine Learning Challenge

## Brief Background

> In genetics, an e​nhancer​is a short (100 ­1000 base pairs) region of DNA that can be bound by proteins (activators) to increase the likelihood transcription will occur at a gene. P​romoter​is a similar sized region of the DNA that initiates transcription of a particular gene.

## Task

> Given a DNA region of 1000 base pairs, predict if it is an e​nhancer​or a p​romoter. ​In other words, given a string with 1000 characters (A/C/G/T) you have to classify it into one of two possible classes based on its sequence.

## Methodology

### Setup

* `0`: promoter
* `1`: enhancer
* Remove observations with unknown nucleobases, since this is a small set (15 observations)

### Baseline: Random Classifier

A baseline classifier to evaluate the success of other classifiers is random classification based on the distribution of the training data. In the training data, the probability of a given region being a promoter is 0.79. The objective is to improve on the performance of a random classifier which assigns the class `0` by a random draw from a bernoulli distribution with probability of the training data. In 10-fold cross validation the accuracy of this classifier 0.67.

### Experiments

#### Classifiers with no feature engineering

The first set of experiments was to evaluate the accuracy of standard ML classifiers without any feature engineering. Because of the time required to train, data is subsampled (10,000 samples).

Results of these experiments can

#### String similarity measures

Many string similarity measures have applications in genetics in understanding regions of similarity ([sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment)). A majority vote or k-nearest neighbor classifier may be implemented using one of these measures of similarity or distance.

The following similarity measures were used to analyze distributions of the scores for pairs of sequences both having label `0`, both having label `1` and having different labels.


