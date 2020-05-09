#!/usr/bin/env python3
import requests
import sys

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
print(new_positives)
