# -*- coding: utf-8 -*-
"""
GUI class to handle interations and whatnot.
"""


import wx
import wx.xrc


class MainFrame(wx.Frame):
    def __init__(self, parent, title, winSize=( 1200,1000 )):
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
        # Formatting constants
        EMPTYNAME = wx.EmptyString
        ITEMTYPE = wx.ITEM_NORMAL
        ID = wx.ID_ANY

        super(MainFrame, self).__init__(parent, title = title, size = winSize)

        self.menubar = wx.MenuBar( 0 )
        self.menu1 = wx.Menu()
        self.menuExit = wx.MenuItem( self.menu1, ID, u"Exit", EMPTYNAME, ITEMTYPE )
        self.menu1.Append( self.menuExit )

        self.menubar.Append( self.menu1, u"File" )

        self.menu2 = wx.Menu()
        self.menuItem3 = wx.MenuItem( self.menu2, ID, u"Recording Settings", EMPTYNAME, ITEMTYPE )
        self.menu2.Append( self.menuItem3 )

        self.menuItem4 = wx.MenuItem( self.menu2, ID, u"Start Recording", EMPTYNAME, ITEMTYPE )
        self.menu2.Append( self.menuItem4 )

        self.menubar.Append( self.menu2, u"Test (deprecated)" )

        self.SetMenuBar( self.menubar )

    def addCloseProgramHandler(self, handler):
        self.Bind( wx.EVT_MENU, handler, id = self.menuExit.GetId() )

    def addRecordingSettingsHandler(self, handler):
        self.Bind( wx.EVT_MENU, handler, id = self.menuItem3.GetId() )

    def addStartTestHandler(self, handler):
        self.Bind( wx.EVT_MENU, handler, id = self.menuItem4.GetId() )
