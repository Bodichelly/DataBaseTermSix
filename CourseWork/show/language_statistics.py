import plotly.express as px
import pandas as pd

from operator import itemgetter
from DB_utils.mongodb import mongo_manager
from data_analysis_utils.data_manage_utils import get_data_frame, get_essential_columns_names


def language_statistics(year: int):
    data_arr = mongo_manager.find_all({'year': str(year), 'language': {'$ne': 'NaN'}})
    # data_arr = sorted(data_arr, key=itemgetter('year'))
    variables = get_essential_columns_names()
    long_df = pd.DataFrame([i for i in data_arr], columns=variables)
    long_df = long_df.dropna(axis=0, subset=['language'])
    count = []
    languages = long_df['language'].unique()
    for lang in languages:
        count.append(len(long_df[long_df['language'] == lang].index))

    fig = px.pie(values=count, names=languages, title="Most popular programing languages in " + str(year))
    fig.show()
