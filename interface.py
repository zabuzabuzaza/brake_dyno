# -*- coding: utf-8 -*-
"""
GUI class to handle interations and whatnot. 
"""

from dataset import DataSet
from arduino import Arduino
import util
import wx

class Gooey(wx.Frame): 
    def __init__(self, parent, title):
        """
        Initialises the main GUI frame for all user interation and event 
        handling. 

        Parameters
        ----------
        parent : Frame
            a parent frame in which to initialise in. Usually 'None'. 
        title : string
            a title for the window. 
        """
        super(Gooey, self).__init__(parent, title=title, size=(200,150))
        self.SetTitle(title)
        self.initUI()
        
    def initUI(self): 
        """
        Populates the frame with the required components and functionality. 

        Returns
        -------
        None.
        """
        panel = wx.Panel(self) 
        
        self.but2 = wx.Button(panel, label="Record Data")
        self.but2.Bind(wx.EVT_BUTTON, self.executeAcq)
        
        self.Centre()
        self.Show(True)
        
    def onClicked(self, event): 
        """
        DEPRECATED. It's only here so I don't keep forgetting the structure
        for an event handler. 
        """
        buttonLabel = event.GetEventObject().GetLabel() 
        print(buttonLabel)
        
    def onMouseMove(self, e): 
        """
        DEPRECATED. It's only here so I don't keep forgetting the structure
        for an event handler. 
        """
        x, y = e.GetPosition()
        print(f"Current mouse position x = {x}, y = {y}")
        
    def executeAcq(self, event): 
        """
        Opens the serial port and starts the process of:
            - reading the serial port 
            - data recording
            - saving data to a csv file
        Closes the serial when done. 

        Parameters
        ----------
        event : event handler
            A reference to the action that triggered this function. 

        Returns
        -------
        None.

        """
        # opens serial connection
        newArduino = Arduino()
        ser = newArduino.ser
        
        # creates a Dataset object to retrieve and store the data
        newDataset = DataSet() 
        newDataset.runDataAcq(ser)
        data = newDataset.dataset    
        
        # takes the Dataset ojbect and saves its contents to file
        util.data2csv(data)
        
        ser.close()
