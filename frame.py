# -*- coding: utf-8 -*-
"""
GUI class to handle interations and whatnot.
"""

#from panel import initialPanel

import wx
import wx.xrc

class Gooey(wx.Frame):
    def __init__(self, parent, title, winSize=( 800,700 )):
        """
        Initialises the main GUI frame for all user interation and event
        handling.

        Parameters
        ----------
        parent : Frame
            a parent frame in which to initialise in. Usually 'None'.
        title : string
            a title for the window.
        """
        super(Gooey, self).__init__(parent, title = title, size = winSize)


