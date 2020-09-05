# -*- coding: utf-8 -*-
"""
Class for handling data storage and retrieval. 
"""

class DataSet: 
    def __init__(self): 
        """
        Initialises a Dataset object for the collection and retrieval of 
        serial data coming in. 
        """
        self.dataset = []
        
    def runDataAcq(self, serial, limit=2000): 
        """
        Starts the Arduino data collection loop to read serial input for a 
        given amount of time. 

        Parameters
        ----------
        serial : (py)serial obj
            The serial from which to read / write from. 
        limit : int, optional
            A set time limit (in milliseconds) to record analog data in. This 
            will change as various test runs are implemented. 
            The default is 2000 (ms).

        Returns
        -------
        None.

        """
        count = 0
        while count < limit: 
            self.getSerialData(serial)
            count += 1
        
    def getSerialData(self, serial): 
        """
        Reads the incoming data from the serial port and adds it to this 
        object's data structure. 

        Parameters
        ----------
        serial : (py)serial obj
            The serial from which to read / write from. 

        Returns
        -------
        None.

        """
        
        ser_bytes = serial.readline()
        # will need to explore int to byte conversion that doesn't scale the 
        # input weirdly. For now, takes the incoming bytes (b'000/n') and takes
        # what we need
        data = int(str(ser_bytes[:-1])[2:-1])
        
        # keep for now until a live plot is implemented
        print(data)
        
        self.dataset.append(data)
        
        # keep for now for testing / debugging
        self.ledCheck(data, serial)
        
            
    def ledCheck(self, data, serial, checkPoint = 514): 
        """
        Used mainly for test verification. Turns the BUILTIN led on if the 
        analog input is in the upper half of its range, off otherwise. 

        Parameters
        ----------
        data : int 
            analog value read from serial. 
        serial : (py)serial object
            The serial from which to read / write from. 
        checkPoint : int, optional
            Value from which to compare analog range to. The default is 514.

        Returns
        -------
        None.

        """
        if data > checkPoint: 
            serial.write(bytes(1))
        else: 
            serial.write(bytes(0))   
            
