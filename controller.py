# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:47:15 2020

@author: iamde
"""
import wx
from model import Model
from mainFrame import MainFrame
from mainPanel import MainPanel
from settingsFrame import SettingsFrame

import time


class Controller():
    def __init__(self):
        """
        For event handling for all frames and panels.
        """
        WINDOW_SIZE = (1000, 1000)
        WINDOW_TITLE = "braaaaakkkkkee ddyyynnnnnooo"

        self.model = Model()
        self.mainFrame = MainFrame(None, WINDOW_TITLE, WINDOW_SIZE)

        self.mainPanel = MainPanel(self.mainFrame)

        self.mainFrame.Centre()
        self.mainFrame.Show()

        self.mainFrame.Layout()
        self.statusBar = self.mainFrame.CreateStatusBar( 1 )


        self.addMainFrameEventHandlers()

    def addMainFrameEventHandlers(self):
        self.mainFrame.addRecordingSettingsHandler(self.openRecordingSettings)
        self.mainFrame.addStartTestHandler(self.executeAcq)

        # disable main frame duration setting
        # self.mainPanel.addTextCtrlHandler(self.model.getTestDuration)

    def addSettingsFrameEventHandlers(self, settingsFrame):
        settingsFrame.addTestRunChoiceHandler(self.setTestRun)
        settingsFrame.addTextCtrlHandler(self.model.getTestDuration)
        settingsFrame.addCheckBoxHandler(self.setRecords)

        settingsFrame.addApplySettingsHandler(self.applyTestSettings, settingsFrame)
        settingsFrame.addCancelSettingsHandler(self.cancelTestSettings, settingsFrame)

    def openRecordingSettings(self, event):
        try:
            settingsFrame = SettingsFrame(None)
        except wx.PyNoAppError:
            print("Try running it again. ")
        settingsFrame.Centre()
        settingsFrame.Show()
        self.addSettingsFrameEventHandlers(settingsFrame)

    def setTestRun( self, event ):
        event.Skip()

    def setRecords( self, event ):
        event.Skip()

    def executeAcq(self, event):
        self.model.executeAcq(event)
        self.mainPanel.m_gauge2.SetValue(self.model.testDuration)

    def applyTestSettings(self, event, frame):
        self.model.applyTestSettings(event)
        self.mainPanel.m_gauge2.SetRange(self.model.testDuration)
        frame.Close()

    def cancelTestSettings(self, event, frame):
        self.model.cancelTestSettings(event)
        frame.Close()














