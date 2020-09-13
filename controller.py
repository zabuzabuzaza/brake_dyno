# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:47:15 2020

@author: iamde
"""
import wx
from mainFrame import MainFrame
from mainPanel import MainPanel
from settingsFrame import SettingsFrame

from model import Model
from arduino import Arduino
from schedules import TestSchedules
import util

import time


class Controller():
    def __init__(self):
        """
        For event handling for all frames and panels.
        """
        WINDOW_SIZE = (1800, 1000)
        WINDOW_TITLE = "braaaaakkkkkee ddyyynnnnnooo"

        self.testSchedules = TestSchedules()
        self.model = Model()

        self.mainFrame = MainFrame(None, WINDOW_TITLE, WINDOW_SIZE)

        self.mainPanel = MainPanel(self.mainFrame)

        self.mainFrame.Centre()
        self.mainFrame.Show()

        self.mainFrame.Layout()
        self.statusBar = self.mainFrame.CreateStatusBar( 1 )


        self.addMainFrameEventHandlers()
        self.addMainPanelEventHandlers()

        self.mainPanel.updateSettings(self.model)

    def addMainFrameEventHandlers(self):
        self.mainFrame.addCloseProgramHandler(self.closeProgram)
        # self.mainFrame.addRecordingSettingsHandler(self.openRecordingSettings)
        # self.mainFrame.addStartTestHandler(self.executeAcq)

        # disable main frame duration setting
        # self.mainPanel.addTextCtrlHandler(self.model.getTestDuration)

    def addMainPanelEventHandlers(self):
        self.mainPanel.addTestScheduleHandler(self.setTestSchedule)
        self.mainPanel.addXRecordHandler(self.setXRecord)
        self.mainPanel.addYRecordHandler(self.setYRecord)
        self.mainPanel.addRotorTRecordHandler(self.setRotorTRecord)
        self.mainPanel.addCalipTRecordHandler(self.setCalipTRecord)
        self.mainPanel.addMotorRecordHandler(self.setMotorRecord)
        self.mainPanel.addCOMPortHandler(self.setCOMPort)
        self.mainPanel.addFileNameHandler(self.setFileName)
        self.mainPanel.addApplySettingsHandler(self.applySettings)
        self.mainPanel.addDefaultSettingsHandler(self.defaultSettings)
        self.mainPanel.addStartTestHandler(self.startTest)
        self.mainPanel.addStopTestHander(self.stopTest)

    # def addSettingsFrameEventHandlers(self, settingsFrame):
    #     settingsFrame.addTestRunChoiceHandler(self.setTestRun)
    #     settingsFrame.addTextCtrlHandler(self.model.getTestDuration)
    #     settingsFrame.addCheckBoxHandler(self.setRecords)

    #     settingsFrame.addApplySettingsHandler(self.applyTestSettings, settingsFrame)
    #     settingsFrame.addCancelSettingsHandler(self.cancelTestSettings, settingsFrame)

    # def openRecordingSettings(self, event):
    #     try:
    #         settingsFrame = SettingsFrame(None)
    #     except wx.PyNoAppError:
    #         print("Try running it again. ")
    #     settingsFrame.Centre()
    #     settingsFrame.Show()
    #     self.addSettingsFrameEventHandlers(settingsFrame)

    def closeProgram(self, event):
        print("Close Program")
        self.mainFrame.Close()

    def setTestSchedule( self, event ):
        try:
            self.model.testParameters['testSchedule'] = event.GetString()
        except (ValueError, KeyError):
            self.model.testParameters['testSchedule'] = "Joystick"

    def setXRecord( self, event ):
        print("X rec")

    def setYRecord( self, event ):
        print("y rec")

    def setRotorTRecord( self, event ):
        print("rotor")

    def setCalipTRecord( self, event ):
        print("calip")

    def setMotorRecord( self, event ):
        print("motor")

    def setCOMPort( self, event ):
        try:
            self.model.testParameters['COMPort'] = event.GetString()
        except (ValueError, KeyError):
            self.model.testParameters['COMPort'] = "COM3"

    def setFileName( self, event ):
        try:
            self.model.testParameters['fileName'] = event.GetString() + ".csv"
        except (ValueError, KeyError):
            self.model.testParameters['fileName'] = "data.csv"

    def applySettings( self, event ):
        try:
            self.model.testSchedule = self.model.testParameters['testSchedule']
        except (ValueError, KeyError):
            self.model.testSchedule = "Joystick"
        try:
            self.model.COMPort = self.model.testParameters['COMPort']
        except (ValueError, KeyError):
            self.model.COMPort = "COM3"
        try:
            self.model.fileName = self.model.testParameters['fileName']
        except (ValueError, KeyError):
            self.model.fileName = "data.csv"
        self.mainPanel.updateSettings(self.model)
        self.mainPanel.updateConditions(self.model, "Test not started.")

    def defaultSettings( self, event ):
        self.model.testSchedule = "Joystick"
        self.model.COMPort = "COM3"
        self.model.fileName = "data.csv"
        self.mainPanel.updateSettings(self.model)

    def startTest(self, event):
        """
        Opens the serial port and starts the process of:
            - reading the serial port
            - data recording
            - saving data to a csv file
        Closes the serial when done.
        Parameters
        --------
        event : event handler
            A reference to the action that triggered this function.
        """
        # open serial port
        newArduino = Arduino()
        ser = newArduino.ser

        # add plot to GUI
        self.model.createCanvas(self.mainPanel.tab1)
        # self.mainPanel.addToPanel(self.model.canvas)

        # set timer and acquisition rate
        count = 0
        start_time = time.time()
        self.mainPanel.progressGauge.SetRange(self.model.testDuration)

        while (time.time() - start_time) < self.model.testDuration:
            # reads and stores serial data
            x_data, y_data = self.model.getSerialData(ser, (time.time() - start_time))

            # update test conditions
            self.mainPanel.updateConditions(time.time() - start_time)

            # to increase system performance, only plot every few datapoints
            # maybe in the future i'll implement a variable acquisition rate
            # depending on system performance
            if count % 2 == 0:
                self.model.plotter(x_data, y_data)

            count += 1

        self.mainPanel.updateConditions(self.model.testDuration)
        # completes GUI updates
        # saves data to csv file & closes serial port safely
        util.data2csv(self.model.dataSet)
        ser.close()

    def stopTest( self, event ):
        print("stop")














