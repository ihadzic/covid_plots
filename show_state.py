#!/usr/bin/env python3
import requests
import sys
import numpy
from matplotlib import pyplot

mva_len = 7

if len(sys.argv) <= 1:
    state="nj"
else:
    state=sys.argv[1]
url="https://covidtracking.com/api/v1/states/" + state + "/daily.json"
r=requests.get(url)
if r.status_code == 200:
    daily=r.json()
    raw_positives=[ p.get("positive") for p in daily ]
    positives = [ p if p is not None else 0 for p in raw_positives ]
    positives.append(0)
    positives.reverse()
    new_positives_raw = [ x - y for (x,y) in zip(positives[1:], positives[0:-1]) ]
    new_positives = [ x if x > 0 else 0 for x in new_positives_raw ]
    # moving average: implement as convolution with filters impulse
    # response and drop the tail of last mva_len elements
    new_positives_mva = numpy.convolve(new_positives, [1/mva_len]*mva_len)
    new_positives_mva = new_positives_mva[:-mva_len+1]
    pyplot.plot(new_positives, linewidth=1, color='black')
    pyplot.plot(new_positives_mva, linewidth=2, color='red')
    pyplot.xlabel('days')
    pyplot.ylabel('cases')
    pyplot.grid()
    pyplot.show()
else:
    print("API request failed {}".format(r.status_code))
