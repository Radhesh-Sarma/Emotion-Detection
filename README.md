# Emotion-Detection
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9cb6056a6cdd46928000c7f205ba35c9)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Radhesh-Sarma/Emotion-Detection&amp;utm_campaign=Badge_Grade)

## Introduction
This is an Emotion Detection project, which classifies the emotion of a person in the image into 'sad' and 'not sad' categories, with the help of Genetic Algorithms by making use of the best subset of features.

## Method
* Developed in Python, with the help of libraries like numpy, pandas, skit-learn and matplot.
* Initially, the image dataset is preprocessed using the OpenFace Toolkit (http://cmusatyalab.github.io/openface), which generates a csv file containing the facial landmarks of each image fed in as an input.
* These features are then normalized, and the dataset is divided into 70% for training, 10% for validation and 20% for testing.
* To select the best features, the data is preprocessed by constructing a binary matrix which tells the user, whether to take the particular feature for classification or not.
* 1: Represents feature selected in the best subset.
* 0: Represents feature excluded from the best subset.
* Next, the Genetic Algorithm runs over the training dataset, training the classifier models Logistic Regression and Support Vector Machine over the training dataset and validating them over the validation data.
* Accuracy of the model = No. of correctly classified samples/ Total No. of Samples
* The Genetic algorithm is implemeted with 3 different variations of Parent Selection, Crossover and Mutation.
* Finally the best subset of features is obtained through the algorithm.
* The Hyperparameters like the type of parent selection technique, crossover, mutation and classifier model are tuned through Grid Search.

## Types of Parent Selection implemented
* Rank Selection
* Tournament Selection
* Roulette wheel Selection
## Types of Crossover implemented
* Uniform crossover
* Two point crossover
* Single point crossover
## Types of Mutation implemented
* Bit flip mutation
* Swap mutation
* Inverse mutation
## Types of Classification Models used
* Logistic Regression
* Support Vector Machines

Please check results.xlsx for more Details about the Results obtained.
