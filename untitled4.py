# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 17:32:59 2020

@author: ashu0
"""

import pandas as pd
from glob import glob

filenames = glob(r'C:\Users\ashu0\OneDrive\Desktop\Ok\Modeling\*.csv')
dataframes = [pd.read_csv(f) for f in filenames]

df_dist_ware=dataframes[0]
df_sales=dataframes[1]
df_SKU_Sales=dataframes[2]
df4_warehouse_address=dataframes[3]

df_connect_1=pd.merge(df_dist_ware,df_SKU_Sales,how='left',left_on=['Sale #','Item #'],right_on=['Sale ID','SKU'])

df_connect_2=pd.merge(df_connect_1,df_sales,how='left',left_on=['Sale #'],right_on=['Sale #'])                                    

df_connect_3=pd.merge(df_connect_2,df4_warehouse_address, how='left',left_on=['Warehouses'],right_on=['Warehouses'])      

#An Example in allocation
df_connect_3['Dist-Warehouse Level Price']=df_connect_3['Qty_x']*df_connect_3['Per Unit Price']




    

