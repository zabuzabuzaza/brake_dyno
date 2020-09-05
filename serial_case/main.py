# -*- coding: utf-8 -*-
"""
Serial version
"""
import sys
import serial 

from arduino import Arduino

def main(): 
    
    newArduino = Arduino()
    newArduino.printArduino()
    ser = newArduino.ser
    
    count = 0
    while count < 2000: 
        ser_bytes = ser.readline()
        data = int.from_bytes(ser_bytes, sys.byteorder)
        print(data)
        count += 1
        
        if data > 175000000: 
            ser.write(bytes(1))
        else: 
            ser.write(bytes(0))
        
    
    ser.close()

if __name__ == '__main__': 
    try: 
        main()
    except Exception as e:
        #serial.Serial('COM3').close()
        print(e)
        sys.exit(0)