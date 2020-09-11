# -*- coding: utf-8 -*-
"""
Class for handling data storage and retrieval.
"""


import time

class DataSet():
    def __init__(self):
        """
        Initialises a Dataset object for the collection and retrieval of
        serial data coming in.
        """
        self.dataset = [["Seconds", "X_Data", "Y Data"]]

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

        self.dataset.append(data)

        # keep for now for testing / debugging
        # self.ledCheck(data_x, serial)


    def ledCheck(self, data_x, serial, checkPoint = 514):
        """
        Used mainly for test verification. Turns the BUILTIN led on if the
        analog input is in the upper half of its range, off otherwise.

        Parameters
        ----------
        data : int
            analog value read from serial.
        serial : (py)serial object
            The serial from which to read / write from.
        checkPoint : int, optional
            Value from which to compare analog range to. The default is 514.
        """
        if data_x > checkPoint:
            serial.write(bytes(1))
        else:
            serial.write(bytes(0))

