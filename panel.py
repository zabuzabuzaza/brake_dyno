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

import matplotlib
import numpy as np

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx

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

        self.variables = {"testLength": 10}
        self.interactables = {}


        self.sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.drawStack1(self.sizer1)

        self.SetSizer(self.sizer1)

        self.interactables['button1'].Bind(wx.EVT_BUTTON, self.executeAcq)
        self.interactables['textEntry'].Bind(wx.EVT_TEXT_ENTER, self.getTestLength)

    def drawStack1(self, parentSizer):
        staticText1 = wx.StaticText(self, label="Welcome to our Brake Dyno", style=wx.ALIGN_CENTRE)
        parentSizer.Add(staticText1, 0, wx.ALIGN_CENTRE, 5)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        staticText2 = wx.StaticText(self, label="Enter test length (seconds)")
        sizer2.Add(staticText2, 0, wx.ALIGN_CENTER, 5)
        enterText = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        sizer2.Add(enterText, 0, wx.ALIGN_CENTER, 5)
        self.interactables['textEntry'] = enterText


        parentSizer.Add(sizer2, 0, wx.ALIGN_CENTER, 5)
        self.drawPlot(parentSizer)

        but1 = wx.Button(self, label="Record Data")
        self.interactables['button1'] = but1

        parentSizer.Add(but1, 0, wx.ALIGN_CENTER, 5)

    def drawPlot(self, mainSizer):
        figure = Figure()
        axes = figure.add_subplot(111)
        canvas = FigureCanvas(self, -1, figure)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(canvas, 1, wx.LEFT | wx.TOP | wx.GROW)

        mainSizer.Add(sizer, 0, wx.ALIGN_CENTER, 5)

        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.variables['dataset'] = [t, s]
        axes.plot(t, s)


    def getTestLength(self, event):
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
        test_time = int(event.GetEventObject().GetLineText(0))
        self.variables['testLength'] = test_time
        self.interactables['button1'].SetLabel(f"Start Recording {test_time}")
        print(self.variables['testLength'])


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
        newDataset.runDataAcq(ser, limit= self.variables['testLength'])
        data = newDataset.dataset

        # takes the Dataset ojbect and saves its contents to file
        util.data2csv(data)
        #self.variables['dataset'] = data
        time, x_values = util.extractValues(data)
        self.variables['dataset'] = [time, x_values]

        ser.close()





