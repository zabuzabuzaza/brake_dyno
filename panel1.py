# -*- coding: utf-8 -*-
"""
Class for plotting
"""

from dataset import DataSet
from arduino import Arduino
#from controller import Controller
import util
import wx
import wx.xrc


class InitialPanel(wx.Panel):
    def __init__(self, parent):
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
        super().__init__(parent)


        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )


        bSizer7.AddSpacer(0)

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Test Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        bSizer8.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"seconds", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )


        bSizer7.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Test Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer7.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_gauge2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge2.SetValue( 0 )
        bSizer7.Add( self.m_gauge2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer7.AddSpacer(0)


        bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
        self.SetSizer(bSizer1)


        self.m_textCtrl2.Bind( wx.EVT_TEXT, self.setTestDuration )
        self.m_textCtrl2.Bind( wx.EVT_TEXT_ENTER, self.setTestDuration )

    def setTestDuration(self, event):
        """
        Event handler for Text Entry to Test Length.

        Parameters
        ----------
        event : event obj
            The textEntry object from which to get the entered text.

        Returns
        -------
        None.

        """
        #test_time = int(event.GetEventObject().GetLineText(0))
        self.testDuration = int(event.GetEventObject().GetLineText(0))
        #self.variables['testLength'] = test_time
        #self.interactables['button1'].SetLabel(f"Start Recording {test_time}")
        #print(self.variables['testLength'])
        print(self.testDuration)


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
        newDataset.runDataAcq(ser, limit= self.testDuration)
        data = newDataset.dataset

        # takes the Dataset ojbect and saves its contents to file
        util.data2csv(data)
        #self.variables['dataset'] = data
        time, x_values = util.extractValues(data)
        self.variables['dataset'] = [time, x_values]

        ser.close()





