import vk
import getpass

APP_ID = 6695750


def get_user_login():
    return input('login: ')


def get_user_password():
    return getpass.getpass(prompt='password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends, online'
    )

    api = vk.API(session)
    online_user_ids = api.friends.getOnline(fields='nickname', v=5.85)
    online_friends = api.users.get(user_ids=online_user_ids, v=5.85)
    return online_friends
    # например, api.friends.get()


def output_friends_to_console(friends_online):
    for user in friends_online:
        print(user['first_name'], user['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
