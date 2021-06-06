from fastapi_login import LoginManager
import os
import json

abspath = os.path.abspath(__file__)
# print("abspath: ", abspath)
dname = os.path.dirname(abspath)
# print("dname: ", dname)
file_name = os.path.join(dname, "app.ini")
# print("file_name: ", file_name)
with open(file_name, "r") as f:
    INI = json.load(f)
SECRET = INI["SECRET"]

manager = LoginManager(SECRET,
                       '/login',
                       use_cookie=True)

DB = {
    'users': {
        'johndoe@mail.com': {
            'name': 'John Doe',
            'password': 'hunter2'
        }
    }
}


@manager.user_loader
def query_user(user_id: str):
    """
    Get a user from the db
    :param user_id: E-Mail of the user
    :return: None or the user object
    """
    return DB['users'].get(user_id)
