import pandas as pd
from DB_utils.mongodb import mongo_manager
from data_analysis_utils.data_manage_utils import get_essential_columns_names


def get_unique_columns_value(column: str):
    data_arr = mongo_manager.find_all({'language': {'$ne': 'NaN'}})
    variables = get_essential_columns_names()
    long_df = pd.DataFrame([i for i in data_arr], columns=variables).sort_values(column)
    return long_df[column].unique()


def get_years():
    return get_unique_columns_value('year')


def get_languages():
    return get_unique_columns_value('language')


def get_positions():
    return get_unique_columns_value('position')


def get_cities():
    return get_unique_columns_value('city')