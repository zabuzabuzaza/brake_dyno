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
            "X-Stick", 
            "Y-Stick", 
            "Rotor", 
            "Caliper", 
            "MotorT", 
        ]

        self.testDuration = self.DEFAULT_TEST_DURATION
        self.dataSet = [["Seconds", "X_Data", "Y Data", "Input3", "Input4", "Input5"]]
        self.plotSets = {}

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

    # def setTestDuration(self, schedule_name):
    #     """
    #     Event handler for Text Entry to Test Length.

    #     Parameters
    #     ----------
    #     event : event obj
    #         The textEntry object from which to get the entered text.
    #     """
        
    #     if schedule_name == self.scheduleList[0]: 
    #         self.testDuration = 50
    #     elif schedule_name == self.scheduleList[1]: 
    #         self.testDuration = 20
    #     elif schedule_name == self.scheduleList[2]: 
    #         self.testDuration = 40
    #     elif schedule_name == self.scheduleList[3]: 
    #         self.testDuration = 60
    #     else: 
    #         # should not happen
    #         self.testDuration = 5

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
        print(ser_line)

        serial_data = [count] + ser_line.split(',')
        print(serial_data)
        float_data = []

        for element in serial_data: 
            try: 
                float_data.append(float(element))
            except ValueError: 
                float_data.append(0)


        self.dataSet.append(float_data)

        # print(data)

        # serial.write(bytearray(struct.pack("f", out)))
        # print(bytearray(struct.pack("f", out)))
        # serial.write(str.encode(str(data[1])))

        return tuple(serial_data)

    def createCanvas(self, key):
        self.plotSets[key] = [np.array(np.zeros(self.PLOT_WINDOW))] * 3

        line_x = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][1])))
        line_y = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][2])))

        return wxplot.PlotGraphics([line_x, line_y], title="Title")

    def plot1(self, key, t_new, x_new):
        self.plotSets[key][0] = np.append(self.plotSets[key][0][1:], t_new)
        self.plotSets[key][1] = np.append(self.plotSets[key][1][1:], x_new)
        
        line_x = wxplot.PolyLine(list(zip(self.plotSets[key][0], self.plotSets[key][1])))

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




