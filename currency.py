import urllib
from urllib import request
import json
print("Enter the name of the Movie you would like to get rating for")
title = input()
newTitle=title.replace(" ", "+")
print (newTitle)
url ="http://www.omdbapi.com/?t="+newTitle
print (url)
r = urllib.request.urlopen(url)
json_dat= r.read().decode()
json.object = json.loads(json_dat)
print (json.object['imdbRating'])
