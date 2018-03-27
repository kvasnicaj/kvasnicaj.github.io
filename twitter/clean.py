from json import loads

tweets_filename = 'tweets.json'
tweets_file = open(tweets_filename, "r")

for line in tweets_file:
    statuses = loads(line.strip())
    for tweet in statuses['statuses']:
        print(tweet['created_at'])
        print(tweet['id'])
        print(tweet['user']['screen_name'])
        print(tweet['text'])
