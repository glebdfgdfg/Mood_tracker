
import src.menu as menu
import src.handlers as handlers

from src.session import Session


def main():
    session = Session()
    session.restore_user()  # Восстановить пользователя из предыдущей сессии, если есть

    while True:
        # Проверяем, вошел ли пользователь
        if not session.is_logged_in():

            match menu.login_menu(session):
                case 1:
                    session.logged = session.login()
                    continue
                case 2:
                    session.register_user()
                    continue
                case 3:
                    match menu.language_menu(session):
                        case 1:
                            session.set_locale('EN')
                        case 2:
                            session.set_locale('RU')
                        case 3:
                            session.set_locale('UK')
                case -1:
                    print('by!')
                    session.save_session()  # Сохраняем информацию о пользователе при выходе
                    exit()

        else:
            session.save_session()
            match menu.main_menu(session):
                case 1:
                    match menu.choice_assessment(session):
                        case 1:
                            handlers.add_note(session, 5)
                        case 2:
                            handlers.add_note(session, 4)
                        case 3:
                            handlers.add_note(session, 3)
                        case 4:
                            handlers.add_note(session, 2)
                        case 5:
                            handlers.add_note(session, 1)
                        case -1:
                            print('by!')
                            session.save_session()  # Сохраняем информацию о пользователе при выходе
                            exit()
                case 2:
                    handlers.analysis(session)
                case 3:
                    match menu.language_menu(session):
                        case 1:
                            session.set_locale('EN')
                        case 2:
                            session.set_locale('RU')
                        case 3:
                            session.set_locale('UK')
                case 4:
                    print('by!')
                    session.logout()  # Пользователь выходит из сессии
                case -1:
                    print('by!')
                    session.save_session()  # Сохраняем информацию о пользователе при выходе
                    exit()
