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
max_len = 0
all_positives = []
# first pass, store data locally and determine the longest data set
for state in states:
    url="https://covidtracking.com/api/v1/states/" + state + "/daily.json"
    r= requests.get(url)
    if r.status_code == 200:
        daily=r.json()
        raw_positives=[ p.get("positive") for p in daily ]
        positives = [ p if p is not None else 0 for p in raw_positives ]
        if len(positives) > max_len:
            max_len = len(positives)
        all_positives.append(positives)
        lstates.append(state)
    else:
        print("state {} skipped (API request failed)".format(state))

# second pass, pad datasets to be aligned to the latest day
for positives in all_positives:
    padded_positives = positives + [ 0 ] * (1 + max_len - len(positives))
    padded_positives.reverse()
    new_positives_raw = [ x - y for (x,y) in zip(padded_positives[1:],
                                                 padded_positives[0:-1]) ]
    new_positives = [ x if x > 0 else 0 for x in new_positives_raw ]
    # moving average: implement as convolution with filters impulse
    # response and drop the tail of last mva_len elements
    new_positives_mva = numpy.convolve(new_positives, [1/mva_len]*mva_len)
    new_positives_mva = new_positives_mva[:-mva_len+1]
    pyplot.plot(new_positives_mva, linewidth=2)

pyplot.legend(lstates)
pyplot.xlabel('days')
pyplot.ylabel('cases')
pyplot.grid()
pyplot.show()
