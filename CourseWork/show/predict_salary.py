import csv
import os
import json
import plotly.express as px
import pandas as pd
import numpy as np
from operator import itemgetter
from DB_utils.mongodb import mongo_manager
from data_analysis_utils.data_manage_utils import get_data_frame, get_essential_columns_names
from scipy import stats
from scipy.special import logsumexp


def predict(salaries, counts):
    if len(counts) == 1 or np.array_equal(counts, [1, 1]):
        return salaries[-1]
    else:
        slope, intercept, r, p, std_err = stats.linregress(counts, salaries)
        if not slope or not intercept:
            return salaries[-1]
        return int(slope * counts[-1] + intercept)


def sum_up_data_frame(data_frame):
    counts = []
    salaries = []
    for year in data_frame['year'].unique():
        year_data = data_frame[data_frame['year'] == year]
        median = year_data['salary'].mean()
        count = year_data['salary'].count()
        counts.append(count)
        salaries.append(int(median))
    return predict(salaries, counts)


def predict_salary(language: str):
    data_arr = mongo_manager.find_all({'language': language})
    variables = get_essential_columns_names()
    long_df = pd.DataFrame([i for i in data_arr], columns=variables).sort_values(by='year')
    positions = long_df['position'].unique()

    predictions = []

    for pos in positions:
        prediction = {}
        salary = sum_up_data_frame(long_df[long_df['position'] == pos])
        prediction['position'] = pos
        prediction['salary'] = salary
        predictions.append(prediction)

    save_path = './show/predictions'
    file_name = language + "_prediction.csv"
    complete_name = os.path.join(save_path, file_name)
    keys = predictions[0].keys()
    with open(os.path.abspath(complete_name), 'a', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(predictions)
        return
