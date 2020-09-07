# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 01:01:03 2020

@author: iamde
"""
import wx

class SettingsFrame( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 674,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )


        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Test Run", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        fgSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

        m_choice1Choices = [ u"Test Run 1", u"Test Run 2", u"Test RUn 3" ]
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        fgSizer2.Add( self.m_choice1, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Test Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        bSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"seconds", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )


        fgSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Recording\nParameters", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        self.m_scrolledWindow1.SetMinSize( wx.Size( -1,100 ) )
        self.m_scrolledWindow1.SetMaxSize( wx.Size( -1,200 ) )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_checkBox1 = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"X-Position", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox1.SetValue(True)
        bSizer4.Add( self.m_checkBox1, 0, wx.ALL, 5 )

        self.m_checkBox2 = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Y-Position", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox2.SetValue(True)
        bSizer4.Add( self.m_checkBox2, 0, wx.ALL, 5 )

        self.m_checkBox3 = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Rotor Temp", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_checkBox3, 0, wx.ALL, 5 )

        self.m_checkBox4 = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Caliper Temp", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_checkBox4, 0, wx.ALL, 5 )

        self.m_checkBox5 = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Motor Speed", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_checkBox5, 0, wx.ALL, 5 )


        self.m_scrolledWindow1.SetSizer( bSizer4 )
        self.m_scrolledWindow1.Layout()
        bSizer4.Fit( self.m_scrolledWindow1 )
        fgSizer2.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer6.Add( fgSizer2, 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer6, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Apply Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button2, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.SetSizer(bSizer2)

        # Connect Events
        self.m_choice1.Bind( wx.EVT_CHOICE, self.setTestRun )
        self.m_textCtrl2.Bind( wx.EVT_TEXT, self.setTestDuration )
        self.m_textCtrl2.Bind( wx.EVT_TEXT_ENTER, self.setTestDuration )
        self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.setXRecord )
        self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.setYRecord )
        self.m_button1.Bind( wx.EVT_BUTTON, self.resetTestSettings )
        self.m_button2.Bind( wx.EVT_BUTTON, self.applyTestSettings )

        # Virtual event handlers, overide them in your derived class


    def setTestRun( self, event ):
        event.Skip()

    def setTestDuration( self, event ):
        event.Skip()

    def setXRecord( self, event ):
        event.Skip()

    def setYRecord( self, event ):
        event.Skip()

    def resetTestSettings( self, event ):
        event.Skip()

    def applyTestSettings( self, event ):
        event.Skip()

