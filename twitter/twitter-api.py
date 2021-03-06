from json import dumps
from twitter import OAuth, Twitter
from config import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET

''' access and consumer keys should be defined in token.py '''

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)

tweets = twitter.search.tweets(q='#frenchie', result_type='recent', count=50)

print(dumps(tweets))
