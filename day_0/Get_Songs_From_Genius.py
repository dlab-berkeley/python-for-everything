#!/usr/bin/python

import urllib
import urllib2
import json
song_url = 'http://genius-api.com/api/songInfo' #Song information
artist_url = 'http://genius-api.com/api/artistInfo' #artist info
values = {'name' : 'Liquid Swords',
          'genre' : 'rap'}
data = urllib.urlencode(values)
req = urllib2.Request(song_url, data)
response = urllib2.urlopen(req)
the_page = response.read()

print(the_page)

# decoded_data = json.loads(the_page)


#How to get songs from Rap Genius
#curl -d 'name=Liquid Swords' -d 'genre=rap' 'http://genius-api.com/api/songInfo'
