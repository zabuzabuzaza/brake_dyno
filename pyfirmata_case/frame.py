# -*- coding: utf-8 -*-
"""
Class for wxPython frame and all GUI stuff. 
"""

import wx 
 
class Frame():
    
    def __init__(self): 
        
        self.app = wx.App() 
        self.window = wx.Frame(None, title = "wxPython Frame", size = (300,200)) 
        self.panel = wx.Panel(self.window) 
        self.label = wx.StaticText(self.panel, label = "Hello World", 
                                   pos = (100,50)) 
        
        self.button = wx.Button(self.panel, label='Button')
        
        
        
        
        
        self.window.Show(True) 
        #self.app.MainLoop()
    
    def executeLoop(self):
        self.app.MainLoop()
        
    def updateText(self, string): 
        self.label.SetLabel(string)
        
    
        

