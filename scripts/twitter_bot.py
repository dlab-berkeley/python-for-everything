#!/bin/env python

import json
from requests_oauthlib import OAuth1Session
import time
import yaml

# Normally we would organize this as a class, but we haven't talked
# about how or why to do that yet

# Getting credentials
with open('../etc/creds.yml', 'r') as f:
    creds = yaml.load(f)

# Setting up Twitter OAuth object
twitter = OAuth1Session(**creds)
search_endpoint = "https://api.twitter.com/1.1/search/tweets.json"
post_endpoint = "https://api.twitter.com/1.1/statuses/update.json"

# Enter your search parameters here
search_parameters = {'q' : 'DlabAtBerkeley'}

# Here is our main function
def main():
    # You may want to set a condition here, like 'never on Sunday'
    while True:
        r = twitter.get(search_endpoint, search_parameters)
        if r.ok:
            for tweet in r:
                status = r['text']
                # You may want to set a condition here
                if True:
                    # Enter your post parameters here
                    post_parameters = {
                        'status' : status + ' @dillonniederhut'
                    }
                    p = r.post(post_endpoint, post_parameters)
                    if p.ok:
                        print(time.asctime(), post_parameters, p.status)
                    else raise BaseException(r.reason)
                    time.sleep(30)
        # Else, iff you are exceeding the rate limit
        elif r.status_code == 429:
            time.sleep(60)
        else:
            raise BaseException(r.reason)

# This bit of syntax tells Python not to run this code when imported
# into an interactive session, but only when it is called as a program
# from bash or another program.

if __name__ == 'main':
    main()
