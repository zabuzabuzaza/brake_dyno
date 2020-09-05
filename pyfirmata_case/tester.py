# -*- coding: utf-8 -*-
"""
Test script used for testing. 

"""

import main 

import pyfirmata
import sys
import time

from frame import Frame

def blinker(): 
    """
    Tests for basic Arduino functionality. 
    """
    board = pyfirmata.Arduino('COM3')
    
    count = 0
    while count < 5:
        board.digital[13].write(1)
        time.sleep(1)
        board.digital[13].write(0)
        time.sleep(1)
        
        print(f"Count is {count}")
        count += 1
        
def tester_main(): 
    """
    Runs all testing functions with prints.
    """    
    board = pyfirmata.Arduino('COM3')
    
    print("Now running blinker() test")
    blinker()
    print("Now stopped blinker() test")
    
    board.exit()
    
def gui_tester(): 
    newFrame = Frame()
    time.sleep(2)
    newFrame.updateText("test")
    

if __name__ == '__main__': 
    try: 
        #main.main()
        
        #tester_main()
        
        gui_tester()
        
    except KeyboardInterrupt: 
        sys.exit(0)
