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

def extract(runtime=False, \
            year=False, \
            month=False, \
            mpaa_rating=False, \
            genres=False, \
            studio=False, \
            abridged_directors=False, \
            title=False, \
            abridged_cast=False, \
            synopsis=False):
            
    
    movies = readJSON('processedmovies.txt')
    
    # start with the runtime feature
    bowfeatures = {}
    bowvocabs = {}
    rtime = separate(movies, 'runtime')
    rtime = [float(e) for e in rtime]
    rtime = np.asarray(rtime)
    rtime = preprocessing.scale(rtime)
    bowfeatures['runtime'] = np.array([rtime]).T
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
    bownames = [];
    if runtime:
        bownames.append('runtime')
    if year:
        bownames.append('year')
    if month:
        bownames.append('month') 
    if mpaa_rating:
        bownames.append('mpaa_rating') 
    if genres:
        bownames.append('genres') 
    if studio:
        bownames.append('studio') 
    if abridged_directors:
        bownames.append('abridged_directors') 
    if title:
        bownames.append('title') 
    if abridged_cast:
        bownames.append('abridged_cast') 
    if synopsis:
        bownames.append('synopsis') 
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