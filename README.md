# Promoter Discovery Machine Learning Challenge

## Installation

### Software Requirements

* python 2.7
* python packages: matplotlib, sklearn, numpy, random, time, csv, unittest, pytest
* [jupyter notebook](http://jupyter.readthedocs.io/en/latest/install.html)

### Download the data

```
wget -r --no-parent -A '*.bed' mitra.stanford.edu/kundaje/nboley/RAMPAGE_enhancer_prediction/RAMPAGE_peaks/train_data/
wget -r --no-parent -A 'GRCh38.genome.fa' mitra.stanford.edu/kundaje/nboley/RAMPAGE_enhancer_prediction/RAMPAGE_peaks/train_data/
mkdir RAMPAGE_PEAKS && mkdir RAMPAGE_PEAKS/train_data && mv mitra.stanford.edu/kundaje/nboley/RAMPAGE_enhancer_prediction/RAMPAGE_peaks/train_data/* RAMPAGE_peaks/train_data/
```

### Download code and run notebook

```bash
git clone https://github.com/abarciauskas-bgse/promoter_discovery
cd promoter_discovery
ipython notebook
# navigate to http://localhost:9999 or whatever port is indicated in stdout
```


### Run unit tests

```
py.test
```

## Brief Background

> In genetics, an e​nhancer​is a short (100 ­1000 base pairs) region of DNA that can be bound by proteins (activators) to increase the likelihood transcription will occur at a gene. P​romoter​is a similar sized region of the DNA that initiates transcription of a particular gene.

## Task

> Given a DNA region of 1000 base pairs, predict if it is an e​nhancer​or a p​romoter. ​In other words, given a string with 1000 characters (A/C/G/T) you have to classify it into one of two possible classes based on its sequence.

## Methodology

### Setup

* `0`: promoter
* `1`: enhancer
* Remove observations with unknown nucleobases, since this is a small set (15 observations)
* Standard ML models fit in **Experiments** are fit with a randomly selected subset of 10,000 observations.
    * Note: It is possible random vs sequential sub-selection of the origin data set impacts accuracy. It appeared in experimenting with a subset of the initial 10,000 observations to achieve higher rates of accuracy from all classifiers. If this is a persistent characteristic of the data set it suggests there is something underlying the data generating process of the entire genome which may be predictive in sequence classification.

### Baseline: Random Classifier

See **1 - Baseline (Randomized) Classifier**

A baseline classifier to evaluate the success of other classifiers is random classification based on the distribution of the training data. In the training data, the probability of a given region being a promoter is 0.79. The objective is to improve on the performance of a random classifier which assigns the class `0` by a random draw from a bernoulli distribution with probability of the training data. In 10-fold cross validation the accuracy of this classifier 0.67.

### Experiments

#### Classifiers with no feature engineering

See **2 - Classifiers (without feature engineering)**

The first set of experiments was to evaluate the accuracy of standard ML classifiers without any feature engineering. Mostly the default parameters were used. The models are trained on 90% of training data and tested on the remaining 10%.

| Classifier                                    | Score |
|-----------------------------------------------|-------|
| Logistic Regression                           | 0.777 |
| Support Vector Machine with RBF Kernel        | 0.825 |
| Support Vector Machine with Linear Kernel     | 0.780 |
| Decision Tree Classifier                      | 0.783 |
| Adaboost                                      | 0.796 |
| Random Forest Classifier (n_estimators = 100) | 0.800 |
| Naive Bayes                                   | 0.812 |
| K-Nearest Neighbors (K = 6)                   | 0.843 |
| Gradient Boosting Machine (n_estimators = 10) | 0.787 |


#### Classifiers with bigram features

> It may be helpful to think of the genome as a document written in an unknown language where words are allowed to overlap.

See **3 - Bigram Frequencies**

When strings or characters might overlap, it makes sense to analyse the frequency distributions of different ngrams. The smallest ngram which makes sense in this context is the bigram, representing a base pair. 16 unique base pairs were found in the data. The frequency distributions for each class, `promoter` and `enhancer` is analyzed in the **3 - Bigram Frequencies** notebook. It is evident that there are differences in the distributions of certain base pairs between each class. Most notably for the base pairs 'CG', 'AT' and 'TA'.

This was the basis for the hypothesis that bigram frequencies are a predictive feature of DNA sequence classification. The same models trained in experiments with no feature engineering were trained using only the bigram frequencies as features. 

This has the added benefit of reducing the feature space from 4000 to 16.

| Classifier                                    | Score |
|-----------------------------------------------|-------|
| Logistic Regression                           | 0.846 |
| Support Vector Machine with RBF Kernel        | 0.841 |
| Support Vector Machine with Linear Kernel     | 0.846 |
| Decision Tree Classifier                      | 0.845 |
| Adaboost                                      | 0.845 |
| Random Forest Classifier (n_estimators = 100) | 0.841 |
| Naive Bayes                                   | 0.841 |
| K-Nearest Neighbors (K = 15)                  | 0.846 |
| Gradient Boosting Machine (n_estimators = 10) | 0.842 |

Using bigrams features seems to have greater predictive power! The next step is to try to improve accuracy through hyperparameter optimization using grid search and 10 fold cross validation of the best classifiers: **K-NN, SVM with Linear Kernel, Adaboost and Logistic Regression.**


#### Cross-validation and Hyperparameter Selection with Bigram Features

See **5 - Cross-validation and Hyperparameter Selection with Bigram Features**.

The next step in model selection was to optimize hyperparamters for each of the best classifier types listed above. To do this, the subset size was doubled to 20,000* and exhaustive grid search was used to optimize hyperparameters.**

**Results of Exhaustive Grid Search**

| Classifier                                | Score |
|-------------------------------------------|-------|
| Logistic Regression                       | 0.851 |
| Support Vector Machine with Linear Kernel | 0.850 |
| Adaboost                                  | 0.846 |
| K-Nearest Neighbors (K = 6)               | 0.835 |

The best classifier is logistic regression with the hyperparameters `penalty = 'l2', C = 100, solver = 'lbfgs'`.

Trained on the entire data set, this classifier achieved an accuracy of 0.852 in 10-fold cross-validation (or 0.8515 so approximately what was reported on the smaller data set). This result has the added benefit of using one of the simplest classifiers (and thus being fast, only taking 23 seconds to train on the entier data set) and being parameterized.

As found in bigram frequencies, this confirms the finding that frequency of bigram 'CG' in a sequence is the greatest predictor. Every additional instance of the bigram 'CG' in a DNA decreases the probability of the sequence being an enhancer.^

| Bigram   |   Coefficient |
|:---------|--------------:|
| AA       |        -0.002 |
| AC       |        -0.021 |
| GT       |        -0.02  |
| AG       |        -0.004 |
| CC       |         0.03  |
| CA       |         0.003 |
| CG       |        -0.068 |
| TT       |        -0.015 |
| GG       |         0.004 |
| GC       |         0.006 |
| AT       |         0.004 |
| GA       |        -0.019 |
| TG       |         0.023 |
| TA       |        -0.002 |
| TC       |         0.026 |
| CT       |        -0.002 |

\* Using a subset size of 10,000 all classifiers achieved the same accuracy.

\*\* [Randomized search has been shown to be more efficient and better](http://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf), but in this setting exhaustive grid search was possible and all that was necessary given the hyperparameter options.

\^ The odds ratio for 'CG' coefficient is 0.93, which I believe may be interpreted as a unit increase in the frequence of 'CG' decreases probability of being labeled `enhancer` by 2% (odds ratio equal to `p/(1-p)`), but need someone to check my interpretation on this.

### Non-parameterized classifiers using Majority Vote or K-NN of String Similarity

Many string similarity measures have applications in genetics in understanding regions of similarity ([sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment)). A majority vote or k-nearest neighbor classifier may be implemented using one of these measures of similarity or distance.

The similarity measures were used to analyze distributions of the scores for pairs of sequences both having label `0`, both having label `1` and having different labels.

See **6 - Needleman Wunsch**.

For example, one of the more flexible algorithms is the Needleman Wunsch (NW) algorithm. NW is a global sequence alignment algorithm which calculates a score representing the similarity of two strings allowing for mismatches, gaps (insertions or deletions) (includes a gap penalty) and dynamic programming.

A majority vote classifier assessed on the top 3 NW scores for comparisons with 10 randomly selected sequences from each class achieved an accuracy of 0.8 in 100 trials.

This is a very, very small sample and the algorithm is slow (46 minutes for this experiment) so these results are inconclusive. More analysis is required to answer questions such as "How many comparisons should be made?" and "How many votes should be counted?".

## Future Work

### Additional experiments using String Similarity Measures

String similarity measures have distributions for sequences of the same class that are distinct from distributions for different classes. This indicates these measures reveal the true class of a sequence when evaluated against sequences of each class. However as noted above these algorithms are slow and further development in a language other than python (java) may facilitate further experimentation

It would also likely be further revealling to add dimensions to the algorithms' scoring system so that a sequence is evaluated against multiple sequences from each class.

### Recurrent Neural Networks

Given the sequential nature of the data, it is very likely that a trained recurrent neural network, and even more so a recurrent neural network using long short term memory neurons, would have strong predictive power. This experiment was not possible given the computational requirements to train a RNN.*

\* *Specifically, the hardware configuration I have experience with and attempted to revive (an AWS AMI on GPU-backed instance) is now out of date and needs some rejiggering, which I felt was probably out of scope for this project.*


