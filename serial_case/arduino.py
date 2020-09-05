# -*- coding: utf-8 -*-
"""
Arduino class for Arduino handling
"""
import serial


class Arduino: 
    def __init__(self): 
        """
        Initialises the serial connection for communication between Arduino 
        & computer. 
        """
        self.ser = serial.Serial('COM3')
        

    