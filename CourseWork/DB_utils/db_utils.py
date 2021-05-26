from DB_utils.db_manager import DBManager
from data_analysis_utils.data_manage_utils import get_essential_columns_names
from utils.console_utils import clear_console


def create_dictionary(row):
    arr = get_essential_columns_names()
    dictionary = {}
    for field in arr:
        dictionary[field] = row[field]
    return dictionary


def insert_data_frame_into_db(manager: DBManager, data_frame):
    i = 0
    for index, row in data_frame.iterrows():
        # clear_console()
        print(i)
        dictionary = create_dictionary(row)
        if dictionary:
            manager.insert(dictionary)
        i += 1
