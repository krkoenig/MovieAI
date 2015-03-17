# -*- coding: utf-8 -*-
"""
@author: Kyle, Buddy, Igii
"""

#test = queryMovies('a',2)
#print(test)
#for a in test['movies']:
#    print(a['title'])
    
from time import sleep     
    
open('movies.txt', 'w').close()

l = readCSV('Movies.2010.2014.csv')
for row in l:
    sleep(0.25)
    print(row[0] + '\n')
    test = queryMovies(row[0])
    if len(test['movies']) > 0:
        test = test['movies'][0]
        writeJSON(test,'movies.txt')
        print(test['id'] + '\n')
    
l = readJSON('movies.txt')
for r in l:
    print(r['title'])
    print ('\n')
    
    
    
#####################################
# how to load features, and ratings #
#####################################
    
import pickle
import numpy as np


a = open('criticratings.p', 'rb')
b = open('audienceratings.p', 'rb')
c = open('features.npy', 'rb')
criticratings = pickle.load(a)
audienceratings = pickle.load(b)
features = np.load(c)
a.close()
b.close()
c.close()