# -*- coding: utf-8 -*-
"""
Utilities script for various functions. 
"""
import csv 

def data2csv(data_list, filename='data.csv'): 
    with open(filename, 'w', newline='') as csv_file: 
            wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            wr.writerow(data_list)  

