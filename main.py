from db import init
from flask import Flask, request, redirect, url_for, render_template
from tweets import add_tweet, get_all_tweets, get_tweets_by_username
from users import get_all_users, password_match, get_user_by_username, create_user

app = Flask(__name__)
current_user = ''

init()


@app.route('/')
def index():
    if current_user:
        return redirect(url_for('tweet'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    global current_user
    current_user = ''
    return redirect(url_for('index'))


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register_post', methods=['POST'])
def register_post():
    username = request.form['username']
    password = request.form['password']

    create_user(username, password)
    user = get_user_by_username(username)
    print(user)
    return f'Successfully registered! {username} <br> <a href="/">Login</a>'


@app.route('/login', methods=['POST'])
def login():
    global current_user
    username = request.form['username']
    password = request.form['password']
    authenticated = password_match(username, password)
    if authenticated:
        current_user = username
        return redirect(url_for('tweet'))
    else:
        return 'Login failed. Invalid username or password <br> <a href="/">Try again</a>'


@app.route('/tweet')
def tweet():
    return render_template('form.html', action='/save-tweet', header='What is happening?',
                           fieldtitle='Tweet', fieldname='tweet', buttonvalue='Tweet')


@app.route('/save-tweet', methods=['POST'])
def contact():
    tweet = request.form['tweet']
    add_tweet(tweet, current_user)
    return 'Successful received tweet ' + tweet


@app.route('/tweets/<username>')
@app.route('/tweets')
def user_tweets(username=None):
    if username:
        tweets = get_tweets_by_username(username)
    else:
        tweets = get_all_tweets()

    return render_template('tweets.html',
                           tweets=tweets,
                           current_user=current_user,
                           username=username)


app.run(host='0.0.0.0', port=81)
