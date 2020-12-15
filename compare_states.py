#!/usr/bin/env python3
import requests
import argparse
import utils
from matplotlib import pyplot

mva_len = 7

parser = argparse.ArgumentParser(description="Compare COVID trends for two or more states")
parser.add_argument("state1", metavar="state", type=str, nargs=1, help="first state")
parser.add_argument("state2", metavar="state", type=str, nargs="+", help="additional state(s)")
args=parser.parse_args()
args.states = args.state1 + args.state2

lstates = []
max_len = 0
all_positives = []
# first pass, store data locally and determine the longest data set
for state in args.states:
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
    _, new_positives_mva = utils.process_positives(padded_positives, mva_len)
    pyplot.plot(new_positives_mva, linewidth=2)

pyplot.legend(lstates)
pyplot.xlabel('days')
pyplot.ylabel('cases')
pyplot.grid()
pyplot.show()
