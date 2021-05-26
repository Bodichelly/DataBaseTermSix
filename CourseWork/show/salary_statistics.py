import plotly.express as px
import pandas as pd

from operator import itemgetter
from DB_utils.mongodb import mongo_manager
from data_analysis_utils.data_manage_utils import get_data_frame, get_essential_columns_names


def sum_up_data_frame(data_frame, year):
    tmp_array = []
    for position in data_frame['position'].unique():
        position_data = data_frame[data_frame['position'] == position]
        median = position_data['salary'].mean()
        tmp_array.append({
            'position': position,
            'salary': median,
            'year': year
        })
    return pd.DataFrame(tmp_array)


def salary_statistics(language: str):
    data_arr = mongo_manager.find_all({'language': language})
    # data_arr = sorted(data_arr, key=itemgetter('year'))
    variables = get_essential_columns_names()
    long_df = pd.DataFrame([i for i in data_arr], columns=variables).sort_values(by = 'year')
    years = long_df['year'].unique()
    new_df = []
    for y in years:
        data_of_year = sum_up_data_frame(long_df[long_df['year'] == y], y)
        new_df.append(data_of_year)
    result = pd.concat(new_df)

    # print(result)
    # fig = px.scatter(result, x="year", y="salary", color="position", title=language.upper())
    # fig.show()
    fig = px.line(result, x="year", y="salary", color="position",
                  line_group="position", title=language.upper())
    fig.show()

    # fig = px.bar(long_df, x="year", y="salary", color="position", title=language.upper())
    # fig.show()
