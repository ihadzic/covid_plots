#!/usr/bin/env python3
import argparse
import utils
from matplotlib import pyplot

mva_len = 7

parser = argparse.ArgumentParser(description="Show COVID trend for a state")
parser.add_argument("state", type=str, nargs="?", default="nj", help="state to analyze")
args=parser.parse_args()
daily = utils.get_daily_data_for_state(args.state)
if daily is not None:
    raw_positives=[ p.get("positive") for p in daily ]
    positives = [ p if p is not None else 0 for p in raw_positives ]
    positives.append(0)
    positives.reverse()
    new_positives, new_positives_mva = utils.process_positives(positives, mva_len)
    pyplot.plot(new_positives, linewidth=1, color='black')
    pyplot.plot(new_positives_mva, linewidth=2, color='red')
    pyplot.xlabel('days')
    pyplot.ylabel('cases')
    pyplot.grid()
    pyplot.show()
