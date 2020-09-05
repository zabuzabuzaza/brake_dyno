# -*- coding: utf-8 -*-
"""
Parallels a typical arduino script, with functions such as a setup & 
looping function. 

Requires the "StandardFirmata" script uploaded to the Arduino. This is 
obtainable from the Arduino IDE with File > Examples > Firmata > 
StandardFirmata. 
"""
import sys
import time 
import serial

from arduino import Arduino
from frame import Frame
import util


def main(): 
    """
    
    """
    #newFrame = Frame()
    #newFrame.executeLoop()

    
    newArduino = Arduino() 
    
    newBoard = newArduino.board
    
    d_in = newArduino.digital_input
    a_in = newArduino.analog_input 
    led = newArduino.led
    
    
    stopped = False
    dataset = []
    
    
    while not stopped:
        if d_in.read(): 
            led.write(1)
            stopped = True
    
        # record analog input 
        a_value = a_in.read()
        dataset.append(a_value)
        print(f"{a_value}")
        
        time.sleep(0.1)
        
    print(dataset)
    util.data2csv(dataset)
        
        
    print("Done")
    newBoard.exit()


if __name__ == '__main__': 
    try: 
        main()
    except KeyboardInterrupt: 
        sys.exit(0)