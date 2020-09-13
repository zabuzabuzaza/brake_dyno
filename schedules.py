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
        self.next = True

        self.moduleList = [self.module1, self.module2, self.module3, self.module4, self.module5]

    def scheduleJoystick(self):

        if next:
            try:
                self.moduleList[0]()
            except IndexError:
                print("Test ended")
                self.testEnd = True
                return

            #print(f"just did {self.moduleList[0]}")
            self.moduleList = self.moduleList[1:]
            #print(f"List is now {self.moduleList}")
            time.sleep(1)
            print("Sleep")
            self.next = False


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

    def module2(self):
        self.currentModule = "Module 2: Burnish"

    def module3(self):
        self.currentModule = "Module 3: Fraction Characteristic After Burnish"

    def module4(self):
        self.currentModule = "Module 4: Drag Module"

    def module5(self):
        self.currentModule = "Module 5: Conditioning Stops"

    def module6(self):
        self.currentModule = "Module 6: Backward / Forward Drag Module"

    def module7(self):
        self.currentModule = "Module 7: Deceleration Stops"

    def module8(self):
        self.currentModule = "Module 8: Fraction Characteristic"

