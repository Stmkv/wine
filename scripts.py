import pandas as pd
import pprint

from collections import defaultdict


def get_format_year(year: int) -> str:
    last_num = int(str(year)[-1])
    if 11 <= year <= 2:
        return f"лет"
    elif last_num == 1:
        return f"год"
    elif 2 <= last_num <= 4:
        return f"года"
    else:
        return f"лет"


def read_exel_file(file):
    excel_file = pd.read_excel(file, usecols=['Категория',
                                              'Название',
                                              'Сорт',
                                              'Цена',
                                              'Картинка',
                                              'Акция'],
                               keep_default_na=False)
    return excel_file

def get_dict_with_alcohol(file):
    alcohols = defaultdict(list)

    for wine in file:
        category = wine['Категория']
        alcohols[category].append(wine)
    return dict(alcohols)
