from CUI import select_from_list, CUI
from DB_utils.db_utils import create_dictionary, insert_data_frame_into_db
from DB_utils.mongodb import mongo_manager
from data_analysis_utils.data_manage_utils import get_data_frame
from show.language_statistics import language_statistics
from show.predict_salary import predict_salary
from show.salary_statistics import salary_statistics

# command to insert data from dataset into DB
# insert_data_frame_into_db(mongo_manager, get_data_frame())
# command to clean collection
# mongo_manager.delete_all()

# salary_statistics('JavaScript')
# language_statistics(2019)
# predict_salary('JavaScript')

CUI()
0