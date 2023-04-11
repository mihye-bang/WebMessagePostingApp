from flask import Flask, request, redirect, url_for

from myfile import someFunction

app = Flask(__name__)
tweets = []

current_user = ''


def get_html_form(action, header, field_title, field_name, button_value):
    return f'''
        <form method=POST action="{action}">
        <h3>{header}</h3>
        {field_title}: <input type="text" name="{field_name}" >
        <input type="submit" value="{button_value}">
        </form> 
        '''


if __name__ == "__main__":
    print(f"First Line: {__name__}")

someFunction()


@app.route('/')
def index():
    if current_user:
        return redirect(url_for('tweet'))
    else:
        return get_html_form('/login', 'Please Login', 'Username', 'username', 'Login')


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
    tweets.append(tweet)
    return 'Successful received tweet ' + tweet


@app.route('/my_tweets')
def my_tweets():
    tweet = ''
    for twt in tweets:
        tweet += f'<li>{twt}</li>'

    return f'''
    <h3>All my tweets</h3>
    <ol>{tweet}</ol>
    '''


app.run(host='0.0.0.0', port=81)
