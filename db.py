import sqlite3
conn = sqlite3.connect('tweets.db')     # creates a tweets.db file

# assume it's as a handle to run a SQLite commands. allows executing
cursor = conn.cursor()

# 'id' is a keyword and so put _ to avoid conflicts
# cursor.execute('''CREATE TABLE if not exists tweets (
#         _id integer primary key autoincrement,
#         tweet text,
#         username text
#     )''')


def init():
    try:
        cursor.execute('''CREATE TABLE tweets (
            _id integer primary key autoincrement,
            tweet text,
            username text
        )''')
    except sqlite3.OperationalError as e:
        print('Table tweet alrady exists. Skipping creation.')

    conn.commit()   # don't forget this - saying I'm done with executing, so it saves the database
