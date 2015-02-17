# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 14:49:27 2015

@author: Kyle
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