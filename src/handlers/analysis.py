
import os

from colorama import *
from pathlib import Path
from datetime import datetime, timedelta

from src.utils import csv
from src.utils.csv import language


def get_week() -> list:
    this_week = []
    dt = datetime.today()
    start = dt - timedelta(days=dt.weekday())

    for num in range(7):
        date = start + timedelta(days=num)
        this_week.append(date.strftime("%Y-%m-%d"))

    return this_week


def create_grade_table(session: object, grades: list) -> None:
    weekdays = language(session.locale, 'weekdays')
    print(f"{'':^15}│{weekdays[0]:^5}│{weekdays[1]:^5}│{weekdays[2]:^5}│{weekdays[3]:^5}│{weekdays[4]:^5}│{weekdays[5]:^5}│{weekdays[6]:^5}│")
    print(f"{'─' * 15}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┤")

    grade_categories = language(session.locale, 'assessment')

    for category in reversed(grade_categories):
        row = []
        for grade in grades:
            if grade == grade_categories.index(category) + 1:
                match grade:
                    case 5:
                        row.append(Fore.GREEN + str(grade) + Style.RESET_ALL)
                    case 4:
                        row.append(Fore.BLUE + str(grade) + Style.RESET_ALL)
                    case 3:
                        row.append(Fore.CYAN + str(grade) + Style.RESET_ALL)
                    case 2:
                        row.append(Fore.YELLOW + str(grade) + Style.RESET_ALL)
                    case 1:
                        row.append(Fore.RED + str(grade) + Style.RESET_ALL)
            else:
                row.append(' ')

        row_str = ""

        for cell in row:
            if cell == ' ':
                row_str += f"{' ':^5}│"
            else:
                row_str += f"{cell:^14}│"

        print(f"{category:<15}│{row_str}")


def analysis(session: object) -> None:
    os.system('cls')
    init(autoreset=True)
    table_user = Path(os.getcwd(), 'data', 'tables', f'{session.file_token}.csv')
    data_table = csv.read(table_user)
    table = []
    this_week = get_week()
    mood_table = []
    factor = 3

    for line in data_table:
        table.append((line[0], line[1]))

    for day in this_week:
        found = False
        for line in table[1:]:
            if line[0] == day:
                mood_table.append(int(line[1]))
                found = True
                break
        if not found:
            mood_table.append(0)

    wonderful = Back.GREEN + " " * mood_table.count(5) * factor + Style.RESET_ALL
    good = Back.BLUE + " " * mood_table.count(4) * factor + Style.RESET_ALL
    okay = Back.CYAN + " " * mood_table.count(3) * factor + Style.RESET_ALL
    will_do = Back.YELLOW + " " * mood_table.count(2) * factor + Style.RESET_ALL
    bad = Back.RED + " " * mood_table.count(1) * factor + Style.RESET_ALL
    skip = Back.WHITE + " " * mood_table.count(0) * factor + Style.RESET_ALL

    chatrs = language(session.locale, 'print_chart')

    print(f'{chatrs[0]}{wonderful}{good}{okay}{will_do}{bad}{skip}\n')

    print(f'{chatrs[1]:<15}{wonderful:<15}')
    print(f'{chatrs[2]:<15}{good:<15}')
    print(f'{chatrs[3]:<15}{okay:<15}')
    print(f'{chatrs[4]:<15}{will_do:<15}')
    print(f'{chatrs[5]:<15}{bad:<15}')
    print(f'{chatrs[6]:<15}{skip:<15}')

    print()
    create_grade_table(session, mood_table)

    input()
