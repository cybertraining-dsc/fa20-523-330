#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:33:58 2020

@author: tobi
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt


olist_customers = pd.read_csv('dataset/olist_customers_dataset.csv')
olist_customers.head(5)

olist_orders = pd.read_csv('dataset/olist_orders_dataset.csv')
olist_orders.head(5)

olist_sellers = pd.read_csv('dataset/olist_sellers_dataset.csv')
olist_sellers.head(5)

olist_products = pd.read_csv('dataset/olist_products_dataset.csv')
olist_products.head(5)

olist_payments = pd.read_csv('dataset/olist_order_payments_dataset.csv')
olist_payments.head(5)

olist_reviews = pd.read_csv('dataset/olist_order_reviews_dataset.csv')
olist_reviews.head(5)

olist_items = pd.read_csv('dataset/olist_order_items_dataset.csv')
olist_items.head(5)

df = olist_customers
df = df.merge(olist_orders, on ='customer_id',how='left')
df = df.merge(olist_items, on ='order_id',how='left')
df = df.merge(olist_products,on ='product_id',how='left')
df.isna().sum()

plt.figure(98,figsize=(20,10))

sns.heatmap(df.isna(), cmap="viridis")

city_orders = pd.DataFrame(df.groupby(['customer_city'])['product_category_name'].count())
plt.figure(99)
plt.hist(df['customer_state'])
state_sales = pd.DataFrame(df.groupby(['customer_state'])['customer_state'].count())
