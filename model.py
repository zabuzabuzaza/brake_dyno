# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:10:48 2020

@author: iamde
"""

from arduino import Arduino
from dataset import DataSet
import util


class Model():
    def __init__(self):
        """
        For keeping track of all information of the GUI.
        """
        self.DEFAULT_TEST_DURATION = 5


        self.testDuration = self.DEFAULT_TEST_DURATION

        # store settings that will either be applied or cancelled
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
        print(f"Temporary Duration: {self.testParameters['testDuration']}")
        print(f"Actual Duration: {self.testDuration}")

    def applyTestSettings(self, event):
        self.testDuration = self.testParameters['testDuration']
        print(f"Temporary Duration: {self.testParameters['testDuration']}")
        print(f"Actual Duration: {self.testDuration}")

    def cancelTestSettings(self, event):
        self.testParameters['testDuration'] = self.DEFAULT_TEST_DURATION
        print(f"Temporary Duration: {self.testParameters['testDuration']}")
        print(f"Actual Duration: {self.testDuration}")


    def executeAcq(self, event):
        """
        Opens the serial port and starts the process of:
            - reading the serial port
            - data recording
            - saving data to a csv file
        Closes the serial when done.

        Parameters
        ----------
        event : event handler
            A reference to the action that triggered this function.
        """
        # opens serial connection
        newArduino = Arduino()
        ser = newArduino.ser

        # creates a Dataset object to retrieve and store the data
        newDataset = DataSet()
        newDataset.runDataAcq(ser, limit= self.testDuration)
        data = newDataset.dataset

        # takes the Dataset ojbect and saves its contents to file
        util.data2csv(data)

        ser.close()




