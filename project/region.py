#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:33:58 2020

@author: tobi
"""
##conda install -c conda-forge folium
##pip install selenium

import pandas as pd
df = pd.read_csv('olist_customers_dataset.csv')
hist = df.hist
