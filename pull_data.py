#!/usr/bin/env python3
import requests

state="nj"
url="https://covidtracking.com/api/v1/states/" + state + "/daily.json"
r=requests.get(url)
if r.status_code == 200:
    daily=r.json()
    positives=[ p.get("positive") for p in daily ]
positives.reverse()
print(positives)
