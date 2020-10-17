# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:50:17 2020

@author: iamde
"""
import time

class TestSchedules():
    def __init__(self):
        """
        Stores all the test schedules
        """
        self.testEnd = False
        self.currentModule = "Not testing"
        self.scheduleList = {
            "Joystick": 0, 
            "Schedule A": 0, 
            "Schedule B": 0, 
            "Schedule C": 0, 
        }

        self.next = False

        # each module has 
        # a list of initial brake temperatures 
        # brake pressures &
        # start and release speeds
        self.moduleList = [
            (self.module1, [100], [30], [80, 30]), 
            (self.module2, [100], [15, 30, 15, 18, 22, 38, 15, 26, 18, 34, 15, 26, 15, 22, 
             30, 46, 26, 51, 22, 18, 42, 15, 18, 46, 26, 15, 34, 22, 18, 30, 18, 38], [80, 30]), 
            (self.module3, [100], [30], [80, 30]), 
            (self.module4, [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 
            275, 250, 225, 200, 175, 150, 125, 100, 75, 50], [0, 30, 5, 25, 10, 20, 15], [10, 3]), 
            (self.module5, [100, 150], [30, 5, 25, 10, 20, 15], [50, 0.5]), 
            (self.module6, [150, 125, 100, 75, 50], [0, 20, 5, 15, 10], [3, -3]), 
            (self.module7, [50, 100, 150, 200, 250, 200, 150, 100, 50], [30, 5, 25, 10, 20, 15], [50, 0.5]), 
            (self.module8, [100], [30], [80, 30]), 
        ]

        # indexes of the order of each module for each schedule
        self.scheduleOrders = {
            "Joystick": [1, 3, 5, 6, 8], 
            "Schedule A": [1, 2, 3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8], 
            "Schedule B": [1, 2, 3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8], 
            "Schedule C": [1, 2, 3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8], 
        }
        self.scheduleModules = {
            "Joystick": [], 
            "Schedule A": [], 
            "Schedule B": [], 
            "Schedule C": [], 
        }

        self.createSchedules()
    
    def createSchedules(self): 
        
        for schedule_name in self.scheduleList.keys(): 
            total = 0
            for mod_num in self.scheduleOrders[schedule_name]: 
                # find the total number of speed and pressure combinations
                total += len(self.moduleList[mod_num - 1][1]) * len(self.moduleList[mod_num - 1][2])
                self.scheduleModules[schedule_name].append(self.moduleList[mod_num - 1])

            self.scheduleList[schedule_name] = total



    def runModule(self, module_name, *args):
        return_value = module_name(*args)

        return return_value


    def module1(self, time, peak):
        # self.currentModule = "Module 1: Break In"
        # print("Module 1: Break In")
        if time < 1: 
            return peak*time
        else: 
            return peak


    def module2(self, time, peak):
        # self.currentModule = "Module 2: Burnish"
        # print("Module 2: Burnish")
        if time < 1: 
            return peak*time
        else: 
            return peak


    def module3(self, time, peak):
        # self.currentModule = "Module 3: Fraction Characteristic After Burnish"
        # print("Module 3: Fraction Characteristic After Burnish")
        if time < 1: 
            return peak*time
        else: 
            return peak


    def module4(self, time, peak):
        # self.currentModule = "Module 4: Drag Module"
        # print("Module 4: Drag Module")
        if time < 1: 
            return peak*time
        else: 
            return peak


    def module5(self, time, peak):
        # self.currentModule = "Module 5: Conditioning Stops"
        # print("Module 5: Conditioning Stops")
        if time < 1: 
            return peak*time
        else: 
            return peak


    def module6(self, time, peak):
        # self.currentModule = "Module 6: Backward / Forward Drag Module"
        # print("Module 6: Backward / Forward Drag Module")
        if time < 1: 
            return peak*time
        else: 
            return peak


    def module7(self, time, peak):
        # self.currentModule = "Module 7: Deceleration Stops"
        # print("Module 7: Deceleration Stops")
        if time < 1: 
            return peak*time
        else: 
            return peak


    def module8(self, time, peak):
        # self.currentModule = "Module 8: Fraction Characteristic"
        # print("Module 8: Fraction Characteristic")
        if time < 1: 
            return peak*time
        else: 
            return peak

        
