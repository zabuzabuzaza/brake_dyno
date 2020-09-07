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
        super().__init__(parent)


        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        bSizer7.AddSpacer(0)

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Test Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        bSizer8.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"seconds", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )


        bSizer7.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Test Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer7.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_gauge2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge2.SetValue( 0 )
        bSizer7.Add( self.m_gauge2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer7.AddSpacer(0)

        bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
        self.SetSizer(bSizer1)

    def addTextCtrlHandler(self, handler):
        self.m_textCtrl2.Bind( wx.EVT_TEXT, handler )
        self.m_textCtrl2.Bind( wx.EVT_TEXT_ENTER, handler )










