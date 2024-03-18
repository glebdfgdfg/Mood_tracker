
from .Menu import Menu
from src.utils.csv import language


def language_menu(session: object) -> int:
    cursor = Menu(
        menu_list=language(session.locale, 'language_menu'),
        title=language(session.locale, 'language_menu_text')
    ).menu()
    return cursor


def login_menu(session: object) -> int:
    cursor = Menu(
        menu_list=language(session.locale, 'login_menu'),
        title=language(session.locale, 'login_menu_text')
    ).menu()
    return cursor


def main_menu(session: object) -> int:
    text = language(session.locale, 'main_menu_text').replace('USERNAME', session.logged_in_user)
    cursor = Menu(
        menu_list=language(session.locale, 'main_menu'),
        title=text
    ).menu()
    return cursor


def choice_assessment(session: object) -> int:
    cursor = Menu(
        menu_list=language(session.locale, 'choice_assessment_menu'),
    ).menu()
    return cursor

