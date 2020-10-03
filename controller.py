# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:47:15 2020

@author: iamde
"""
import wx
from frames import MainFrame, SerialDialog
from panel import MainPanel

from model import Model
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
        self.newSchedule = TestSchedules() 

        self.mainFrame = MainFrame(None, WINDOW_TITLE, WINDOW_SIZE)

        self.mainPanel = MainPanel(self.mainFrame)

        self.mainFrame.Centre()
        self.mainFrame.Show()

        self.mainFrame.Layout()
        self.statusBar = self.mainFrame.CreateStatusBar( 1 )

        self.addMainFrameEventHandlers()
        self.addMainPanelEventHandlers()

        self.defaultSettings(None)

        self.start_time = 0

    def addMainFrameEventHandlers(self):
        self.mainFrame.addCloseProgramHandler(self.closeProgram)

    def addMainPanelEventHandlers(self):
        self.mainPanel.addTestScheduleHandler(self.setTestSchedule)
        self.mainPanel.addParamRecordHandler(self.setParamRecord)
        self.mainPanel.addCOMPortHandler(self.setCOMPort)
        self.mainPanel.addFileNameHandler(self.setFileName)

        self.mainPanel.addApplySettingsHandler(self.applySettings)
        self.mainPanel.addDefaultSettingsHandler(self.defaultSettings)

        self.mainPanel.addStartTestHandler(self.startTest)
        self.mainPanel.addStopTestHander(self.stopTest)

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
        # print(self.model.tempParameters['testParams'])

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
        self.model.testDuration = self.newSchedule.scheduleList[self.model.testParameters['testSchedule']]
        self.mainPanel.updateSettings(self.model)

        # add plot to GUI
        for param in self.model.testParameters['testParams']: 
            self.mainPanel.drawPlot(param, self.model.createCanvas(param))

    def defaultSettings( self, event ):
        # check COM status and update time
        self.model.defaultParameters['COMStatus'] = self.checkCOMPort(self.model.defaultParameters['COMPort'])
        self.model.defaultParameters['fileName'] = util.getDate() + ".csv"
        
        self.model.testParameters = dict(self.model.defaultParameters)
        self.model.testDuration = self.newSchedule.scheduleList[self.model.testParameters['testSchedule']]
        self.mainPanel.updateSettings(self.model)

        # add plot to GUI
        for param in self.model.testParameters['testParams']: 
            self.mainPanel.drawPlot(param, self.model.createCanvas(param))


    def checkCOMPort(self, port_Name): 
        newArduino = Arduino(port_Name)
        try: 
            ser = newArduino.ser
            return True
        except AttributeError: 
            return False

    def startTest(self, event):
        
        self.start_time = time.time()
        
        self.mainPanel.progressGauge.SetRange(self.model.testDuration)

        self.TEST_CONTINUE = True
        self.newSchedule.testEnd = False

        # threads
        t_daq = threading.Thread(target=self.data_aq) 
        t_ser = threading.Thread(target=self.sendSerial)
        t_daq.start()
        t_ser.start()

    def sendSerial(self): 
        
        # newSchedule.currentModule = self.model.testParameters['testSchedule']

        # set timer and acquisition rate
        # self.start_time = time.time()
        
        
        while not self.newSchedule.testEnd: 
            # print(self.model.latest_data[1])
            # self.ser.write(str.encode(str(self.model.latest_data[1])))

            # newSchedule.runSchedule(self.model.testParameters['testSchedule'])
            
            for module, length in self.newSchedule.scheduleModules[self.model.testParameters['testSchedule']]:
                module_start = time.time()
                self.mainPanel.moduleGauge.SetRange(length)
                self.newSchedule.runModule(module)
                print(f"Sleeping for time {length}")
                time.sleep(length)
                self.newSchedule.testEnd = True

                self.mainPanel.updateModuleConditions(time.time() - module_start, module.__name__)

                if not self.TEST_CONTINUE: 
                    break

            self.newSchedule.testEnd = True

        
        # completes GUI updates
        if self.TEST_CONTINUE: 
            self.mainPanel.updateTotalConditions(self.model.testDuration)
        else: 
            self.mainPanel.updateTotalConditions(time.time() - self.start_time, stopped=True)

        print("Test Ended")


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
        
        # reset plot
        for param in self.model.testParameters['testParams']: 
            self.mainPanel.updatePlot(param, self.model.createCanvas(param))


        count = 0
        
        while (time.time() - self.start_time) < self.model.testDuration and self.TEST_CONTINUE:
            current = time.time() - self.start_time
            
            # reads and stores serial data
            _, x_data, y_data, _, _, _ = self.model.getSerialData(ser, current)
            
            # update test conditions
            self.mainPanel.updateTotalConditions(current)

            # it's too much for the program to have 2 plots at the same time
            # so we need to slow it down
            if count % 2 == 0: 
                self.mainPanel.updatePlot("X-Stick", self.model.plot1("X-Stick", current, x_data))
                self.mainPanel.updatePlot("Y-Stick", self.model.plot1("Y-Stick", current, y_data))
                
            count += 1

        # completes GUI updates
        if self.TEST_CONTINUE: 
            self.mainPanel.updateTotalConditions(self.model.testDuration)
        else: 
            self.mainPanel.updateTotalConditions(time.time() - self.start_time, stopped=True)
        
        # saves data to csv file & closes serial port safely
        util.data2csv(self.model.dataSet, self.model.testParameters['fileName'])

        ser.close()
        
        
        

    def stopTest( self, event ):
        self.TEST_CONTINUE = False
        print(self.TEST_CONTINUE)

        














