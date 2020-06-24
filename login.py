from database import table


def chech_validSignup(user):  # To check if the table filled completely during signup

    if user.s_full_name.text:

        if user.s_user_name.text:

            if " " not in user.s_user_name.text:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def check_alreadyUser(user):  # To check if the user already  exist during signup

    table.c.execute('select *from login_data where user_name = :user_name',
                    {"user_name": user.s_user_name.text})
    already_user = table.c.fetchone()

    if not already_user:
        return True
    else:
        return False


# To check if both the password is correct during signup
def check_passwordSignup(user):
    if  user.s_password.text :
        if user.s_password.text == user.s_confirm_password.text:
            return True
        else:
            return False
    else:
        return False


def password_User(user):  # return the password of the user name
    table.c.execute('select password from login_data where user_name = :user_name',
                    {"user_name": user.user_name.text})
    return table.c.fetchall()
