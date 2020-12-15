#!/usr/bin/env python3

import numpy

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
