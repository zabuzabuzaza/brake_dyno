# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:10:48 2020

@author: iamde
"""

# from arduino import Arduino
# import util

import matplotlib

import matplotlib.pyplot as plt
import numpy as np


class Model():
    def __init__(self):
        """
        For keeping track of all information of the GUI.
        """
        self.DEFAULT_TEST_DURATION = 5
        self.PLOT_WINDOW = 40

        self.testDuration = self.DEFAULT_TEST_DURATION
        self.dataSet = [["Seconds", "X_Data", "Y Data"]]

        self.y_var = np.array(np.zeros([self.PLOT_WINDOW]))
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(self.y_var)

        # temporarily stores settings that will either be applied or cancelled
        self.testParameters = {}


        self.variables = {"testLength": 10}
        self.interactables = {}

    def getTestDuration(self, event):
        """
        Event handler for Text Entry to Test Length.

        Parameters
        ----------
        event : event obj
            The textEntry object from which to get the entered text.
        """
        try:
            self.testParameters['testDuration'] = int(event.GetEventObject().GetLineText(0))
        except ValueError:
            self.testParameters['testDuration'] = 0

    def applyTestSettings(self, event):
        self.testDuration = self.testParameters['testDuration']

    def cancelTestSettings(self, event):
        self.testParameters['testDuration'] = self.DEFAULT_TEST_DURATION

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

        return int(data_y)

    def plotter(self, y_new):
        self.y_var = np.append(self.y_var, y_new)
        self.y_var = self.y_var[1:(self.PLOT_WINDOW + 1)]
        self.line.set_ydata(self.y_var)
        self.ax.relim()
        self.ax.autoscale_view()

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


    def debugTestSettings(self):
        print(f"Temporary Duration: {self.testParameters['testDuration']}")
        print(f"Actual Duration: {self.testDuration}")




