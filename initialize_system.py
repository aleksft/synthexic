import os
import pandas as pd

from pymongo import MongoClient

"""This script initializes the data in the database"""


class Settings(object):
    DB_TYPE = 'mongo'
    DB_NAME = 'test_database'
    WEIGHT_TB = 'weights'
    DB_MONG_CONN = 'mongodb://localhost:27017'


def initialize_ddbb(weights):
    client = MongoClient(Settings.DB_MONG_CONN)
    db = client[Settings.DB_NAME]
    dataset = db[Settings.WEIGHT_TB]
    for data_index in xrange(weights.size):
        index = data_index + 1
        weight = weights.iloc[data_index]
        weight_dict = {'_id': index, 'weight': weight}
        dataset.insert_one(weight_dict)


def get_weights():
    data_file = os.getcwd() + '/Data.xlsx'
    xls_data = pd.read_excel(io=data_file, sheetname=0, index_col=None)
    weights_data = xls_data.ix[0, 1:]
    return weights_data


weights = get_weights()
initialize_ddbb(weights)
