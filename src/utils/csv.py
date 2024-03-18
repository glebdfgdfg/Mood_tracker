
import os

from pathlib import Path


def read(file_path) -> list:
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(line.strip().split('|'))
    return data


def write(data, file_path) -> None:
    with open(file_path, 'w') as file:
        table = ''
        for row in data:
            table += '|'.join(map(str, row)) + '\n'
        file.write(table)


def append(data, file_path) -> None:
    with open(file_path, 'a') as file:
        for row in data:
            file.write('|'.join(map(str, row)) + '\n')


def language(locale, name_menu) -> list | str:
    path = Path(os.getcwd(), 'data', 'language.csv')
    with open(path, 'r', encoding='utf-8') as f:

        lines = []
        for line in f.readlines():
            lines.append(line.strip().replace('\n', ''))

        languages = lines[0].strip('|').split('|')

        columns = {}
        for lang in languages:
            columns[lang] = {}

        for line in lines[1:]:
            items = line.split('|')
            menu_name = items[0]
            for lang, options_str in zip(languages, items[1:]):
                options = options_str.split(';')
                columns[lang][menu_name] = options

        if len(columns[locale][name_menu]) == 1:
            return columns[locale][name_menu][0]
        else:
            return columns[locale][name_menu]
