
import os
import time
import keyboard


class Menu:

    def __init__(
            self,
            menu_list: list,
            title='',
            cursor='> ',
            delimiter='.',
            numbering=True,
            clear_console=True
    ):
        self._menu_list = menu_list
        self._cursor = cursor
        self._delimiter = delimiter
        self._title = title
        self._numbering = numbering
        self._clear_console = clear_console
        self._delay = 0.1

    def _print(self, cursor_menu) -> None:
        if self._clear_console:
            os.system('cls')

        if self._title:
            print(self._title)

        for string in self._menu_list:
            serial_number = self._menu_list.index(string) + 1

            if self._numbering:
                numbering = str(serial_number)
            else:
                numbering = ''

            if serial_number == cursor_menu:
                print(self._cursor + numbering + self._delimiter + string)
            else:
                spaces = ' ' * len(self._cursor)
                print(spaces + numbering + self._delimiter + string)

    def menu(self) -> int:
        cursor_menu = 1
        end_cursor_menu = len(self._menu_list)
        self._print(cursor_menu)

        while True:
            event = keyboard.read_event(suppress=True)
            if event.name == 'backspace':
                time.sleep(self._delay)
                return 0

            elif event.name == 'q':
                return -1

            elif event.name == 'up' and cursor_menu != 1:
                cursor_menu -= 1
                self._print(cursor_menu)
                time.sleep(self._delay)

            elif event.name == 'down' and cursor_menu < end_cursor_menu:
                cursor_menu += 1
                self._print(cursor_menu)
                time.sleep(self._delay)

            if event.name == 'space':
                time.sleep(self._delay)
                return cursor_menu
