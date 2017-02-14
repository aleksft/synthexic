import os
import time
import json
import requests
import pandas as pd

from flask import json

"""This script simulates the entry of the data in the system"""

url = 'http://localhost:5000/api/v1/prices'
headers = {'Content-Type': 'application/json'}


def get_prices():
    data_file = os.getcwd() + '/Data.xlsx'
    xls_data = pd.read_excel(io=data_file, sheetname=0, index_col=None)
    prices_data = xls_data.ix[1:, 1:]
    return prices_data


def simulation():
    start_time = time.time()
    prices = get_prices()
    process_time = time.time()
    for row in xrange(prices.shape[0]):
        day = row + 1
        price_row = prices.iloc[row]
        block_dict = {'day': day}
        for price_index in xrange(price_row.size):
            index = price_index + 1
            index_val = 'index_' + str(index)
            block_dict[index_val] = price_row.iloc[price_index]
        response = requests.post(url, json=block_dict)
        error = False
        if response.status_code != 200:
            error = True
            print "ERROR in connection for day " + str(day)
        elif not json.loads(response.text)['response']:
            error = True
            print "ERROR saving data day " + str(day)
        if error:
            break
    end_time = time.time()
    print "END processing data"
    print "Complete time: " + str(end_time - start_time)
    print "Process time: " + str(end_time - process_time)


simulation()
