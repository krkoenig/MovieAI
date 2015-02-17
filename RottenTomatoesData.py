# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 13:16:48 2015

@author: Kyle
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
    raw_data = req.urlopen('http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey='+apikey+'&q='+q+'&page_limit=1')
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
    
# p is the movie id (integer) 
# return a json object containing the cast of the requested movie   
def castMovie(p):
    raw_data = req.urlopen('http://api.rottentomatoes.com/api/public/v1.0/movies/'+str(p)+'/cast.json?apikey='+apikey+'&page_limit=50')
    json_data = json.loads(raw_data.read().decode())
    return json_data

# p is the movie id (integer)
# return a json object containing the reviews of the requested movie
def reviewMovie(p):
    raw_data = req.urlopen('http://api.rottentomatoes.com/api/public/v1.0/movies/'+str(p)+'/reviews.json?apikey='+apikey+'&page_limit=50')
    json_data = json.loads(raw_data.read().decode())
    return json_data 

# filename is the name of the file (string)
# data is the JSON data to be written (string)
def writeJSON(data,filename):
    outfile = open(filename, 'a')
    json.dump(data,outfile)
    outfile.write('\n')
    outfile.close()
        
# 
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