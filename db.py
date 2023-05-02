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

    conn.commit()   # don't forget this - saying I'm done with executing, so it saves the database


def insert_tweet(tweet, username):
    cursor.execute('INSERT INTO tweets VALUES (null, :tweet, :username)', {
                   'tweet': tweet, 'username': username})
    conn.commit()


def get_all_tweets():
    cursor.execute('SELECT * FROM tweets')
    tweet = cursor.fetchall()
    return tweet


def get_tweets_by_username(username):
    cursor.execute(
        'SELECT * FROM tweets WHERE username = :username', {'username': username})
    tweets = cursor.fetchmany(10)
    return tweets
