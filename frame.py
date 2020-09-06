# -*- coding: utf-8 -*-
"""
GUI class to handle interations and whatnot.
"""

from arduino import Arduino
from dataset import DataSet
import util
#from panel import initialPanel

import wx
import wx.xrc


class Gooey(wx.Frame):
    def __init__(self, parent, title, winSize=( 800,700 )):
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
        super(Gooey, self).__init__(parent, title = title, size = winSize)

        self.testDuration = 10
        self.dataset = []

        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem1 )

        self.m_menubar1.Append( self.m_menu1, u"File" )

        self.m_menu2 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Recording Settings", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem3 )

        self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Start Recording", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem4 )

        self.m_menubar1.Append( self.m_menu2, u"Test" )

        self.SetMenuBar( self.m_menubar1 )

        self.Bind( wx.EVT_MENU, self.openRecordingSettings, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.startRecording, id = self.m_menuItem4.GetId() )

    def openRecordingSettings(self, event):
        print("open new frame")

    def startRecording(self, event):
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
        newDataset.runDataAcq(ser, limit= self.testDuration)
        data = newDataset.dataset

        # takes the Dataset ojbect and saves its contents to file
        util.data2csv(data)
        #self.variables['dataset'] = data
        #time, x_values = util.extractValues(data)
        #self.variables['dataset'] = [time, x_values]

        ser.close()


