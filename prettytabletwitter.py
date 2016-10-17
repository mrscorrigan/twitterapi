import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable

CONSUMER_KEY = 'GTjUJERmZrs2WgWHG7NE6mnGw'
CONSUMER_SECRET = 'Vh3Iw4vXVEyt1aKUH2vGUT9vNCRZwezFoH9ulSTJVuI6qwx9NL'
OAUTH_TOKEN =  '153560052-zTx94GCRe5nvcPN9YyxlI5CyJ1jH3ZQgOSWwH11j'
OAUTH_TOKEN_SECRET =  'JQjZJI9N9KkNoFbe0fzwV8EGDUNzwKuHl6G2s20vY9st3'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 50
query = 'Weather'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results]
                #for mention in status._json['entities']['user_mentions']]


hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]

words = [w for t in status_texts
           for w in t.split()]

for entry in [screen_names, hashtags, words]:
        counter = Counter(entry)
       # print counter.most_common()[:10] # the top 10 results
        #print

for label, data in (('Text', status_texts), ('Screen Name', screen_names), ('Word', words)):
    table = PrettyTable(field_names=[label, 'Count'])
    counter = Counter(data)
    [table.add_row(entry)
    for entry in counter.most_common()[:10] ]
    table.align[label], table.align['Count'] = 'l', 'r' # align the columns
    print table


# print json.dumps(status_texts[0:5], indent=1)
# print json.dumps(screen_names[0:5], indent=1)
# print json.dumps(hashtags[0:5], indent=1)
# print json.dumps(words[0:5], indent=1)