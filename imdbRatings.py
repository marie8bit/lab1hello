#import urllib and json
import urllib
from urllib import request
import json
#allow user to uenter a movie name to get rating
print("Enter the name of the Movie you would like to get rating for")
title = input()
#change format to htlm format
newTitle=title.replace(" ", "+")
print (newTitle)
#generate url (API)
url ="http://www.omdbapi.com/?t="+newTitle
#print (url)
#get json from url request
r = urllib.request.urlopen(url)
#decode json object
json_dat= r.read().decode()
#change data into a json object
json.object = json.loads(json_dat)
#print requested rating for user
print ("The IMDB rating for "+title+" is "+json.object['imdbRating'])
