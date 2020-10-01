# -*- coding: utf-8 -*-
"""
Utilities script for various functions.
"""
import os
import csv
import serial
import re
from datetime import datetime

class Arduino():
    def __init__(self, port='COM3'):
        """
        Initialises the serial connection for communication between Arduino
        & computer.

        Parameters
        ----------
        port : string, optional
            The port used by the Arduino. Can be checked from the Arduino IDE
            or the Device Manager.
            The default is 'COM3'.
        """
        try:
            self.ser = serial.Serial(port)
            self.ser.flushInput()
        except serial.SerialException as e:
            pass
            # print("No device detected in Serial Port")
            # self.ser = serial.Serial(port)
            # self.ser.flushInput()

def getDate(): 
    return str(datetime.now().strftime("%b %d %H-%M"))

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
    # check for duplicates: 
    fileRegex = re.compile(r"\(\d\)\.csv$")
    while os.path.exists(filename): 
        matchObj = fileRegex.search(filename)
        if matchObj == None: 
            filename = filename[:-4] + "(1).csv"
        else: 
            filename = f"data({int(matchObj.group()[1]) + 1}).csv" 

    # write to csv file
    with open(filename, 'w', newline='') as csv_file:
        wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        wr.writerows(data_list)

    # keep this for now for testing and debugging
    print(f"csv file updated to {filename}")

def extractValues(data_list):
    time_values = []
    x_values = []
    del data_list[0]
    for entry in data_list:
        time_values.append(entry[0])
        x_values.append(entry[0])

    return time_values, x_values

