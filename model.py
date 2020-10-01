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

class Model():
    def __init__(self):
        """
        For keeping track of all information of the GUI.
        """
        # constants
        self.DEFAULT_TEST_DURATION = 20
        self.PLOT_WINDOW = 100
        self.ALL_PARAMETERS = [
            "X-Stick", 
            "Y-Stick", 
            "Rotor", 
            "Caliper", 
            "MotorT", 
        ]

        self.testDuration = self.DEFAULT_TEST_DURATION
        self.dataSet = [["Seconds", "X_Data", "Y Data"]]

        # default settings 
        self.defaultParameters = {
            'testSchedule': "Joystick", 
            'testParams': ["X-Stick", "Y-Stick"], 
            'COMPort': "COM3", 
            'COMStatus': "Click Apply to check Status", 
            'fileName': util.getDate() + ".csv", 
        }

        # stores settings 
        self.testParameters = dict(self.defaultParameters)

        # temporarily stores settings that will either be applied or cancelled
        self.tempParameters = dict(self.testParameters)

        # self.variables = {"testLength": 10}
        # self.interactables = {}

    def getTestDuration(self, event):
        """
        Event handler for Text Entry to Test Length.

        Parameters
        ----------
        event : event obj
            The textEntry object from which to get the entered text.
        """
        try:
            self.tempParameters['testDuration'] = int(event.GetEventObject().GetLineText(0))
        except ValueError:
            self.tempParameters['testDuration'] = 0

    def getSerialData(self, serial, count):
        """
        Reads the incoming data from the serial port and adds it to this
        object's data structure.
        Parameters
        ----------
        serial : (py)serial obj
            The serial from which to read / write from.
        """
        ser_bytes = serial.readline()[:-1].decode("utf-8")

        # need to implement multiple data recordings
        try:
            data_x, data_y = ser_bytes.split(',')
        except (IndexError, ValueError):
            data_x = -1
            data_y = -1

        data = [count, data_x, data_y]

        # keep for now until a live plot is implemented
        # print(data)

        self.dataSet.append(data)

        try:
            int_x, int_y = int(data_x), int(data_y)
        except ValueError:
            int_x, int_y = 0

        return int_x, int_y

    def createCanvas(self):
        self.t_var = np.array(np.zeros(self.PLOT_WINDOW))
        self.x_var = np.array(np.zeros(self.PLOT_WINDOW))
        self.y_var = np.array(np.zeros(self.PLOT_WINDOW))

        line_x = wxplot.PolyLine(list(zip(self.t_var, self.x_var)))
        line_y = wxplot.PolyLine(list(zip(self.t_var, self.y_var)))
        return wxplot.PlotGraphics([line_x, line_y], title="Title")

    def plotter(self, t_new, x_new, y_new):
        self.t_var = np.append(self.t_var[1:], t_new)
        self.x_var = np.append(self.x_var[1:], x_new)
        self.y_var = np.append(self.y_var[1:], y_new)

        line_x = wxplot.PolyLine(list(zip(self.t_var, self.x_var)), colour="red")
        line_y = wxplot.PolyLine(list(zip(self.t_var, self.y_var)), colour="green")
    
        return wxplot.PlotGraphics([line_x, line_y])


    def debugTestSettings(self):
        print(f"Temporary Duration: {self.tempParameters['testDuration']}")
        print(f"Actual Duration: {self.testDuration}")




