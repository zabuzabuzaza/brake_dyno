# -*- coding: utf-8 -*-
"""
Utilities script for various functions.
"""
import csv

def data2csv(data_list, filename='data.csv'):
    """
    Takes a data structure and saves its contents to a csv file. If one
    already exists with the same given name, it will be overwritten.

    Parameters
    ----------
    data_list : list
        list of data to be put into a csv file.
    filename : string, optional
        Optional name for the output csv file. The default is 'data.csv'.
        Will want to implement the current date into the default filename to
        avoid unwanted file overrides.
    """
    with open(filename, 'w', newline='') as csv_file:
            wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            wr.writerows(data_list)

    # keep this for now for testing and debugging
    print("csv file updated")

def extractValues(data_list):
    time_values = []
    x_values = []
    del data_list[0]
    for entry in data_list:
        time_values.append(entry[0])
        x_values.append(entry[0])

    return time_values, x_values

