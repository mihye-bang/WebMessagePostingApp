from flask import Flask, request, redirect, url_for, render_template
from tweets import add_tweet, get_all_tweets, get_tweets_by_username

app = Flask(__name__)

current_user = ''


@app.route('/')
def index():
    if current_user:
        return redirect(url_for('tweet'))
    else:
        return render_template('form.html', action='/login', header='Please Login',
                               fieldtitle='Username', fieldname='username', buttonvalue='Login')


@app.route('/logout')
def logout():
    global current_user
    current_user = ''
    return redirect(url_for('index'))


@app.route('/login', methods=['POST'])
def login():
    global current_user
    current_user = request.form['username']
    return redirect(url_for('tweet'))


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
    return render_template('tweets.html', tweets=tweets, current_user=current_user, username=username)


app.run(host='0.0.0.0', port=81)
