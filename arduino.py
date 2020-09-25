# -*- coding: utf-8 -*-
"""
Arduino class for Arduino handling
"""
import serial

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


