import sqlite3
conn = sqlite3.connect('tweets.db')     # creates a tweets.db file

c = conn.cursor()   # assume it's as a handle to run a SQLite commands. allows executing

c.execute('''CREATE TABLE tweets (
    _id integer primary key autoincrement,
    tweet text,
    username text
)''')

conn.commit()   # don't forget this
