# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:47:15 2020

@author: iamde
"""
import wx
from model import Model
from frame import Gooey
from panel import InitialPanel

class Controller():
    def __init__(self):
        """
        For event handling for all frames and panels.
        """
        self.model = Model()
        self.frame = Gooey(None, "My Gooey")

        self.panel = InitialPanel(self.frame)

        self.frame.Centre()
        self.frame.Show()






