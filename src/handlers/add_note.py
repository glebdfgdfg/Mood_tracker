
import os
from pathlib import Path

from src.utils import csv
from datetime import datetime
from src.utils.csv import language


def add_note(session: object, assessment: int) -> None:
    table_user = Path(os.getcwd(), 'data', 'tables', f'{session.file_token}.csv')
    date = str(datetime.date(datetime.now()))
    table = csv.read(table_user)

    dates = []
    for i in table:
        dates.append(i[0])

    if date in dates:
        input(language(session.locale, 'bad_add_note'))
    else:
        csv.append([[date, assessment]], table_user)


