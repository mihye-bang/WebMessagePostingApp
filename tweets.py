import db


def get_all_tweets(limit=100):
    return db.get_all_tweets(limit)


def add_tweet(tweet, username):
    db.insert_tweet(tweet, username)


def get_tweets_by_username(username):
    return db.get_tweets_by_username(username)
