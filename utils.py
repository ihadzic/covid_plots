#!/usr/bin/env python3

import numpy
import requests

def process_positives(positives, mva_len):
    """
    remove outliers and obvious errors from raw data
    and calculate the moving average, return cleaned-up
    raw data and moving average
    """
    new_positives_raw = [ x - y for (x,y) in zip(positives[1:],
                                                 positives[0:-1]) ]
    new_positives = [ x if x > 0 else 0 for x in new_positives_raw ]
    # moving average: implement as convolution with filters impulse
    # response and drop the tail of last mva_len elements
    new_positives_mva = numpy.convolve(new_positives, [1/mva_len]*mva_len)
    new_positives_mva = new_positives_mva[:-mva_len+1]
    return new_positives, new_positives_mva

def get_daily_data_for_state(state):
    """
    retrieve data for state, return JSON if data were successfully
    retrieved, return None in case of an error
    """
    url="https://covidtracking.com/api/v1/states/" + state + "/daily.json"
    r=requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        print("API request failed {}".format(r.status_code))
        return None
