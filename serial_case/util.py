# -*- coding: utf-8 -*-
"""
Utilities script for various functions. 
"""
import csv 

def data2csv(data_list, filename='data.csv'): 
    with open(filename, 'w', newline='') as csv_file: 
            wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            wr.writerow(data_list)  
<<<<<<< HEAD
    
    print("csv file updated")
=======
>>>>>>> 18f9e3c37e809017f20be9fd5dd79fd71ab51d9e

