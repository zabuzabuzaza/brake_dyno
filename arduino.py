# -*- coding: utf-8 -*-
"""
Arduino class for Arduino handling
"""
from model import Model

import serial


class Arduino(Model):
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

        Returns
        -------
        None.

        """
        self.ser = serial.Serial(port)


