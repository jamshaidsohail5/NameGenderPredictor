#!/usr/bin/env python3.5
# encoding: utf-8

"""
    gender_predictor.py
"""

from nltk import NaiveBayesClassifier, classify
import USSSALoader
import random


class GenderPredictor(object):
    
    @staticmethod
    def _load_names():
        return USSSALoader.get_name_list()
    
    @staticmethod
    def _name_features(name):
        name = name.upper()
        return {
            'last_letter': name[-1],
            'last_two': name[-2:],
            'last_three': name[-3:],
            'last_is_vowel': (name[-1] in 'AEIOUY')
        }
    
    @staticmethod
    def _get_probability_distribution(name_tuple):
        male_prob = (name_tuple[1] * 1.0) / (name_tuple[1] + name_tuple[2])
        if male_prob == 1.0:
            male_prob = 0.99
        elif male_prob == 0.00:
            male_prob = 0.01
        female_prob = 1.0 - male_prob
        return male_prob, female_prob
    
    def get_features(self):
        male_names, female_names = self._load_names()
        feature_set = list()
        for name_tuple in male_names:
            features = self._name_features(name_tuple[0])
            male_prob, female_prob = self._get_probability_distribution(name_tuple)
            features['male_prob'] =  male_prob
            features['female_prob'] = female_prob
            feature_set.append((features, 'M'))

        for name_tuple in female_names:
            features = self._name_features(name_tuple[0])
            male_prob, female_prob = self._get_probability_distribution(name_tuple)
            features['male_prob'] = male_prob
            features['female_prob'] = female_prob
            feature_set.append((features, 'F'))
        return feature_set
    
    def train_and_test(self, training_percent=0.80):
        feature_set = self.get_features()
        random.shuffle(feature_set)
        name_count = len(feature_set)
        cut_point = int(name_count * training_percent)
        train_set = feature_set[:cut_point]
        test_set = feature_set[cut_point:]
        
        self.train(train_set)
        return self.test(test_set)
    
    def train(self, train_set):
        self.classifier = NaiveBayesClassifier.train(train_set)
        return self.classifier
    
    def test(self, test_set):
        return classify.accuracy(self.classifier, test_set)
    
    def classify_name(self, name):
        features = self._name_features(name)
        return self.classifier.classify(features)
    
    def get_most_informative_features(self, n=5):
        return self.classifier.most_informative_features(n)
      

if __name__ == "__main__":
    gp = GenderPredictor()
    
    accuracy = gp.train_and_test(training_percent=0.80)
    print('\nAccuracy: {}'.format(accuracy))
    
    print("\nMost Informative Features")
    features = gp.get_most_informative_features(n=10)
    for feature in features:
        print("\t {} = {} ".format(*feature))
    
    print('\n<<<  Testing Module   >>> \nEnter "q" or "quit" to end testing module')
    while 1:
        test_name = input('\nEnter name to classify: ')
        if test_name.lower() == 'q' or test_name.lower() == 'quit':
            print('End')
            exit(1)
        if len(test_name) < 2:
            continue
        print('{} is classified as {}'.format(test_name, gp.classify_name(test_name)))
    
    
