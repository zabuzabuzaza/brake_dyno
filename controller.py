# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:47:15 2020

@author: iamde
"""
import wx
from model import Model
from frame import Gooey
from panel1 import InitialPanel
from panel2 import SettingsPanel

class Controller():
    def __init__(self):
        """
        For event handling for all frames and panels.
        """
        self.model = Model()
        self.frame = Gooey(None, title="My Gooey", winSize=( 800, 500 ))

        self.panel1 = InitialPanel(self.frame)
        self.frame2 = SettingsPanel(None)

        self.frame.Centre()
        self.frame.Show()

        self.frame.Layout()
        self.frame.m_statusBar1 = self.frame.CreateStatusBar( 3 )

        self.frame2.Centre()
        self.frame2.Show()





