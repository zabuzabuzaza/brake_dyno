# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:47:15 2020

@author: iamde
"""
import wx
from frames import MainFrame, SerialDialog, ConstantSpeedOptions
from panel import MainPanel

from model import Model
from schedules import TestSchedules
import util
from util import Arduino

import time
import threading

DEBUG = False

# if the data logging is lagging behind input, turn this on
SLOW_PLOT = False

class Controller():
    def __init__(self):
        """
        For event handling for all frames and panels.
        """
        WINDOW_SIZE = (1500, 800)
        WINDOW_TITLE = "braaaaakkkkkee ddyyynnnnnooo"
        self.TEST_CONTINUE = True

        self.model = Model()
        self.schedule = TestSchedules() 

        self.mainFrame = MainFrame(None, WINDOW_TITLE, WINDOW_SIZE)

        self.mainPanel = MainPanel(self.mainFrame)

        self.mainFrame.Centre()
        self.mainFrame.Show()

        self.mainFrame.Layout()
        self.statusBar = self.mainFrame.CreateStatusBar( 1 )

        self.addMainFrameEventHandlers()
        self.addMainPanelEventHandlers()

        self.defaultSettings(None)
        self.constantspeed_test = ConstantSpeedOptions(self.mainFrame)

        self.start_time = 0
        self.speed = 0
        self.pressure = 0

    def addMainFrameEventHandlers(self):
        """Create event handlers for overall program handling. 
        """
        self.mainFrame.addCloseProgramHandler(self.closeProgram)

    def addMainPanelEventHandlers(self):
        """Add event handling for changing settings and starting tests. 
        """
        self.mainPanel.addTestScheduleHandler(self.setTestSchedule)
        self.mainPanel.addCOMInHandler(self.setCOMPort)
        # com port out to control system yet to be implemented
        self.mainPanel.addCOMOutHandler(self.setCOMPort)
        self.mainPanel.addFileNameHandler(self.setFileName)

        self.mainPanel.addApplySettingsHandler(self.applySettings)
        self.mainPanel.addDefaultSettingsHandler(self.defaultSettings)

        self.mainPanel.addStartTestHandler(self.startTest)
        self.mainPanel.addStopTestHander(self.stopTest)

    def closeProgram(self, event):
        """Closes the main window. 
        """
        if DEBUG: 
            print("Close Program")
        self.mainFrame.Close()

    def showDialog(self, message): 
        """Dialog Message for various events. 

        Parameters
        ----------
        message : str
            Display message in dialog window. 
        """
        new_Dialog = SerialDialog(self.mainFrame)
        new_Dialog.setDialogMessage(message)
        new_Dialog.ShowModal()

    def showConstantSpeedOptions(self): 
        
        self.constantspeed_test.setSettingsHandler(self.setConstantSpeedOptions)
        self.constantspeed_test.setApplyButtonHandler(self.applyConstantSettings)
        self.constantspeed_test.ShowModal()

        self.constantspeed_test.testPrint()

    def setTestSchedule( self, event ):
        """Add the selected test schedule in dropdown box to selected parameters. 
        """
        self.model.tempParameters['testSchedule'] = event.GetString()

    def setParamRecord( self, event ):  
        """PLEASE REMOVE. NO NEED FOR THIS ANYMORE. 
        """
        try: 
            param = self.model.ALL_PARAMETERS[event.GetId()]
        except IndexError: 
            param = ""

        if event.GetInt(): 
            if param not in self.model.tempParameters['testParams']: 
                self.model.tempParameters['testParams'].append(param)
        else: 
            self.model.tempParameters['testParams'].remove(param)

    def setCOMPort( self, event ):
        """Select the COM port where the Arduino is connected. 
        """
        self.model.tempParameters['COMPort'] = event.GetString()
        self.model.tempParameters['COMStatus'] = self.checkCOMPort(event.GetString())

    def setFileName( self, event ):
        """Select custom Folder Name to save the recorded data in.
        """
        self.model.tempParameters['fileName'] = event.GetString()

    def setConstantSpeedOptions(self, event): 
        id_number = event.GetId()
        input = event.GetString()

        if id_number == 1: 
            self.constantspeed_test.setSettingsLabels(1, input)
        elif id_number == 2: 
            self.constantspeed_test.setSettingsLabels(2, input)
        elif id_number == 3: 
            self.constantspeed_test.setSettingsLabels(3, input)
        else: 
            # should not happen
            pass

    def applySettings( self, event ):
        """Takes the settings temporarily selected, and permanently applies them to the actual program. 
        Change will not take place until the apply button is pressed. 
        """
        # check COM status and update time
        self.model.tempParameters['COMStatus'] = self.checkCOMPort(self.model.tempParameters['COMPort'])
        if self.model.tempParameters['fileName'] == self.model.testParameters['fileName']: 
            self.model.tempParameters['fileName'] = util.getDate()

        self.model.testParameters = dict(self.model.tempParameters)
        self.model.testDuration = self.schedule.scheduleList[self.model.testParameters['testSchedule']]
        self.mainPanel.updateSettings(self.model, self.schedule)

        # add plot to GUI
        self.mainPanel.drawPlot("Output Speed", self.model.createCanvas("Output Speed"))
        self.mainPanel.drawPlot("Pressure", self.model.createCanvas("Pressure"))
        for param in self.model.testParameters['testParams']: 
            self.mainPanel.drawPlot(param, self.model.createCanvas(param))

        self.showConstantSpeedOptions()

    def applyConstantSettings( self, event ): 
        if self.constantspeed_test.getOptionValidity(): 
            speeds, pressures, durations = self.constantspeed_test.getSettings()
            self.schedule.moduleList[self.schedule.scheduleOrders["Constant Speed"][0]-1] = (self.schedule.const_speed, speeds, pressures, durations)

            self.constantspeed_test.Close()

    def defaultSettings( self, event ):
        """Reverts the changed settings back to a default state as stored in defaultParameters in Model. 
        """
        # check COM status and update time
        self.model.defaultParameters['COMStatus'] = self.checkCOMPort(self.model.defaultParameters['COMPort'])
        self.model.defaultParameters['fileName'] = util.getDate()
        
        self.model.testParameters = dict(self.model.defaultParameters)
        self.model.testDuration = self.schedule.scheduleList[self.model.testParameters['testSchedule']]
        self.mainPanel.updateSettings(self.model, self.schedule)

        # add plot to GUI
        self.mainPanel.drawPlot("Output Speed", self.model.createCanvas("Output Speed"))
        self.mainPanel.drawPlot("Pressure", self.model.createCanvas("Pressure"))
        for param in self.model.testParameters['testParams']: 
            self.mainPanel.drawPlot(param, self.model.createCanvas(param))


    def checkCOMPort(self, port_Name): 
        """Checks status of COM Port. 

        Parameters
        ----------
        port_Name : str
            Name of COM port. Can be checked with Device Manager>Ports in Windows or through the Arduino IDE. 

        Returns
        -------
        COM Status : bool
        """
        newArduino = Arduino(port_Name)
        try: 
            ser = newArduino.ser
            return True
        except AttributeError: 
            return False

    def startTest(self, event):
        """Creates threads to handle the data acquisition, the control ssytem and GUI updates. 
        """
        
        self.start_time = time.time()

        self.TEST_CONTINUE = True
        self.schedule.testEnd = False

        # threads
        t_daq = threading.Thread(target=self.data_aq) 
        t_ser = threading.Thread(target=self.sendSerial)
        t_daq.start()
        t_ser.start()

    def sendSerial(self): 
        """Control System for the VDF speed and Brake Actuation. For the selected Test Schedule, conducts the 
        respective test and plots the output values. Once the test is stopped prematurely or naturally 
        finishes, saves all output and input data to csv. 
        """
        test_start = time.time()
        folder_name = self.model.testParameters['fileName']
        total = self.schedule.scheduleList[self.model.testParameters['testSchedule']]
        self.mainPanel.progressGauge.SetRange(total)
        self.passed = 0

        # refresh plot 
        self.mainPanel.updatePlot("Output Speed", self.model.createCanvas("Output Speed"))
        self.mainPanel.updatePlot("Pressure", self.model.createCanvas("Pressure"))

        if self.model.testParameters['testSchedule'] == "Constant Speed": 
            self.constant_speed(total, test_start, folder_name)
        elif self.model.testParameters['testSchedule'] == "Torque Control": 
            self.torque_control(total, test_start, folder_name)
        else: 
            self.brake_squeal(total, test_start, folder_name)

        self.finish_serial(time.time() - test_start, total)
        util.data2csv(self.model.dataSet, foldername=folder_name)
        self.TEST_CONTINUE = False

    def constant_speed(self, total, test_start, folder_name): 
        """Conducts the "Constant Speed" test schedule. 
        For a list of initial motor speeds, and brake pressure levels, the brakes will be applied
        for a given duration. The speed will be held constant during this application. 

        Parameters
        ----------
        total : int
            total number of tests (speed, pressure levels and duration combinations)
        test_start : float
            start time of test
        folder_name : str
            folder to save each individual test log to
        """
        # get the test info for each module
        for module, speed_list, pressure_levels, duration_list in self.schedule.scheduleModules[self.model.testParameters['testSchedule']]:
            for s_index, speed in enumerate(speed_list): 
                self.mainPanel.moduleGauge.SetRange(len(duration_list))

                for p_index, pressure_lvl in enumerate(pressure_levels): 
                    for d_index, duration in enumerate(duration_list): 
                        # here, insert brake warm up routine to bring brakes up to the required temperature
                        # or wait until it cools down

                        self.speed = speed

                        module_start = time.time()

                        while (time.time()-module_start) < duration: 
                            if not self.TEST_CONTINUE: 
                                self.finish_serial((time.time() - test_start), total)
                                return

                            self.pressure = self.schedule.runModule(module, (time.time() - module_start), pressure_lvl)

                            self.mainPanel.updatePlot("Output Speed", self.model.plot1("Output Speed", (time.time() - test_start), self.speed))
                            self.mainPanel.updatePlot("Pressure", self.model.plot1("Pressure", (time.time() - test_start), self.pressure))

                            time.sleep(0.1)
                            self.mainPanel.updateModuleConditions((s_index, len(speed_list)), (d_index, len(duration_list)), module.__name__)
                            self.mainPanel.updateTotalConditions((time.time() - test_start), total, self.passed)

                            if DEBUG: 
                                print(f"Duration = {duration}, Speed={self.speed}")

                        util.data2csv(self.model.moduleSet, module.__name__, duration, self.speed, folder_name)
                        self.model.moduleSet = self.model.data_titles.copy()
                            
                        self.passed += 1

    def torque_control(self, total, test_start, folder_name): 
        """Conducts the "Torque Control" test schedule. 
        For a list of speed pairs (initial speed, end speed), and brake pressure levels, the brakes will be applied
        at a given pressure level until the speed reached the end speed. The torque will be held constant during this application. 

        Parameters
        ----------
        total : int
            total number of tests (speed, pressure levels and duration combinations)
        test_start : float
            start time of test
        folder_name : str
            folder to save each individual test log to
        """

        for module, speed_pairs, pressure_levels in self.schedule.scheduleModules[self.model.testParameters['testSchedule']]:
            for s_index, pair in enumerate(speed_pairs): 
                self.mainPanel.moduleGauge.SetRange(len(speed_pairs))

                for p_index, pressure_lvl in enumerate(pressure_levels): 
                    
                    # here, insert brake warm up routine to bring brakes up to the required temperature
                    # or wait until it cools down
                    while self.speed < pair[0]: 
                        if not self.TEST_CONTINUE: 
                            self.finish_serial((time.time() - test_start), total)
                            return
                        self.speed += 0.2

                        self.mainPanel.updatePlot("Output Speed", self.model.plot1("Output Speed", (time.time() - test_start), self.speed))
                        self.mainPanel.updatePlot("Pressure", self.model.plot1("Pressure", (time.time() - test_start), 0))
                        time.sleep(0.1)
                    
                    self.speed = pair[0]

                    module_start = time.time()

                    while self.speed > pair[1]: 
                        if not self.TEST_CONTINUE: 
                            self.finish_serial((time.time() - test_start), total)
                            return

                        self.pressure = self.schedule.runModule(module, (time.time() - module_start), pressure_lvl)

                        self.mainPanel.updatePlot("Output Speed", self.model.plot1("Output Speed", (time.time() - test_start), self.speed))
                        self.mainPanel.updatePlot("Pressure", self.model.plot1("Pressure", (time.time() - test_start), self.pressure))

                        time.sleep(0.1)
                        self.mainPanel.updateModuleConditions((p_index, len(pressure_levels)), (s_index, len(speed_pairs)), module.__name__)
                        self.mainPanel.updateTotalConditions((time.time() - test_start), total, self.passed)

                        self.speed -= 0.1
                        print(f"Pressure = {self.pressure}, Speed={self.speed}")

                    util.data2csv(self.model.moduleSet, module.__name__, self.pressure, self.speed, folder_name)
                    self.model.moduleSet = self.model.data_titles.copy()
                        
                    self.passed += 1

    def brake_squeal(self, total, test_start, folder_name): 
        """Conducts the various "Brake Squeal" test schedules as per the SAE J2521 Test Procedures. 
        For a list of brake pressure levels, initial rotor temperatures, the brakes will be applied between two speed bounds. 

        Parameters
        ----------
        total : int
            total number of tests (speed, pressure levels and duration combinations)
        test_start : float
            start time of test
        folder_name : str
            folder to save each individual test log to
        """
        for module, initial_temps, pressure_levels, speed_bounds in self.schedule.scheduleModules[self.model.testParameters['testSchedule']]:
            for p_index, pressure_lvl in enumerate(pressure_levels): 
                
                self.mainPanel.moduleGauge.SetRange(len(initial_temps))

                for t_index, temp in enumerate(initial_temps): 

                    # here, insert brake warm up routine to bring brakes up to the required temperature
                    # or wait until it cools down
                    while self.speed < speed_bounds[0]: 
                        if not self.TEST_CONTINUE: 
                            self.finish_serial((time.time() - test_start), total)
                            return
                        self.speed += 0.4

                        self.mainPanel.updatePlot("Output Speed", self.model.plot1("Output Speed", (time.time() - test_start), self.speed))
                        self.mainPanel.updatePlot("Pressure", self.model.plot1("Pressure", (time.time() - test_start), 0))
                        time.sleep(0.1)

                    self.speed = speed_bounds[0]
                    module_start = time.time()

                    while self.speed > speed_bounds[-1]: 
                        if not self.TEST_CONTINUE: 
                            self.finish_serial((time.time() - test_start), total)
                            return
                        # if self.model
                        
                        self.pressure = self.schedule.runModule(module, (time.time() - module_start), pressure_lvl)
                        
                        self.mainPanel.updatePlot("Output Speed", self.model.plot1("Output Speed", (time.time() - test_start), self.speed))
                        self.mainPanel.updatePlot("Pressure", self.model.plot1("Pressure", (time.time() - test_start), self.pressure))

                        time.sleep(0.1)
                        self.mainPanel.updateModuleConditions((p_index, len(pressure_levels)), (t_index, len(initial_temps)), module.__name__)
                        self.mainPanel.updateTotalConditions((time.time() - test_start), total, self.passed)

                        self.speed -= 0.1
                        print(f"Temp={temp}, P = {self.pressure}, Speed={self.speed}")

                    util.data2csv(self.model.moduleSet, module.__name__, temp, pressure_lvl, folder_name)
                    self.model.moduleSet = self.model.data_titles.copy()
                        
                    self.passed += 1
                    
    def finish_serial(self, finish_time, total): 
        """Ends the test (triggered at test end or through user interruption via stop test button). 
        """

        self.schedule.testEnd = True

        # completes GUI updates
        self.mainPanel.updateTotalConditions(finish_time, total, self.passed, stopped=(not self.TEST_CONTINUE))
        
        if DEBUG: 
            print("Test Ended")


    def data_aq(self): 
        """
        Opens the serial port and starts the process of:
            - reading the serial port
            - data recording
            - saving data to a csv file
        Closes the serial when done.

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
        while self.TEST_CONTINUE:
            current = time.time() - self.start_time
            
            # reads and stores serial data
            serial_list = self.model.getSerialData(ser, current)
            #_, x_data, y_data, t_couple1, _, _ = tuple(serial_list)

            # due to me not having an actual speed measurement, we're using fake speeds
            serial_list.pop(-1)
            self.model.append_data(serial_list + [self.speed, self.pressure])
            # update test conditions
            # self.mainPanel.updateTotalConditions(current, self.model.testDuration)

            # it's too much for the program to have 2 plots at the same time
            # so we need to slow it down
            if SLOW_PLOT: 
                if count % 1 == 0: 
                    self.mainPanel.updatePlot("X-Stick", self.model.plot1("X-Stick", current, serial_list[1]))
                    self.mainPanel.updatePlot("Y-Stick", self.model.plot1("Y-Stick", current, serial_list[2]))
                    self.mainPanel.updatePlot("RotorT", self.model.plot1("RotorT", current, serial_list[3]))
                    self.mainPanel.updatePlot("Caliper Temp", self.model.plot1("Caliper Temp", current, serial_list[4]))
                    
                    self.mainPanel.updatePlot("Motor", self.model.plot1("Motor", current, self.speed))
            else: 
                self.mainPanel.updatePlot("X-Stick", self.model.plot1("X-Stick", current, serial_list[1]))
                self.mainPanel.updatePlot("Y-Stick", self.model.plot1("Y-Stick", current, serial_list[2]))
                self.mainPanel.updatePlot("RotorT", self.model.plot1("RotorT", current, serial_list[3]))
                self.mainPanel.updatePlot("Caliper Temp", self.model.plot1("Caliper Temp", current, serial_list[4]))
                self.mainPanel.updatePlot("Motor", self.model.plot1("Motor", current, self.speed))

            count += 1

        ser.close()
        
    def stopTest( self, event ):
        """Interrupts the test run. 
        """
        self.TEST_CONTINUE = False
        

        














