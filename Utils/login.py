from webapp2_extras.users import users


def comprobarLogin():
    usr = users.get_current_user()
    nick = None
    if usr:
        login_out_url = users.create_logout_url("/")
        nick = usr.nickname()
    else:
        login_out_url = users.create_login_url("/")

    return login_out_url, nick