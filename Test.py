# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 14:49:27 2015

@author: Kyle
"""

#test = queryMovies('a',2)
#print(test)
#for a in test['movies']:
#    print(a['title'])
    
l = readCSV('example.csv')
print(l)
print('\n')
for row in l:
    test = queryMovies(row,1)
    print(test['movies'][0]['synopsis'] + '\n')