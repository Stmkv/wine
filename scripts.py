import pprint
from collections import defaultdict

import pandas as pd


def get_format_year(year: int) -> str:
    last_two_nums = int(str(year)[-2:])
    if 11 <= last_two_nums <= 19:
        return "лет"
    elif last_two_nums % 10 == 1:
        return "год"
    elif 2 <= last_two_nums % 10 <= 4:
        return "года"
    else:
        return "лет"


def read_exel_file(file):
    excel_file = pd.read_excel(
        file,
        usecols=["Категория", "Название", "Сорт", "Цена", "Картинка", "Акция"],
        keep_default_na=False,
    )
    return excel_file


def get_dict_with_alcohol(file):
    alcohols = defaultdict(list)

    for wine in file:
        category = wine["Категория"]
        alcohols[category].append(wine)
    return dict(alcohols)
