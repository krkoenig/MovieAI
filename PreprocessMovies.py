# -*- coding: utf-8 -*-
"""
@author: Kyle, Buddy, Igii
"""

import string
from dateutil.parser import parse

    
movies = readJSON('movies.txt')

# remove unnecessary keys
for movie in movies:
    movie.pop('critics_consensus', None)
    movie.pop('links', None)
    movie.pop('posters', None)
    movie.pop('alternate_ids', None)

# remove incomplete movies
for movie in list(movies):
    if len(movie) != 12:
        movies.remove(movie)
        
# convert cast and directors to lists of strings
for movie in movies:
    cast = []
    directors = []    
    
    for member in movie['abridged_cast']:
        cast.append(member['name'])
    
    for director in movie['abridged_directors']:
        directors.append(director['name'])
    
    movie['abridged_cast'] = cast
    movie['abridged_directors'] = directors
    
# get release month
for movie in movies:
    if 'theater' in movie['release_dates']:
        date = parse(movie['release_dates']['theater'])
    else:
        date = parse(movie['release_dates']['dvd'])
    
    month = date.strftime("%B")
    movie['month'] = month
    movie.pop('release_dates', None)

# turn release year into a string
for movie in movies:
    movie['year'] = str(movie['year'])
    
# remove spaces in some features and turn them into sentences
# helps with their bag of words later
for movie in movies:
    castlist = []
    directorlist = []
    genrelist = []
    studio = []
    
    for cast in list(movie['abridged_cast']):
        castlist.append('a' + ''.join(e for e in cast if e.isalnum()))
        
    for director in list(movie['abridged_directors']):
        directorlist.append('d' + ''.join(e for e in director if e.isalnum()))
        
    for genre in list(movie['genres']):
        genrelist.append(''.join(e for e in genre if e.isalnum()))
    
    movie['abridged_cast'] = ' '.join(castlist)
    movie['abridged_directors'] = ' '.join(directorlist)
    movie['genres'] = ' '.join(genrelist)
    movie['studio'] = 's' + ''.join(e for e in movie['studio'] if e.isalnum())

# get critic and audience rating
for movie in movies:
    if movie['ratings']['critics_rating'] != 'Rotten':
        movie['critics_rating'] = 1
    else:
        movie['critics_rating'] = 0
        
    if movie['ratings']['audience_rating'] != 'Spilled':
        movie['audience_rating'] = 1
    else:
        movie['audience_rating'] = 0
    
    movie.pop('ratings', None)
    
# remove all punctuation and make the synopses lower-case
for movie in movies:
    synopsis = movie['synopsis']
    synopsis = synopsis.lower()
    exclude = set(string.punctuation)
    synopsis = ''.join(e for e in synopsis if e not in exclude)
    synopsis = ' '.join(synopsis.split())
    movie['synopsis'] = synopsis

# write out the movie data
file = open('processedmovies.txt', 'w')

for movie in movies:
    writeJSON(movie, 'processedmovies.txt')

file.close()