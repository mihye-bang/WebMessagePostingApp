tweets = []


def get_all_tweets():
    return tweets


def add_tweet(tweet, username):
    t = {
        'username': username,
        'tweet': tweet
    }
    tweets.append(t)


def get_tweets_by_username(username):
    user_tweets = []
    for tweet in tweets:
        # tweet.get('username')
        if (tweet['username'] == username):
            user_tweets.append(tweet)
    return user_tweets
