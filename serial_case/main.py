# -*- coding: utf-8 -*-
"""
Serial version
"""
import sys
import serial 
import wx 

from arduino import Arduino
from dataset import DataSet
from interface import Gooey
import util



def main(): 
    
    ex = wx.App()
    Gooey(None, "My Gooey")
    ex.MainLoop()
     
<<<<<<< HEAD

    
    # newArduino = Arduino()
    # ser = newArduino.ser
    
    
    # newDataset = DataSet() 
=======
>>>>>>> 18f9e3c37e809017f20be9fd5dd79fd71ab51d9e
    

if __name__ == '__main__': 
    try: 
        main()
    except Exception as e:
        #tempArduino = serial.Serial('COM3')
        #tempArduino.close()
        print(e)
        sys.exit(0)