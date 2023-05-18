from flask import session


def create_session(newuser):
    session['user'] = newuser


def get_session():
    return session['user']


def has_session():
    return 'user' in session


def del_session():
    del session['user']
