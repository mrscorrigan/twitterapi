import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'GTjUJERmZrs2WgWHG7NE6mnGw'
CONSUMER_SECRET = 'Vh3Iw4vXVEyt1aKUH2vGUT9vNCRZwezFoH9ulSTJVuI6qwx9NL'
OAUTH_TOKEN =  '153560052-zTx94GCRe5nvcPN9YyxlI5CyJ1jH3ZQgOSWwH11j'
OAUTH_TOKEN_SECRET =  'JQjZJI9N9KkNoFbe0fzwV8EGDUNzwKuHl6G2s20vY9st3'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

#print json.dumps(dub_trends, indent=1)
#print json.dumps(lon_trends, indent=1)

print common_trends