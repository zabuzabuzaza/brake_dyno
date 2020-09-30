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

class Model():
    def __init__(self):
        """
        For keeping track of all information of the GUI.
        """
        # constants
        self.DEFAULT_TEST_DURATION = 20
        self.PLOT_WINDOW = 40

        self.DEFAULT_SCHEDULE = "Joystick"
        self.DEFAULT_PARAMS = ["X-Stick", "Y-Stick"]
        self.DEFAULT_COM_NAME = "COM3"
        self.DEFAULT_COM_STATUS = "Click Apply to check Status" 
        self.DEFAULT_FILE_NAME = util.getDate() + ".csv"

        self.testDuration = self.DEFAULT_TEST_DURATION
        self.dataSet = [["Seconds", "X_Data", "Y Data"]]

        # self.testSchedule = self.DEFAULT_SCHEDULE
        # self.testParams = self.DEFAULT_PARAMS
        # self.COMName = self.DEFAULT_COM_NAME
        # self.COMStatus = self.DEFAULT_COM_STATUS
        # self.fileName = self.DEFAULT_FILE_NAME

        # default settings 
        self.defaultParameters = {
            'testSchedule': self.DEFAULT_SCHEDULE, 
            'testParams': self.DEFAULT_PARAMS, 
            'COMPort': self.DEFAULT_COM_NAME, 
            'COMStatus': self.DEFAULT_COM_STATUS, 
            'fileName': self.DEFAULT_FILE_NAME, 
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
    

    # def applyTestSettings(self, event):
    #     self.testDuration = self.tempParameters['testDuration']

    # def cancelTestSettings(self, event):
    #     self.tempParameters['testDuration'] = self.DEFAULT_TEST_DURATION

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
        print(data)

        self.dataSet.append(data)

        try:
            int_x, int_y = int(data_x), int(data_y)
        except ValueError:
            int_x, int_y = 0

        return int_x, int_y


    # def createCanvas(self, panel):
    #     #self.y_var = np.array(np.zeros([self.PLOT_WINDOW]))
    #     #self.x_var = np.array(np.zeros([self.PLOT_WINDOW]))
    #     #plt.ion()
    #     self.y_var = np.array(np.zeros([self.PLOT_WINDOW]))
    #     self.x_var = np.array(np.zeros([self.PLOT_WINDOW]))
    #     self.fig, self.axs = plt.subplots(nrows=2)

    #     self.fig.set_size_inches(10, 5)
    #     self.yline, = self.axs[0].plot(self.y_var)
    #     self.xline, = self.axs[1].plot(self.x_var)

    #     #self.canvas = FigureCanvas(panel, -1, self.fig)

    # def plotter(self, x_new, y_new, frame):
    #     self.y_var = np.append(self.y_var, y_new)
    #     self.y_var = self.y_var[1:(self.PLOT_WINDOW + 1)]

    #     self.x_var = np.append(self.x_var, x_new)
    #     self.x_var = self.x_var[1:(self.PLOT_WINDOW + 1)]

    #     self.yline.set_ydata(self.y_var)
    #     self.xline.set_ydata(self.x_var)

    #     self.axs[0].relim()
    #     self.axs[1].relim()
    #     self.axs[0].autoscale_view()
    #     self.axs[1].autoscale_view()

    #     self.fig.canvas.draw()
    #     self.fig.canvas.flush_events()


    def debugTestSettings(self):
        print(f"Temporary Duration: {self.tempParameters['testDuration']}")
        print(f"Actual Duration: {self.testDuration}")




