# -*- coding: utf-8 -*-
"""
Arduino class to handle Arduino
"""
import pyfirmata
import time

class Arduino():
    def __init__(self): 
        self.board = pyfirmata.Arduino('COM3')
        
        # starts iterator for input
        it = pyfirmata.util.Iterator(self.board)
        it.start() 
        
        self.analog_input = self.board.get_pin('a:0:i')
        self.digital_input = self.board.get_pin('d:12:i')
        
        self.led = self.board.get_pin('d:13:o') 
        


        
    def test_print(self): 
        print("inside Arduino")
        
        
