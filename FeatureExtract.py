# -*- coding: utf-8 -*-
"""
@author: Kyle, Buddy, Igii
"""

import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing


# separate out a particular feature
def separate(movies, feature):
    features = []
    
    for movie in movies:
        features.append(movie[feature])

    return features

# get the bag of words for a particular feature
def bagOfWords(feature, stopwords):
    vectorizer = CountVectorizer(analyzer = "word", \
                                 stop_words = stopwords, \
                                 min_df = 2)
    features = vectorizer.fit_transform(feature)
    features = features.toarray()
    vocab = vectorizer.get_feature_names()
    
    return features, vocab


movies = readJSON('processedmovies.txt')

# start with the runtime feature
bowfeatures = {}
bowvocabs = {}
runtime = separate(movies, 'runtime')
runtime = [float(e) for e in runtime]
runtime = np.asarray(runtime)
runtime = preprocessing.scale(runtime)
bowfeatures['runtime'] = np.array([runtime]).T
bowvocabs['runtime'] = ['runtime']

# for each bag of words feature, get its features
bows = {'year': None, 'month': None, 'mpaa_rating': None, \
        'genres': None, 'studio': None, 'abridged_directors': None, \
        'title': 'english', 'abridged_cast': None, 'synopsis': 'english'}

for bowname in bows.keys():
    raw = separate(movies, bowname)
    features, vocab = bagOfWords(raw, bows[bowname])
    bowfeatures[bowname] = features
    bowvocabs[bowname] = vocab
    
# append all of the features and vocabs together
bownames = ['runtime', 'year', 'month', 'mpaa_rating', 'genres', 'studio', \
            'abridged_directors', 'title', 'abridged_cast', 'synopsis']
features = np.empty(shape = (1193, 0))
featurenames = []

for bowname in bownames:
    features = np.concatenate((features, bowfeatures[bowname]), axis = 1)
    featurenames.extend(bowvocabs[bowname])
    
# get movie ratings
criticratings = separate(movies, 'critics_rating')
audienceratings = separate(movies, 'audience_rating')

# save ratings and features
cratings = open('criticratings.p', 'wb')
aratings = open('audienceratings.p', 'wb')
ffeatures = open('features.npy', 'wb')
pickle.dump(criticratings, cratings)
pickle.dump(audienceratings, aratings)
np.save(ffeatures, features)