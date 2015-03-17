# -*- coding: utf-8 -*-
"""
@author: Kyle, Buddy, Igii
"""

# Grabs the data from Rottoen Tomato's API and returns a JSON object which
# is the resonse given from Rotten Tomatoes

import urllib.request as req 
import urllib.parse as par
import json

apikey = 'wgm7hdwatf4x5r6fhyxcbzh3'

# q is search term (string)
# return a json object containing the 50 most related movies
def queryMovies(q):
    # Convert p to URL usable string
    q = par.quote(q)
    raw_data = req.urlopen('http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey='+apikey+'&q='+q+'&page_limit=10')
    json_data = json.loads(raw_data.read().decode())
    return json_data
    
# return a json object containing up to 50 upcoming movies
def upcomingMovies():
    raw_data = req.urlopen('http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json?apikey='+apikey+'&page_limit=50')
    json_data = json.loads(raw_data.read().decode())
    return json_data
    
#return a json object containing up to 50 opening movies
def openingMovies():
    raw_data = req.urlopen('http://api.rottentomatoes.com/api/public/v1.0/lists/movies/opening.json?apikey='+apikey+'&page_limit=50')
    json_data = json.loads(raw_data.read().decode())
    return json_data
    
# filename is the name of the file (string)
# data is the JSON data to be written (string)
def writeJSON(data,filename):
    outfile = open(filename, 'a')
    json.dump(data,outfile)
    outfile.write('\n')
    outfile.close()
        
def readJSON(filename):
    infile = open(filename, 'r')
    json_data = []
    for line in infile:
        json_data.append(json.loads(line))
    infile.close()
    return json_data
        
import csv  
  
# filename is the name of the file (string)
# returns a list of strings
def readCSV(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        l = []
        for row in reader:
            l.append(row)
        csvfile.close()
    return l;
    
from time import sleep

# Puts 2010 to 2014 movies into movies.txt
def get2010to2014Movies():   
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