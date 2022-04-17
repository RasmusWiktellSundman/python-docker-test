from .. import app, auth

@auth.verify_password
def verify_password(username, password):
    if username in app.config['USERS'] and app.config['USERS'][username] == password:
        return True
    return False