# -*- coding: utf-8 -*-
"""
@author: Kyle, Buddy, Igii
"""

from time import sleep


# get movie ids
file = open('movieids.txt', 'w')
titles = readCSV('movies.2010.2014.csv')
ids = []
count = 0

for title in titles:
    print(title[0] + '\n')
    sleep(0.25)
    movies = queryMovies(title[0])
    options = movies['movies']
    found = False
    
    if len(options) > 0:
        for option in options:
            if option['year'] and len(option['ratings']) == 4:
                if int(option['year']) > 2009:
                    if (~found):
                        found = True
                        file.write(str(option['id']) + '\n')
                        count += 1
                        print(str(count) + '\n')

file.close()

# read in the movie ids
movieids = []

with open('movieids.txt') as file:
    for line in file:
        movieids.append(int(line))

movieids = list(set(movieids))

# get detailed movie info
file = open('movies.txt', 'w')
count = 0

for movieid in movieids:
    sleep(0.25)
    info = detailedMovie(movieid)
    writeJSON(info, 'movies.txt')
    count += 1
    print(count)

file.close()