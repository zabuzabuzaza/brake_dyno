# -*- coding: utf-8 -*-
"""
Utilities script for various functions.
"""
import os
import csv
import serial

from datetime import datetime

# probably wont need
import re

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
    """Returns data in Mont DD HH-MM format. 

    Returns
    -------
    data : str
    """
    return str(datetime.now().strftime("%b %d %H-%M"))

def data2csv(data_list, module=None, temp=None, pressure=None, foldername='data'):
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
    # folderRegex = re.compile(r"\(\d\)$")
    # while os.path.exists(foldername): 
    #     matchObj = folderRegex.search(foldername)
    #     if matchObj == None: 
    #         foldername = foldername[:-4] + "(1)"
    #     else: 
    #         foldername = f"data({int(matchObj.group()[1]) + 1})" 

    try: 
        os.mkdir(foldername)
    except FileExistsError: 
        pass 

    if module == None: 
        filename = "fulltestrun.csv"
    else: 
        filename = f"{module}_t({temp})_p({pressure})" + ".csv"
    filename = os.path.join(foldername, filename)

    


    # write to csv file
    with open(filename, 'w', newline='') as csv_file:
        wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        wr.writerows(data_list)

    # keep this for now for testing and debugging
    print(f"csv file updated to {filename}")

