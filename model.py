# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:10:48 2020

@author: iamde
"""

# import matplotlib
# matplotlib.use('WXAgg')
# from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# import matplotlib.pyplot as plt
# import numpy as np

import util
import wx.lib.plot as wxplot
import numpy as np
import struct

import time

class Model():
    def __init__(self):
        """
        For keeping track of all information of the GUI.
        """
        # constants
        self.DEFAULT_TEST_DURATION = 200
        self.PLOT_WINDOW = 100
        # self.scheduleList = {
        #     "Joystick": 50, 
        #     "Schedule A": 20, 
        #     "Schedule B": 40, 
        #     "Schedule C": 60, 
        # }
        self.ALL_PARAMETERS = [
            "Pressure", 
            "X-Stick", 
            "Y-Stick", 
            "RotorT", 
            "CaliperT", 
            "Motor", 
        ]

        self.testDuration = self.DEFAULT_TEST_DURATION
        self.data_titles = [["Seconds", "X_Data", "Y Data", "Thermocouple 1", "Thermocouple 2", "Motor Speed", "Brake Pressure"]]
        self.dataSet = self.data_titles.copy()
        self.moduleSet = self.data_titles.copy()
        self.plotSets = {}

        # default settings 
        self.defaultParameters = {
            'testSchedule': "Joystick", 
            'testParams': ["X-Stick", "Y-Stick", "RotorT", "Motor"], 
            'COMPort': "COM3", 
            'COMStatus': "Click Apply to check Status", 
            'fileName': util.getDate(), 
        }

        # stores settings 
        self.testParameters = dict(self.defaultParameters)

        # temporarily stores settings that will either be applied or cancelled
        self.tempParameters = dict(self.testParameters)

    def getSerialData(self, serial, count):
        """
        Reads the incoming data from the serial port and adds it to this
        object's data structure.
        Parameters
        ----------
        serial : (py)serial obj
            The serial from which to read / write from.
        """

        ser_line = serial.readline()[:-1].decode("utf-8")

        serial_data = [count] + ser_line.split(',')
        #print(serial_data)
        

        # for element in serial_data: 
        #     try: 
        #         float_data.append(float(element))
        #     except ValueError: 
        #         float_data.append(0)

        # self.dataSet.append(float_data)

        return serial_data
    
    def append_data(self, data_list): 

        float_data = []
        for element in data_list: 
            try: 
                float_data.append(float(element))
            except ValueError: 
                float_data.append(0)

        self.dataSet.append(float_data)
        self.moduleSet.append(float_data)

        


    def createCanvas(self, key):
        self.plotSets[key] = [np.array(np.zeros(self.PLOT_WINDOW))] * 3

        line_x = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][1])))
        line_y = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][2])))

        return wxplot.PlotGraphics([line_x, line_y], title="Title")

    def plot1(self, key, t_new, x_new):
        self.plotSets[key][0] = np.append(self.plotSets[key][0][1:], t_new)
        self.plotSets[key][1] = np.append(self.plotSets[key][1][1:], x_new)
        
        line_x = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][1])), colour="red", width=5)

        return wxplot.PlotGraphics([line_x])
    
    def plot2(self, key, t_new, x_new, y_new):
        self.plotSets[key][0] = np.append(self.plotSets[key][0][1:], t_new)
        self.plotSets[key][1] = np.append(self.plotSets[key][1][1:], x_new)
        self.plotSets[key][2] = np.append(self.plotSets[key][2][1:], y_new)
        
        line_x = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][1])), colour="red")
        line_y = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][2])), colour="green")
        
        return wxplot.PlotGraphics([line_x, line_y])

    def debugTestSettings(self):
        print(f"Temporary Duration: {self.tempParameters['testDuration']}")
        print(f"Actual Duration: {self.testDuration}")




