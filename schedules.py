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

        self.next = True

        # self.moduleLengths = [1, 2, 3, 4, 5, 6, 7, 8]
        self.moduleList = [
            (self.module1, 1), 
            (self.module2, 2), 
            (self.module3, 3), 
            (self.module4, 4), 
            (self.module5, 5), 
            (self.module6, 6), 
            (self.module7, 7), 
            (self.module8, 8), 
        ]

        # indexes of the order of each module for each schedule
        self.scheduleOrders = {
            "Joystick": [1, 4, 5, 2, 3], 
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
                total += self.moduleList[mod_num - 1][1]
                self.scheduleModules[schedule_name].append((
                    self.moduleList[mod_num - 1][0], self.moduleList[mod_num - 1][1]
                ))

            self.scheduleList[schedule_name] = total


    def runSchedule(self, schedule_name): 

        for module, length in self.scheduleModules[schedule_name]: 
            module()
            print(f"Sleeping for time {length}")
            time.sleep(length)

        self.testEnd = True
        print("Test Ended")

    def runModule(self, module_name):
        module_name()


    def scheduleJoystick(self):

        
        try:
            self.moduleList[0]()
        except IndexError:
            print("Test ended")
            self.testEnd = True
            return

        time.sleep(self.moduelLengths[0])
        print("Sleep")
        #print(f"just did {self.moduleList[0]}")
        self.moduleList = self.moduleList[1:]
        self.moduleLengths = self.moduleLengths[1:]
        #print(f"List is now {self.moduleList}")
        
        


        #time.sleep(5)

    def scheduleA(self):
        self.module1()
        self.module2()
        self.module3()

        self.module4()
        self.module5()
        self.module6()
        self.module7()
        self.module8()

        self.module4()
        self.module5()
        self.module6()
        self.module7()
        self.module8()

        self.module4()
        self.module5()
        self.module6()
        self.module7()
        self.module8()

    def module1(self):
        self.currentModule = "Module 1: Break In"
        print("Module 1: Break In")

    def module2(self):
        self.currentModule = "Module 2: Burnish"
        print("Module 2: Burnish")


    def module3(self):
        self.currentModule = "Module 3: Fraction Characteristic After Burnish"
        print("Module 3: Fraction Characteristic After Burnish")


    def module4(self):
        self.currentModule = "Module 4: Drag Module"
        print("Module 4: Drag Module")


    def module5(self):
        self.currentModule = "Module 5: Conditioning Stops"
        print("Module 5: Conditioning Stops")


    def module6(self):
        self.currentModule = "Module 6: Backward / Forward Drag Module"
        print("Module 6: Backward / Forward Drag Module")


    def module7(self):
        self.currentModule = "Module 7: Deceleration Stops"
        print("Module 7: Deceleration Stops")


    def module8(self):
        self.currentModule = "Module 8: Fraction Characteristic"
        print("Module 8: Fraction Characteristic")

        
