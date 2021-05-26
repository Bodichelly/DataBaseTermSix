import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from utils.translate_city_name import translate_city_name


def short_month_name_to_long(short: str) -> str:
    if short == 'dec':
        return 'December'
    elif short == 'may':
        return 'May'
    elif short == 'jun':
        return 'June'


def get_essential_columns_names(short: bool = False):
    if short:
        return np.array(['city', 'salary', 'promotion', 'position', 'language'])
    else:
        return np.array(['city', 'salary', 'promotion', 'position', 'language', 'year', 'month'])


def slice_filename(filename: str):
    return {
        'year': filename[:4],
        'month': short_month_name_to_long(filename[5:8])
    }


def adjust_str(data) -> str:
    data_str = str(data)
    data_str = data_str.lstrip().rstrip().strip('.').strip('@').strip(',')
    return translate_city_name(data_str)


def adjust_int(data) -> int:
    data_int = int(data)
    test = lambda x: x if x > 0 else 0
    return test(data_int)


def get_data_frame():

    frames = []

    for file in os.listdir(os.path.abspath("./data_clean")):
        if file.endswith(".csv"):
            addition_data = slice_filename(file)
            salaries_data = pd.read_csv('./data_clean/'+file)[get_essential_columns_names(True)]
            salaries_data['month'] = addition_data['month']
            salaries_data['year'] = addition_data['year']
            frames.append(salaries_data)

    result = pd.concat(frames)
    result['city'] = result['city'].apply(adjust_str)
    result['promotion'] = result['promotion'].apply(adjust_int)
    #print(result[pd.isnull(result).any(axis=1)]['position'].unique())
    return result


if __name__ == "__main__":
    get_data_frame()
