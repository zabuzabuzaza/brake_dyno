# -*- coding: utf-8 -*-
"""
GUI
"""
from dataset import DataSet
from arduino import Arduino
import util
import wx

class Gooey(wx.Frame): 
    
    def __init__(self, parent, title):
        super(Gooey, self).__init__(parent, title=title, size=(200,150))
        self.SetSize((250, 180))
        self.SetTitle(title)
        self.initUI()
        
    def initUI(self): 
        panel = wx.Panel(self) 
        
        #self.but1 = wx.Button(panel, label="Button1")
        #self.but1.Bind(wx.EVT_BUTTON, self.onClicked)
        
        self.but2 = wx.Button(panel, label="Button2")
        self.but2.Bind(wx.EVT_BUTTON, self.executeAcq)
        
        self.Centre()
        self.Show(True)
        
    def onClicked(self, event): 
        buttonLabel = event.GetEventObject().GetLabel() 
        print(buttonLabel)
        
    def onMove(self, e): 
        x, y = e.GetPosition()
        print(f"Current window position x = {x}, y = {y}")
        
    def onMouseMove(self, e): 
        x, y = e.GetPosition()
        print(f"Current mouse position x = {x}, y = {y}")
        
    def executeAcq(self, event): 
            
        newArduino = Arduino()
        ser = newArduino.ser
        
        
        newDataset = DataSet() 
        newDataset.runDataAcq(ser)
        data = newDataset.dataset    
        
        util.data2csv(data)
