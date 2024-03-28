import os
import json
import getpass
from pathlib import Path
from datetime import datetime

from src.utils import csv
from src.utils import hasher
from src.utils.csv import language


class Session:
    def __init__(self):
        self._path_session = Path(os.getcwd(), 'data', 'session.json')
        self._path_users_table = Path(os.getcwd(), 'data', 'users.csv')
        self.logged_in_user = None
        self.last_logout_time = None
        self.file_token = None
        self.locale = 'EN'

    def register_user(self) -> bool:
        name = input(language(self.locale, 'enter_name'))

        while True:
            name_hash = hasher.username_hash(name)
            pass_token1 = hasher.password_hash(
                getpass.getpass(language(self.locale, 'enter_pass'))
            )
            pass_token2 = hasher.password_hash(
                getpass.getpass(language(self.locale, 'enter_pass_again'))
            )
            if pass_token1 == pass_token2:
                pass_token = pass_token1
                self.file_token = hasher.file_token(name_hash, pass_token)
                break
            else:
                os.system('cls')
                print(language(self.locale, 'bad_pass'))

        users = csv.read(self._path_users_table)

        temp_users = []
        for user in users:
            temp_users.append(user[0])

        if name not in temp_users:
            self.logged_in_user = name
            users.append([name, pass_token])
            user_table_path = Path(
                os.getcwd(), 'data', 'tables', f'{self.file_token}.csv'
            )

            csv.write(users, self._path_users_table)
            csv.write([['datetime', 'mood_assessment']], user_table_path)
            print(language(self.locale, 'good_reg'))
            return True
        else:
            input(language(self.locale, 'bad_reg'))
            return False

    def login(self) -> bool:
        name = input(language(self.locale, 'enter_name'))

        name_token = hasher.username_hash(name)
        pass_token = hasher.password_hash(
            getpass.getpass(language(self.locale, 'enter_pass'))
        )

        users = csv.read(self._path_users_table)

        for user in users:
            if user[0] == name and user[1] == pass_token:
                self.logged_in_user = name
                self.file_token = hasher.file_token(name_token, pass_token)
                return True

        input(language(self.locale, 'bad_login'))
        return False

    def logout(self) -> None:
        self.logged_in_user = None
        self.last_logout_time = None
        self.file_token = None
        self.locale = 'EN'

        with open(self._path_session, "w") as f:
            data = {
                'logged_in_user': None,
                'last_logout_time': None,
                'locale': None,
            }
            f.write(json.dumps(data, indent=4))

    def is_logged_in(self) -> None:
        return self.logged_in_user is not None

    def save_session(self) -> None:
        self.last_logout_time = datetime.now()
        if self.logged_in_user:
            with open(self._path_session, "w") as f:
                data = {
                    'logged_in_user': self.logged_in_user,
                    'last_logout_time': str(self.last_logout_time),
                    'locale': self.locale,
                }
                f.write(json.dumps(data, indent=4))

    def restore_user(self) -> bool:
        if os.path.exists(self._path_session):
            with (open(self._path_session, "r") as f):
                data = json.load(f)
                if data['logged_in_user'] and data['last_logout_time']:
                    self.logged_in_user = data['logged_in_user']
                    self.last_logout_time = datetime.fromisoformat(
                        data['last_logout_time']
                    )
                    self.locale = data['locale']

                    print(language(
                        self.locale,
                        'welcome_user').replace('USERNAME', self.logged_in_user)
                    )

                    while True:
                        name_hash = hasher.username_hash(self.logged_in_user)
                        pass_token = hasher.password_hash(
                            getpass.getpass(language(self.locale, 'enter_pass'))
                        )
                        users = csv.read(self._path_users_table)

                        for user in users:
                            if user[0] == self.logged_in_user and \
                                    user[1] == pass_token:
                                self.file_token = hasher.file_token(
                                    name_hash,
                                    pass_token
                                )
                                return True

                        print(language(self.locale, 'bad_pass'))
                else:
                    return False
        else:
            return False

    def set_locale(self, locale) -> None:
        self.locale = locale

        if os.path.exists(self._path_session):
            with open(self._path_session, 'r') as f:
                data = json.load(f)
                data['locale'] = self.locale
            with open(self._path_session, 'w') as f:
                f.write(json.dumps(data, indent=4))

        else:
            with open(self._path_session, "w") as f:
                data = {
                    'logged_in_user': self.logged_in_user,
                    'last_logout_time': self.last_logout_time,
                    'locale': self.locale,
                }
                f.write(json.dumps(data, indent=4))
