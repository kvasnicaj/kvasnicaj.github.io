'''
import twitter statuses to Mongodb, oauth setting is in config.py
'''
from pymongo import MongoClient
from twitter import OAuth, Twitter
import pandas as pd
from config import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth=oauth)

# search tweets
tweets = twitter.search.tweets(q='Praha', result_type='recent', count=50)

# connect to mongodb
client = MongoClient('localhost', 27017)
# select database
db = client.test

# insert statuses to collection (1 status = 1 document)
for line in tweets['statuses']:
    db.tweets.insert(line)

# save mongodb collection to dataframe
df = pd.DataFrame(list(db.tweets.find()))
print(pd.info())
