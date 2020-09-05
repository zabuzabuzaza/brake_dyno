# -*- coding: utf-8 -*-
"""
Arduino class for Arduino handling
"""
import serial


class Arduino: 
    def __init__(self): 
        self.ser = serial.Serial('COM3')
        
    def printArduino(self): 
        print('inside arduino')

