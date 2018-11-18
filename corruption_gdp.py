#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:19:33 2018

@author: sigita
"""

import pandas as pd
import matplotlib.pyplot as plt
import json
from pprint import pprint


path = "/home/sigita/Dropbox/LearnProgramming/transparency_international/dataset.json"

with open(path) as f:
    data = json.load(f)

pprint(data)

header = data["elements"][1]["data"][0][0]
datavalues = data["elements"][1]["data"][0][1:]

df = pd.DataFrame(data = dataset, columns = header)

#Test
X = df.iloc[:, 1:8].values
denmark = X[1,1:]
years = ["2017", "2016", "2015", "2014", "2013", "2012"]
var = []

