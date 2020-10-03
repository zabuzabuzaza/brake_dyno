# -*- coding: utf-8 -*-
"""
GUI class to handle interations and whatnot.
"""

import wx
import wx.xrc


class MainFrame(wx.Frame):
    def __init__(self, parent, title, winSize=( 800,800 )):
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
        self.menuExit = wx.MenuItem( self.menu1, ID, "Exit", EMPTYNAME, ITEMTYPE )
        self.menu1.Append( self.menuExit )

        self.menubar.Append( self.menu1, u"File" )

        self.SetMenuBar( self.menubar )

    def addCloseProgramHandler(self, handler):
        self.Bind( wx.EVT_MENU, handler, id = self.menuExit.GetId() )

    def addRecordingSettingsHandler(self, handler):
        self.Bind( wx.EVT_MENU, handler, id = self.menuItem3.GetId() )

    def addStartTestHandler(self, handler):
        self.Bind( wx.EVT_MENU, handler, id = self.menuItem4.GetId() )

class SerialDialog(wx.Dialog): 
    def __init__( self, parent , title=""):
        """Dialog box that pops up due to a bad connection with the selected serial 
        port. 

        Parameters
        ----------
        parent : wx.Frame
            The parent frame to spawn this dialog window. 
        title : str, optional
            window title, by default ""
        """
        wx.Dialog.__init__ ( self, parent, title=title, size=( 250,250 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
        
        main_box = wx.BoxSizer( wx.VERTICAL )
        
        self.dialog_message = wx.StaticText( self, wx.ID_ANY, "Dialog Here", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.dialog_message.Wrap( -1 )
        main_box.Add( self.dialog_message, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.SetSizer( main_box )
        self.Layout()
        
        self.Centre( wx.BOTH )

    def setDialogMessage(self, message): 
        self.dialog_message.SetLabel( message )
