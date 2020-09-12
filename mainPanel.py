# -*- coding: utf-8 -*-
"""
Class for plotting
"""

import wx
import wx.xrc

class MainPanel(wx.Panel):
    def __init__(self, parent):
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
        POSITION = wx.DefaultPosition
        EMPTYNAME = wx.EmptyString
        SIZE = wx.DefaultSize
        ID = wx.ID_ANY
        FLAG = wx.ALL
        STYLE = 0
        BORDER = 5
        PROPORTION0 = 0
        PROPORTION1 = 1
        WRAP = -1

        super().__init__(parent)

        self.bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        bSizer7.AddSpacer(0)

        # bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        # self.m_staticText6 = wx.StaticText( self, ID, u"Test Duration", POSITION, SIZE, STYLE )
        # self.m_staticText6.Wrap( WRAP )
        # bSizer8.Add( self.m_staticText6, PROPORTION0, FLAG, BORDER )

        # self.m_textCtrl2 = wx.TextCtrl( self, ID, EMPTYNAME, POSITION, SIZE, style=wx.TE_PROCESS_ENTER)
        # bSizer8.Add( self.m_textCtrl2, PROPORTION0, FLAG, BORDER )

        # self.m_staticText7 = wx.StaticText( self, ID, u"seconds", POSITION, SIZE, STYLE )
        # self.m_staticText7.Wrap( WRAP )
        # bSizer8.Add( self.m_staticText7, PROPORTION0, FLAG, BORDER )

        # bSizer7.Add( bSizer8, PROPORTION0, wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        self.m_staticText5 = wx.StaticText( self, ID, u"Test Progress", POSITION, SIZE, STYLE )
        self.m_staticText5.Wrap( WRAP )
        bSizer7.Add( self.m_staticText5, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        self.m_gauge2 = wx.Gauge( self, ID, 100, POSITION, SIZE, wx.GA_HORIZONTAL )
        self.m_gauge2.SetValue( 0 )
        bSizer7.Add( self.m_gauge2, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        bSizer7.AddSpacer(0)

        self.bSizer1.Add( bSizer7, PROPORTION1, wx.EXPAND, BORDER )
        self.SetSizer(self.bSizer1)

    def addToPanel(self, canvas):
        self.bSizer1.Add(canvas)
        self.Fit()

    def addTextCtrlHandler(self, handler):
        self.m_textCtrl2.Bind( wx.EVT_TEXT, handler )
        self.m_textCtrl2.Bind( wx.EVT_TEXT_ENTER, handler )










