# -*- coding: utf-8 -*-
"""
GUI class to handle interations and whatnot.
"""

from dataset import DataSet
from arduino import Arduino
import util
import wx
import wx.xrc

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
        super(Gooey, self).__init__(parent, title = title, size = ( 700,250 ))

        panel = wx.Panel(self)

        sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.staticText1 = wx.StaticText(panel, label="Welcome to our Brake Dyno", style=wx.ALIGN_CENTRE)
        sizer1.Add(self.staticText1, 0, wx.ALIGN_CENTRE, 5)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText2 = wx.StaticText(panel, label="Enter test length (milliseconds)")
        sizer2.Add(self.staticText2, 0, wx.ALIGN_CENTER, 5)
        self.enterText = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        sizer2.Add(self.enterText, 0, wx.ALIGN_CENTER, 5)
        self.test_length = 2000

        sizer1.Add(sizer2, 0, wx.ALIGN_CENTER, 5)


        self.but1 = wx.Button(panel, label="Record Data")
        sizer1.Add(self.but1, 0, wx.ALIGN_CENTER, 5)



        panel.SetSizer(sizer1)

        self.Centre()
        self.Show()

        self.but1.Bind(wx.EVT_BUTTON, self.executeAcq)
        self.enterText.Bind(wx.EVT_TEXT_ENTER, self.getTestLength)


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

    def getTestLength(self, event):
        test_time = int(event.GetEventObject().GetLineText(0))
        self.test_length = test_time
        self.but1.SetLabel(f"Start Recording {test_time}")
        print(self.test_length)

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
        newDataset.runDataAcq(ser, limit= self.test_length)
        data = newDataset.dataset

        # takes the Dataset ojbect and saves its contents to file
        util.data2csv(data)

        ser.close()



