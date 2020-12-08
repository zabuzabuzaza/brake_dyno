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

# if checking logging input from serial
PRINT_SERIAL_IN = False

class Model():
    def __init__(self):
        """
        For keeping track of all information of the GUI.
        """
        # constants
        self.DEFAULT_TEST_DURATION = 200
        self.PLOT_WINDOW = 100

        self.testDuration = self.DEFAULT_TEST_DURATION
        self.data_titles = [["Seconds", "X_Data", "Y Data", "Thermocouple 1", "Thermocouple 2", "Motor Speed", "Brake Pressure"]]
        self.dataSet = self.data_titles.copy()
        self.moduleSet = self.data_titles.copy()
        self.plotSets = {}

        # default settings 
        self.defaultParameters = {
            'testSchedule': "Constant Speed", 
            'testParams': ["X-Stick", "Y-Stick", "RotorT", "Caliper Temp", "Motor"], 
            'COMPort': "COM3", 
            'COMStatus': "Click Apply to check Status", 
            'fileName': util.getDate(), 
        }
        # self.defaultParameters = {
        #     'testSchedule': "Constant Speed", 
        #     'testParams': ["RotorT", "Caliper Temp", "Motor"], 
        #     'COMPort': "COM3", 
        #     'COMStatus': "Click Apply to check Status", 
        #     'fileName': util.getDate(), 
        # }

        # stores settings 
        self.testParameters = dict(self.defaultParameters)

        # temporarily stores settings that will either be applied or cancelled
        self.tempParameters = dict(self.testParameters)

    def getSerialData(self, serial, count):
        """Reads the incoming data from the serial port and adds it to this
        object's data structure.
        Parameters
        ----------
        serial : (py)serial obj
            The serial from which to read / write from.
        """

        ser_line = serial.readline()[:-1].decode("utf-8")
        serial_data = [count] + ser_line.split(',')

        return serial_data
    
    def append_data(self, data_list): 
        """Add a list of data for a given time step to the full data set. 

        Parameters
        ----------
        data_list : [floats]
            list of inputs for a given time. 
        """

        float_data = []
        for element in data_list: 
            try: 
                float_data.append(float(element))
            except ValueError: 
                float_data.append(0)

        self.dataSet.append(float_data)
        self.moduleSet.append(float_data)

        


    def createCanvas(self, key):
        """Creates a plot for a given parameter (indicated by the key). 

        Parameters
        ----------
        key : string
            to reference the plot object stored in a dict. 

        Returns
        -------
        PlotGraphics obj
            plot with no line
        """
        self.plotSets[key] = [np.array(np.zeros(self.PLOT_WINDOW))] * 3

        line_x = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][1])))
        line_y = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][2])))

        return wxplot.PlotGraphics([line_x, line_y], title="Title")

    def plot1(self, key, t_new, x_new):
        """Plots a line for one data point for a given time. 

        Parameters
        ----------
        key : str
            reference to the plot to plot on. 
        t_new : float
            time point
        x_new : float
            data point

        Returns
        -------
        PlotGraphics obj
            plot object with updated plot line
        """
        self.plotSets[key][0] = np.append(self.plotSets[key][0][1:], t_new)
        self.plotSets[key][1] = np.append(self.plotSets[key][1][1:], x_new)
        
        line_x = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][1])), colour="red", width=5)

        return wxplot.PlotGraphics([line_x])
    
    def plot2(self, key, t_new, x_new, y_new):
        """NOT USED, DELETE EVENTUALLY
        """
        self.plotSets[key][0] = np.append(self.plotSets[key][0][1:], t_new)
        self.plotSets[key][1] = np.append(self.plotSets[key][1][1:], x_new)
        self.plotSets[key][2] = np.append(self.plotSets[key][2][1:], y_new)
        
        line_x = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][1])), colour="red")
        line_y = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][2])), colour="green")
        
        return wxplot.PlotGraphics([line_x, line_y])

    def debugTestSettings(self):
        print(f"Temporary Duration: {self.tempParameters['testDuration']}")
        print(f"Actual Duration: {self.testDuration}")




