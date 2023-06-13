from db import init
from flask import Flask, request, redirect, session, url_for, render_template, flash
from tweets import add_tweet, get_all_tweets, get_tweets_by_username
from users import get_all_users, password_match, get_user_by_username, create_user, get_all_users_following, get_all_users_unfollowing
import random

app = Flask(__name__)
app.secret_key = "super secret key"

init()

# inject username


@app.context_processor
def inject_user():
    username = session.get('user', None)
    return {'username': username}


@app.route('/')
def index():
    # check if the user is logged
    if 'user' in session:
        # Get last 10 tweets
        tweets = get_all_tweets(10)
        return render_template('home.html', tweets=tweets)
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    # Getting username and password from the form
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        flash('Username or password cannot be blank!', 'error')
        return render_template('login.html')

    authenticated = password_match(username, password)
    if authenticated:
        # Use Flask session
        session['user'] = username
        flash('Login was successful!', 'info')
        return redirect(url_for('index'))
    else:
        flash('Login Failed. Invalid username or password!', 'error')
        return render_template('login.html')


@app.route('/logout')
def logout():
    # Use flask session
    del session['user']
    flash('Logout was successful!', 'info')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register_post', methods=['POST'])
def register_post():
    username = request.form['username']
    password = request.form['password']

    if not username or password:
        flash('Username or password cannot be blank!', 'error')
        return render_template('register.html')

    try:
        create_user(username, password)
        user = get_user_by_username(username)
    except Exception as e:
        flash(f'Error registering {username}: {e}', 'error')
    else:
        flash(f'Successfully registered {username}', 'info')
        print(user)
        return redirect(url_for('index'))


@app.route('/tweet')
def tweet():
    return render_template('form.html', action='/save-tweet', header='What is happening?',
                           fieldtitle='Tweet', fieldname='tweet', buttonvalue='Tweet')


@app.route('/save-tweet', methods=['POST'])
def contact():
    tweet = request.form['tweet']
    if not tweet:
        flash('Tweet can not be empty!', 'error')
        return render_template('form.html', action='/save-tweet', header='What is happening?', fieldtitle='Tweet', fieldname='tweet', buttonvalue='Tweet')

    # change user info from session
    add_tweet(tweet, session['user'])
    flash('Tweet posted successfully', 'info')
    return redirect(url_for('index'))


@app.route('/users', methods=['GET'])
def users():
    # following_users = get_all_users_following()
    # unfollowing_users = get_all_users_unfollowing()
    following_users = []
    unfollowing_users = []
    all_users = get_all_users()

    final_users = []
    for user in all_users:
        # add the random bool component to user that implies following/ unfollowing
        random_follow = random.choice([True, False])
        user = (user[0], user[1], user[2], random_follow)
        final_users.append(user)

        # add users based on the bool to following/ unfollowing users
        if random_follow:
            unfollowing_users.append(user)
        else:
            following_users.append(user)

    print(final_users)
    return render_template('users_page.html', all_users=final_users, following_users=following_users, unfollowing_users=unfollowing_users)


@app.route('/tweets/<username>')
@app.route('/tweets')
def user_tweets(username=None):
    if 'user' not in session:
        return redirect(url_for('index'))

    if username:
        tweets = get_tweets_by_username(username)
    else:
        tweets = get_all_tweets()

    return render_template('tweets_page.html', tweets=tweets, tweet_user=username)


if __name__ == '__main__':
    app.debug = True
    app.run()(host='0.0.0.0', port=81)
# app.run(host='0.0.0.0', port=81)
