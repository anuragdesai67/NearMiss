# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:15:42 2020

@author: anurag
"""

import pandas as pd


#global variables
global ALL_ACCIDENTS_FILENAME
ALL_ACCIDENTS_FILENAME = 'C:/Users/anurag/Desktop/Github_Repos/NearMiss/data/Accidents.csv'

#read csv file into a pandas dataframe
def read_data(filename):
    '''
    param filename: full path to csv file
    type  filename: string
    return pandas dataframe
    '''
    with open(filename, encoding="utf-8-sig") as f:
        data = pd.read_csv(f)
        f.close()
    return data

if __name__ == '__main__':
    df_all_accidents = read_data(ALL_ACCIDENTS_FILENAME)
    print(len(df_all_accidents))