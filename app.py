from flask import Flask, request, redirect, url_for
from tweets import add_tweet, get_all_tweets, get_tweets_by_username

app = Flask(__name__)

current_user = ''


def get_html_form(action, header, field_title, field_name, button_value):
    return f'''
        <form method=POST action="{action}">
        <h3>{header}</h3>
        {field_title}: <input type="text" name="{field_name}" >
        <input type="submit" value="{button_value}">
        </form> 
        '''


@app.route('/')
def index():
    if current_user:
        return redirect(url_for('tweet'))
    else:
        return get_html_form('/login', 'Please Login', 'Username', 'username', 'Login')


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
    return get_html_form('/save-tweet', 'What is happening?', 'Tweet', 'tweet', 'Tweet')


@app.route('/save-tweet', methods=['POST'])
def contact():
    tweet = request.form['tweet']
    add_tweet(tweet, current_user)
    return 'Successful received tweet ' + tweet


@app.route('/tweets/<username>')
@app.route('/tweets')
def user_tweets(username=None):
    tweet_html = ''
    for tweet in get_tweets_by_username(username):
        tweet_html += f'<li>{tweet["tweet"]} by {tweet["username"]}</li>'
    return f'''
    <h3>All my tweets</h3>
    <ol>{tweet_html}</ol>
    <br>
    <br>
    <a href="/logout">Logout {current_user}</a>
    '''


app.run(host='0.0.0.0', port=81)
