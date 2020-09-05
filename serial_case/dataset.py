# -*- coding: utf-8 -*-
"""
Class for handling the data
"""

class DataSet: 
    def __init__(self): 
        self.dataset = []
        
    def runDataAcq(self, serial, limit=2000): 
        count = 0
        while count < limit: 
            self.getSerialData(serial)
            count += 1
        
    def getSerialData(self, serial): 
        ser_bytes = serial.readline()
        data = int(str(ser_bytes[:-1])[2:-1])
        print(data)
        
        self.dataset.append(data)
        
        self.ledCheck(data, serial)
        
            
    def ledCheck(self, data, serial, checkPoint = 514): 
        if data > 514: 
            serial.write(bytes(1))
        else: 
            serial.write(bytes(0))   
            
