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
            (self.module1, 5), 
            (self.module2, 5), 
            (self.module3, 13), 
            (self.module4, 14), 
            (self.module5, 15), 
            (self.module6, 16), 
            (self.module7, 17), 
            (self.module8, 18), 
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



    def runModule(self, module_name, *args):
        return_value = module_name(*args)

        return return_value


    def module1(self, time, limit):
        # self.currentModule = "Module 1: Break In"
        # print("Module 1: Break In")
        print(time*0)
        return 0

    def module2(self, time, limit):
        # self.currentModule = "Module 2: Burnish"
        # print("Module 2: Burnish")
        if time < limit/2: 
            print(time)
            return time
        else: 
            print(-time + time*limit)
            return -time + time*limit


    def module3(self, time, limit):
        # self.currentModule = "Module 3: Fraction Characteristic After Burnish"
        # print("Module 3: Fraction Characteristic After Burnish")
        if time < limit/4: 
            print(time)
            return time
        elif limit/4 <= time < (3*limit)/4: 
            print(0.5)
            return 0.5
        else: 
            print(-time + time*limit)
            return -time + time*limit


    def module4(self, time, limit):
        # self.currentModule = "Module 4: Drag Module"
        # print("Module 4: Drag Module")
        if time < limit/4: 
            print(time)
            return time
        elif limit/4 <= time < (3*limit)/4: 
            print(4)
            return 4
        else: 
            print(-time + limit)
            return -time + limit


    def module5(self, time, limit):
        # self.currentModule = "Module 5: Conditioning Stops"
        # print("Module 5: Conditioning Stops")
        if time < limit/4: 
            print(time)
            return time
        elif limit/4 <= time < (3*limit)/4: 
            print(5)
            return 5
        else: 
            print(-time + time*limit)
            return -time + time*limit


    def module6(self, time, limit):
        # self.currentModule = "Module 6: Backward / Forward Drag Module"
        # print("Module 6: Backward / Forward Drag Module")
        if time < limit/4: 
            print(time)
            return time
        elif limit/4 <= time < (3*limit)/4: 
            print(6)
            return 6
        else: 
            print(-time + time*limit)
            return -time + time*limit


    def module7(self, time, limit):
        # self.currentModule = "Module 7: Deceleration Stops"
        # print("Module 7: Deceleration Stops")
        if time < limit/4: 
            print(time)
            return time
        elif limit/4 <= time < (3*limit)/4: 
            print(7)
            return 7
        else: 
            print(-time + time*limit)
            return -time + time*limit


    def module8(self, time, limit):
        # self.currentModule = "Module 8: Fraction Characteristic"
        # print("Module 8: Fraction Characteristic")
        if time < limit/4: 
            print(time)
            return time
        elif limit/4 <= time < (3*limit)/4: 
            print(8)
            return 8
        else: 
            print(-time + time*limit)
            return -time + time*limit

        
