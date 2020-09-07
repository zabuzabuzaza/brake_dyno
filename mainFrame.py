# -*- coding: utf-8 -*-
"""
GUI class to handle interations and whatnot.
"""

from arduino import Arduino
from dataset import DataSet
import util

import wx
import wx.xrc


class MainFrame(wx.Frame):
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
        super(MainFrame, self).__init__(parent, title = title, size = winSize)

        self.testDuration = 10
        self.dataset = []

        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem1 )

        self.m_menubar1.Append( self.m_menu1, u"File" )

        self.m_menu2 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Recording Settings", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem3 )

        self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Start Recording", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem4 )

        self.m_menubar1.Append( self.m_menu2, u"Test" )

        self.SetMenuBar( self.m_menubar1 )


    def addRecordingSettingsHandler(self, handler):
        self.Bind( wx.EVT_MENU, handler, id = self.m_menuItem3.GetId() )

    def addStartTestHandler(self, handler):
        self.Bind( wx.EVT_MENU, handler, id = self.m_menuItem4.GetId() )
