#!/usr/bin/env python3
import requests
import sys
import numpy
from matplotlib import pyplot

mva_len = 7

if len(sys.argv) <= 2:
    print("need at least two states")
    exit(1)
else:
    states = sys.argv[1:]
lstates = []
for state in states:
    url="https://covidtracking.com/api/v1/states/" + state + "/daily.json"
    r= requests.get(url)
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
        pyplot.plot(new_positives_mva, linewidth=2)
        lstates.append(state)
    else:
        print("state {} skipped (API request failed)".format(state))
pyplot.legend(lstates)
pyplot.xlabel('days')
pyplot.ylabel('cases')
pyplot.grid()
pyplot.show()
