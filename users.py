import db
from werkzeug.security import generate_password_hash, check_password_hash


def password_match(username, password) -> bool:
    (id, us, pw) = db.get_user_by_username(username)
    return check_password_hash(pw, password)


def get_all_users():
    return db.get_all_users()


def create_user(username, password):
    hashed_password = generate_password_hash(password, method='sha256')
    db.create_user(username, hashed_password)


def get_user_by_username(username):
    return db.get_user_by_username(username)


def get_all_users_unfollowing():
    return db.get_all_users_following()


def get_all_users_following():
    return db.get_all_users_unfollowing()
