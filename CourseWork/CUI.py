from DB_utils.db_utils import insert_data_frame_into_db
from DB_utils.mongodb import mongo_manager
from data_analysis_utils.data_manage_utils import get_data_frame
from show.language_statistics import language_statistics
from show.predict_salary import predict_salary
from show.salary_statistics import salary_statistics
from show.show_data import get_languages, get_years
import math
from utils.console_utils import clear_console


def select_from_list(item_list):
    while True:
        print("#################### Select Command ####################")
        # clear_console()
        for index, item in enumerate(item_list):
            if not isinstance(item, str):
                continue
            print("[{:d}] {:s}".format(index, str(item)))
        print("Enter code: ")
        num = int(input())
        if num < 0 or num >= len(item_list):
            continue
        return [item_list[num], num]


main_menu = [
    'Salary statistics',
    'Languages popularity statistics per year',
    'Predict salary for a specific language',
    'DB manipulation',
    'Exit'
]

db_menu = [
    'Load data from svg',
    'Clear DB',
    'Exit'
]


def CUI():
    while True:
        command = select_from_list(main_menu)
        if command[1] == 0:
            lang = select_from_list(get_languages())
            salary_statistics(lang[0])
        elif command[1] == 1:
            year = select_from_list(get_years())
            language_statistics(year[0])
        elif command[1] == 2:
            lang = select_from_list(get_languages())
            predict_salary(lang[0])
        elif command[1] == 3:
            db_command = select_from_list(db_menu)

            if db_command[1] == 0:
                insert_data_frame_into_db(mongo_manager, get_data_frame())
            elif db_command[1] == 1:
                mongo_manager.delete_all()
        elif command[1] == 4:
            break