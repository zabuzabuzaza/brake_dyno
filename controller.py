# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:47:15 2020

@author: iamde
"""
import wx
from mainFrame import MainFrame
from mainPanel import MainPanel
from dialogs import SerialDialog

from model import Model
# from arduino import Arduino
from schedules import TestSchedules
import util
from util import Arduino

import time
import threading


class Controller():
    def __init__(self):
        """
        For event handling for all frames and panels.
        """
        WINDOW_SIZE = (1500, 800)
        WINDOW_TITLE = "braaaaakkkkkee ddyyynnnnnooo"
        self.TEST_CONTINUE = True

        self.model = Model()

        self.mainFrame = MainFrame(None, WINDOW_TITLE, WINDOW_SIZE)

        self.mainPanel = MainPanel(self.mainFrame)

        self.mainFrame.Centre()
        self.mainFrame.Show()

        self.mainFrame.Layout()
        self.statusBar = self.mainFrame.CreateStatusBar( 1 )

        self.addMainFrameEventHandlers()
        self.addMainPanelEventHandlers()

        self.defaultSettings(None)
        # self.mainPanel.updateSettings(self.model)

    def addMainFrameEventHandlers(self):
        self.mainFrame.addCloseProgramHandler(self.closeProgram)
        # self.mainFrame.addRecordingSettingsHandler(self.openRecordingSettings)
        # self.mainFrame.addStartTestHandler(self.executeAcq)

        # disable main frame duration setting
        # self.mainPanel.addTextCtrlHandler(self.model.getTestDuration)

    def addMainPanelEventHandlers(self):
        self.mainPanel.addTestScheduleHandler(self.setTestSchedule)
        self.mainPanel.addParamRecordHandler(self.setParamRecord)
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

    def showDialog(self, message): 
        new_Dialog = SerialDialog(self.mainFrame)
        new_Dialog.setDialogMessage(message)
        new_Dialog.ShowModal()

    def setTestSchedule( self, event ):
        self.model.tempParameters['testSchedule'] = event.GetString()

    def setParamRecord( self, event ):  
        try: 
            param = self.model.ALL_PARAMETERS[event.GetId() - 1]
        except IndexError: 
            param = ""

        if event.GetInt(): 
            if param not in self.model.tempParameters['testParams']: 
                self.model.tempParameters['testParams'].append(param)
        else: 
            self.model.tempParameters['testParams'].remove(param)

        # keep for debugging
        print(self.model.tempParameters['testParams'])

    def setCOMPort( self, event ):
        self.model.tempParameters['COMPort'] = event.GetString()
        self.model.tempParameters['COMStatus'] = self.checkCOMPort(event.GetString())

    def setFileName( self, event ):
        self.model.tempParameters['fileName'] = event.GetString() + ".csv"

    def applySettings( self, event ):
        # check COM status and update time
        self.model.tempParameters['COMStatus'] = self.checkCOMPort(self.model.tempParameters['COMPort'])
        if self.model.tempParameters['fileName'] == self.model.testParameters['fileName']: 
            self.model.tempParameters['fileName'] = util.getDate() + ".csv"

        self.model.testParameters = dict(self.model.tempParameters)
        self.mainPanel.updateSettings(self.model)

    def defaultSettings( self, event ):
        # check COM status and update time
        self.model.defaultParameters['COMStatus'] = self.checkCOMPort(self.model.defaultParameters['COMPort'])
        self.model.defaultParameters['fileName'] = util.getDate() + ".csv"
        
        self.model.testParameters = dict(self.model.defaultParameters)
        self.mainPanel.updateSettings(self.model)

    def checkCOMPort(self, port_Name): 
        newArduino = Arduino(port_Name)
        try: 
            ser = newArduino.ser
            return True
        except AttributeError: 
            return False

    def startTest(self, event):
        t = threading.Thread(target=self.data_aq) 
        t.start()


    def data_aq(self): 
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
        if not self.checkCOMPort(self.model.testParameters['COMPort']): 
            message = """No device detected in serial port.\n
                    Try again or check your connections."""
            self.showDialog(message)
            return
        
        newArduino = Arduino(self.model.testParameters['COMPort'])
        ser = newArduino.ser

        # add plot to GUI
        # self.model.createCanvas(self.mainPanel.tab1)
        self.mainPanel.drawPlot(self.model.createCanvas())

        # set timer and acquisition rate
        start_time = time.time()
        self.TEST_CONTINUE = True
        self.mainPanel.progressGauge.SetRange(self.model.testDuration)

        while (time.time() - start_time) < self.model.testDuration and self.TEST_CONTINUE:
            # reads and stores serial data
            x_data, y_data = self.model.getSerialData(ser, (time.time() - start_time))

            # update test conditions
            self.mainPanel.updateConditions(time.time() - start_time)
            self.mainPanel.drawPlot(self.model.plotter((time.time() - start_time), x_data, y_data))

        # completes GUI updates
        if self.TEST_CONTINUE: 
            self.mainPanel.updateConditions(self.model.testDuration)
        else: 
            self.mainPanel.updateConditions(time.time() - start_time, stopped=True)
        
        # saves data to csv file & closes serial port safely
        util.data2csv(self.model.dataSet, self.model.testParameters['fileName'])
        ser.close()

    def stopTest( self, event ):
        self.TEST_CONTINUE = False

        














