#!/usr/bin/env python3
import requests
import sys
import numpy

mva_len = 7

if len(sys.argv) <= 1:
    state="nj"
else:
    state=sys.argv[1]
url="https://covidtracking.com/api/v1/states/" + state + "/daily.json"
r=requests.get(url)
if r.status_code == 200:
    daily=r.json()
    positives=[ p.get("positive") for p in daily ]
    positives.append(0)
    positives.reverse()
    new_positives = [ x - y for (x,y) in zip(positives[1:], positives[0:-1]) ]
    # moving average: implement as convolution with filters impulse
    # response and drop the tail of last mva_len elements
    new_positives_mva = numpy.convolve(new_positives, [1/mva_len]*mva_len)
    new_positives_mva = new_positives_mva[:-mva_len+1]
    print(len(new_positives))
    print(len(new_positives_mva))
else:
    print("API request failed {}".format(r.status_code))
