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

df = pd.DataFrame(data = datavalues, columns = header)

#Test plot
X = df.iloc[:, 1:8].values

years = [2012, 2013, 2014, 2015, 2016, 2017]

denmark = list(map(int, X[1,1:]))
denmark.reverse()

estonia = list(map(int, X[20,1:]))
estonia.reverse()

latvia = list(map(int, X[39,1:]))
latvia.reverse()

lithuania = list(map(int, X[38,1:]))
lithuania.reverse()

 
# Plot the change in PCI in 4 countries
plt.plot( years, denmark, marker='o', markerfacecolor='olive', markersize=8, color='skyblue', linewidth=3, label="Denmark")
plt.plot( years, latvia, marker='', color='red', linewidth=2, linestyle='dashed', label="Latvia")
plt.plot( years, lithuania, marker='', color='yellow', linewidth=2, linestyle='dashed', label="Lithuania")
plt.plot( years, estonia, marker='', color='blue', linewidth=2, linestyle='dashed', label="Estonia")
plt.legend()
