import sqlite3
# creates a tweets.db file
conn = sqlite3.connect('tweets.db', check_same_thread=False)

# assume it's as a handle to run a SQLite commands. allows executing
cursor = conn.cursor()


def init():
    # try:
    #     cursor.execute('''CREATE TABLE tweets(
    #     _id integer primary key autoincrement,
    #     tweet text,
    #     username text
    # )''')
    # except sqlite3.OperationalError as e:
    #     print('Table tweet alrady exists. Skipping creation.')

    # instead of catching the error, better to use 'if not exist' for better peformance
    # 'id' is a keyword and so put _ to avoid conflicts
    cursor.execute('''CREATE TABLE if not exists tweets (
        _id integer primary key autoincrement,      
        tweet text,
        username text
    )''')
    # it can also be username text UNIQUE
    cursor.execute('''CREATE TABLE if not exists users (
        _id integer primary key autoincrement,
        username text,
        password text, 
        UNIQUE(username)
    )''')

    conn.commit()   # don't forget this - saying I'm done with executing, so it saves the database


def create_user(username, password):
    cursor.execute('INSERT INTO users VALUES (null, :username, :password)', {
                   'username': username, 'password': password})
    conn.commit()


def insert_tweet(tweet, username):
    cursor.execute('INSERT INTO tweets VALUES (null, :tweet, :username)', {
                   'tweet': tweet, 'username': username})
    conn.commit()


def get_all_tweets(limit):
    cursor.execute('SELECT * FROM tweets order by _id desc')
    tweets = cursor.fetchmany(limit)
    return tweets


def get_all_users():
    cursor.execute('SELECT * FROM users order by _id desc')
    users = cursor.fetchall()
    return users


def get_tweets_by_username(username):
    cursor.execute(
        'SELECT * FROM tweets WHERE username = :username', {'username': username})
    tweets = cursor.fetchmany(10)
    return tweets


def get_user_by_username(username):
    cursor.execute(
        'SELECT * FROM users WHERE username = :username', {'username': username})
    user = cursor.fetchone()
    return user


def get_all_users_following():
    []


def get_all_users_unfollowing():
    []
