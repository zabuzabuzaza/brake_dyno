# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 01:01:03 2020

@author: iamde
"""
import wx

class SettingsFrame( wx.Frame ):

    def __init__( self, parent ):
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
        SCROLL_RATE = 5
        WRAP = -1

        # Sizes
        FRAMESIZE = (700, 300)
        SCROLLMIN = (-1, 100)
        SCROLLMAX = (-1, 200)

        # Component Names




        # Begin Initialisation
        wx.Frame.__init__ ( self, parent, ID, EMPTYNAME, POSITION, FRAMESIZE,
                           style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        fgSizer2 = wx.FlexGridSizer( rows=0, cols=2, vgap=0, hgap=0)
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText2 = wx.StaticText( self, ID, u"Test Run", POSITION, SIZE, STYLE )
        self.m_staticText2.Wrap( WRAP )
        fgSizer2.Add( self.m_staticText2, PROPORTION0, FLAG, BORDER )

        m_choice1Choices = [ u"Test Run 1", u"Test Run 2", u"Test RUn 3" ]
        self.m_choice1 = wx.Choice( self, ID, POSITION, SIZE, m_choice1Choices, STYLE )
        self.m_choice1.SetSelection( 0 )
        fgSizer2.Add( self.m_choice1, PROPORTION0, FLAG, BORDER )

        self.m_staticText3 = wx.StaticText( self, ID, u"Test Duration", POSITION, SIZE, STYLE )
        self.m_staticText3.Wrap( WRAP )
        fgSizer2.Add( self.m_staticText3, PROPORTION0, FLAG, BORDER )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl2 = wx.TextCtrl( self, ID, EMPTYNAME, POSITION, SIZE, style=wx.TE_PROCESS_ENTER)
        bSizer3.Add( self.m_textCtrl2, PROPORTION0, FLAG, BORDER )

        self.m_staticText4 = wx.StaticText( self, ID, u"seconds", POSITION, SIZE, STYLE )
        self.m_staticText4.Wrap( WRAP )
        bSizer3.Add( self.m_staticText4, PROPORTION0, FLAG, BORDER )


        fgSizer2.Add( bSizer3, PROPORTION1, wx.EXPAND, BORDER )

        self.m_staticText5 = wx.StaticText( self, ID, u"Recording\nParameters", POSITION, SIZE, STYLE )
        self.m_staticText5.Wrap( WRAP )
        fgSizer2.Add( self.m_staticText5, PROPORTION0, FLAG, BORDER )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, ID, POSITION, SIZE, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( SCROLL_RATE, SCROLL_RATE )
        self.m_scrolledWindow1.SetMinSize( SCROLLMIN )
        self.m_scrolledWindow1.SetMaxSize( SCROLLMAX )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_checkBox1 = wx.CheckBox( self.m_scrolledWindow1, ID, u"X-Position", POSITION, SIZE, STYLE )
        self.m_checkBox1.SetValue(True)
        bSizer4.Add( self.m_checkBox1, PROPORTION0, FLAG, BORDER )

        self.m_checkBox2 = wx.CheckBox( self.m_scrolledWindow1, ID, u"Y-Position", POSITION, SIZE, STYLE )
        self.m_checkBox2.SetValue(True)
        bSizer4.Add( self.m_checkBox2, PROPORTION0, FLAG, BORDER )

        self.m_checkBox3 = wx.CheckBox( self.m_scrolledWindow1, ID, u"Rotor Temp", POSITION, SIZE, STYLE )
        bSizer4.Add( self.m_checkBox3, PROPORTION0, FLAG, BORDER )

        self.m_checkBox4 = wx.CheckBox( self.m_scrolledWindow1, ID, u"Caliper Temp", POSITION, SIZE, STYLE )
        bSizer4.Add( self.m_checkBox4, PROPORTION0, FLAG, BORDER )

        self.m_checkBox5 = wx.CheckBox( self.m_scrolledWindow1, ID, u"Motor Speed", POSITION, SIZE, STYLE )
        bSizer4.Add( self.m_checkBox5, PROPORTION0, FLAG, BORDER )


        self.m_scrolledWindow1.SetSizer( bSizer4 )
        self.m_scrolledWindow1.Layout()
        bSizer4.Fit( self.m_scrolledWindow1 )
        fgSizer2.Add( self.m_scrolledWindow1, PROPORTION1, wx.EXPAND|wx.ALL, BORDER )



        bSizer6.Add( fgSizer2, PROPORTION1, wx.EXPAND, BORDER )


        bSizer2.Add( bSizer6, PROPORTION1, wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button1 = wx.Button( self, ID, u"Apply Settings", POSITION, SIZE, STYLE )
        bSizer5.Add( self.m_button1, PROPORTION0, FLAG, BORDER )

        self.m_button2 = wx.Button( self, ID, u"Cancel", POSITION, SIZE, STYLE )
        bSizer5.Add( self.m_button2, PROPORTION0, FLAG, BORDER )


        bSizer2.Add( bSizer5, PROPORTION0, wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        self.SetSizer(bSizer2)





    def addTestRunChoiceHandler(self, handler):
        self.m_choice1.Bind( wx.EVT_CHOICE, self.setTestRun )

    def addTextCtrlHandler(self, handler):
        self.m_textCtrl2.Bind( wx.EVT_TEXT, handler )
        self.m_textCtrl2.Bind( wx.EVT_TEXT_ENTER, handler )

    def addCheckBoxHandler(self, handler):
        self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.setXRecord )
        self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.setYRecord )

    def addApplySettingsHandler(self, handler, frame):
        self.m_button1.Bind( wx.EVT_BUTTON, lambda event: handler(event, frame) )

    def addCancelSettingsHandler(self, handler, frame):
        self.m_button2.Bind( wx.EVT_BUTTON, lambda event: handler(event, frame) )

    def setTestRun( self, event ):
        event.Skip()

    def setXRecord( self, event ):
        event.Skip()

    def setYRecord( self, event ):
        event.Skip()




