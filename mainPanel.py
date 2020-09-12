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
        EMPTY = wx.EmptyString
        SIZE = wx.DefaultSize
        ID = wx.ID_ANY
        FLAG = wx.ALL
        STYLE = 0
        BORDER = 5
        PROPORTION0 = 0
        PROPORTION1 = 1
        WRAP = -1

        self.gaugeRange = 100

        super().__init__(parent)

        boxA = wx.BoxSizer( wx.VERTICAL )

        #######################################################################
        #
        #   TOP PANE
        #
        #######################################################################

        #######################################################################
        # LEFT SETTINGS
        #######################################################################

        boxBTop = wx.BoxSizer( wx.HORIZONTAL )

        boxCTestParameters = wx.BoxSizer( wx.VERTICAL )

        self.titleParameters = wx.StaticText( self, ID, "Test Settings and Parameters", POSITION, SIZE, STYLE )
        self.titleParameters.Wrap( WRAP )
        boxCTestParameters.Add( self.titleParameters, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        self.divider1 = wx.StaticLine( self, ID, POSITION, SIZE, wx.LI_HORIZONTAL )
        boxCTestParameters.Add( self.divider1, PROPORTION0, wx.EXPAND |wx.ALL, BORDER )

        #######################################################################
        # List of test settings

        gridDTestParameters = wx.FlexGridSizer( 0, 2, 0, 0 )
        gridDTestParameters.SetFlexibleDirection( wx.BOTH )
        gridDTestParameters.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        #######################################################################
        # Test Schedule Chooser

        self.labelSchedule = wx.StaticText( self, ID, "Schedule", POSITION, SIZE, wx.ALIGN_RIGHT )
        self.labelSchedule.Wrap( WRAP )
        gridDTestParameters.Add( self.labelSchedule, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, BORDER )

        choiceScheduleChoices = [ "Joystick", "Schedule A", "Schedule B", "Schedule C", EMPTY ]
        self.choiceSchedule = wx.Choice( self,ID, POSITION, SIZE, choiceScheduleChoices, STYLE )
        self.choiceSchedule.SetSelection( 0 )
        gridDTestParameters.Add( self.choiceSchedule, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, BORDER )

        #######################################################################
        # Choose which parameters to record

        self.labelRecording = wx.StaticText( self, ID, "Parameter\nRecording", POSITION, SIZE, wx.ALIGN_RIGHT )
        self.labelRecording.Wrap( WRAP )
        gridDTestParameters.Add( self.labelRecording, PROPORTION0, wx.ALL|wx.ALIGN_RIGHT, BORDER )

        self.scrollEWinParam = wx.ScrolledWindow( self, ID, POSITION, SIZE, wx.HSCROLL|wx.VSCROLL )
        self.scrollEWinParam.SetScrollRate( 5, 5 )
        self.scrollEWinParam.SetMinSize( ( -1,150 ) )
        boxFParamChoices = wx.BoxSizer( wx.VERTICAL )

        #######################################################################
        # Checkbox list of parameters

        self.checkJoyX = wx.CheckBox( self.scrollEWinParam,ID, "X-Position", POSITION, SIZE, STYLE )
        self.checkJoyX.SetValue(True)
        boxFParamChoices.Add( self.checkJoyX, PROPORTION0, FLAG, BORDER )

        self.checkJoyY = wx.CheckBox( self.scrollEWinParam, ID, "Y-Position", POSITION, SIZE, STYLE )
        self.checkJoyY.SetValue(True)
        boxFParamChoices.Add( self.checkJoyY, PROPORTION0, FLAG, BORDER )

        self.checkRotorTemp = wx.CheckBox( self.scrollEWinParam, ID, u"Rotor Temp", POSITION, SIZE, STYLE )
        boxFParamChoices.Add( self.checkRotorTemp, PROPORTION0, FLAG, BORDER )

        self.checkCalipTemp = wx.CheckBox( self.scrollEWinParam, ID, u"Caliper Temp", POSITION, SIZE, STYLE )
        boxFParamChoices.Add( self.checkCalipTemp, PROPORTION0, FLAG, BORDER )

        self.checkMotorSpeed = wx.CheckBox( self.scrollEWinParam, ID, u"Motor Speed", POSITION, SIZE, STYLE )
        boxFParamChoices.Add( self.checkMotorSpeed, PROPORTION0, FLAG, BORDER )

        self.scrollEWinParam.SetSizer( boxFParamChoices )
        self.scrollEWinParam.Layout()
        boxFParamChoices.Fit( self.scrollEWinParam )
        gridDTestParameters.Add( self.scrollEWinParam, PROPORTION1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, BORDER )

        #######################################################################
        # Choose Serial Port to read / write

        self.labelCOMPort = wx.StaticText( self, ID, "COM Port", POSITION, SIZE, wx.ALIGN_RIGHT )
        self.labelCOMPort.Wrap( WRAP )
        gridDTestParameters.Add( self.labelCOMPort, PROPORTION0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, BORDER )

        self.entryCOMPort = wx.TextCtrl( self, ID, "COM3", POSITION, SIZE, wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
        gridDTestParameters.Add( self.entryCOMPort, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, BORDER )

        #######################################################################
        # Enter custom csv filename

        self.labelFileName = wx.StaticText( self, ID, "File Name\n(optional)", POSITION, SIZE, wx.ALIGN_RIGHT )
        self.labelFileName.Wrap( WRAP )
        gridDTestParameters.Add( self.labelFileName, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, BORDER )

        boxEFileName = wx.BoxSizer( wx.HORIZONTAL )

        self.entryFileName = wx.TextCtrl( self, ID, wx.EmptyString, POSITION, SIZE, wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
        boxEFileName.Add( self.entryFileName, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, BORDER )

        self.labelFileExtension = wx.StaticText( self, ID, ".csv", POSITION, SIZE, STYLE )
        self.labelFileExtension.Wrap( WRAP )
        boxEFileName.Add( self.labelFileExtension, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, BORDER )

        gridDTestParameters.Add( boxEFileName, PROPORTION1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, BORDER )

        boxCTestParameters.Add( gridDTestParameters, PROPORTION1, wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        #######################################################################
        # Apply / Reset settings

        boxDParamButtons = wx.BoxSizer( wx.HORIZONTAL )

        self.buttonApply = wx.Button( self, ID, "Apply", POSITION, SIZE, STYLE )
        boxDParamButtons.Add( self.buttonApply, PROPORTION1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, BORDER )

        self.buttonDefault = wx.Button( self, ID, u"Default", POSITION, SIZE, STYLE )
        boxDParamButtons.Add( self.buttonDefault, PROPORTION1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, BORDER )

        boxCTestParameters.Add( boxDParamButtons, PROPORTION0, wx.EXPAND, BORDER )

        #######################################################################
        # Test Information

        self.divider2 = wx.StaticLine( self, ID, POSITION, SIZE, wx.LI_HORIZONTAL )
        boxCTestParameters.Add( self.divider2, PROPORTION0, wx.EXPAND |wx.ALL, BORDER )

        boxDTextInfo = wx.BoxSizer( wx.VERTICAL )

        self.titleTestInfo = wx.StaticText( self, ID, "Test Infomation", POSITION, SIZE, STYLE )
        self.titleTestInfo.Wrap( WRAP )
        boxDTextInfo.Add( self.titleTestInfo, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        self.divider3 = wx.StaticLine( self, ID, POSITION, SIZE, wx.LI_HORIZONTAL )
        boxDTextInfo.Add( self.divider3, PROPORTION0, wx.EXPAND |wx.ALL, BORDER )

        gridETestInfo = wx.FlexGridSizer( 0, 2, 0, 0 )
        gridETestInfo.SetFlexibleDirection( wx.BOTH )
        gridETestInfo.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        #######################################################################
        # List of Information

        self.labelSelectTest = wx.StaticText( self, ID, "Selected Test", POSITION, SIZE, wx.ALIGN_RIGHT )
        self.labelSelectTest.Wrap( WRAP )
        gridETestInfo.Add( self.labelSelectTest, PROPORTION0, wx.ALL|wx.ALIGN_RIGHT, BORDER )

        self.textSelectTest = wx.StaticText( self, ID, "<get Test>", POSITION, SIZE, STYLE )
        self.textSelectTest.Wrap( WRAP )
        gridETestInfo.Add( self.textSelectTest, PROPORTION0, wx.ALL, BORDER )

        self.labelSelectParams = wx.StaticText( self, ID, "Parameters\nto be\nrecorded", POSITION, SIZE, wx.ALIGN_RIGHT )
        self.labelSelectParams.Wrap( WRAP )
        gridETestInfo.Add( self.labelSelectParams, PROPORTION0, wx.ALL|wx.ALIGN_RIGHT, BORDER )

        self.textSelectParams = wx.StaticText( self, ID, "list of\nparams to\nbe recorded", POSITION, SIZE, STYLE )
        self.textSelectParams.Wrap( WRAP )
        gridETestInfo.Add( self.textSelectParams, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, BORDER )

        self.labelCOMStatus = wx.StaticText( self, ID, "COM Port\nStatus", POSITION, SIZE, wx.ALIGN_RIGHT )
        self.labelCOMStatus.Wrap( WRAP )
        gridETestInfo.Add( self.labelCOMStatus, PROPORTION0, wx.ALL|wx.ALIGN_RIGHT, BORDER )

        self.textCOMStatus = wx.StaticText( self, ID, "<get Status>", POSITION, SIZE, STYLE )
        self.textCOMStatus.Wrap( WRAP )
        gridETestInfo.Add( self.textCOMStatus, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, BORDER )

        self.labelSelectFileName = wx.StaticText( self, ID, "File will be\nsaved as", POSITION, SIZE, wx.ALIGN_RIGHT )
        self.labelSelectFileName.Wrap( WRAP )
        gridETestInfo.Add( self.labelSelectFileName, PROPORTION0, wx.ALL|wx.ALIGN_RIGHT, BORDER )

        self.textSelectFileName = wx.StaticText( self, ID, "<get Name>", POSITION, SIZE, STYLE )
        self.textSelectFileName.Wrap( WRAP )
        gridETestInfo.Add( self.textSelectFileName, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, BORDER )

        boxDTextInfo.Add( gridETestInfo, PROPORTION1, wx.EXPAND, BORDER )

        boxCTestParameters.Add( boxDTextInfo, PROPORTION0, wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        boxBTop.Add( boxCTestParameters, PROPORTION0, wx.EXPAND, BORDER )

        #######################################################################
        # / LEFT SETTINGS
        #######################################################################

        #######################################################################
        #   MIDDLE INFO
        #######################################################################

        boxCInfo = wx.BoxSizer( wx.VERTICAL )

        boxCInfo.SetMinSize( (200,-1) )
        boxDGeneralInfo = wx.BoxSizer( wx.VERTICAL )

        self.titleGeneralInfo = wx.StaticText( self, ID, "General Infomation", POSITION, SIZE, STYLE )
        self.titleGeneralInfo.Wrap( WRAP )
        boxDGeneralInfo.Add( self.titleGeneralInfo, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        self.divider4 = wx.StaticLine( self, ID, POSITION, SIZE, wx.LI_HORIZONTAL )
        boxDGeneralInfo.Add( self.divider4, PROPORTION0, wx.EXPAND |wx.ALL, BORDER )

        #######################################################################
        # Block of text

        self.textGeneralInfo = wx.StaticText( self, ID, ("The entire text goes here. \nWIll be triggered by the \nclick of a text parameter \nor something. \nMay have multiple \nparagraphs. I don't know. "),
                                             wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.textGeneralInfo.Wrap( WRAP )
        boxDGeneralInfo.Add( self.textGeneralInfo, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        #######################################################################
        # Module Listing

        self.textModuleA = wx.StaticText( self, ID, "Module A", POSITION, SIZE, STYLE )
        self.textModuleA.Wrap( WRAP )
        boxDGeneralInfo.Add( self.textModuleA, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        boxCInfo.Add( boxDGeneralInfo, PROPORTION0, wx.EXPAND, BORDER )

        boxBTop.Add( boxCInfo, PROPORTION0, wx.EXPAND, BORDER )

        #######################################################################
        # / MIDDLE INFO
        #######################################################################

        #######################################################################
        #   RIGHT TABS
        #######################################################################

        self.pageCPlot = wx.Notebook( self, ID, POSITION, SIZE, STYLE )
        self.pageCPlot.SetMinSize( ( 800,-1 ) )

        self.tab1 = wx.Panel( self.pageCPlot, ID, POSITION, SIZE, wx.TAB_TRAVERSAL )
        self.bSizer30 = wx.BoxSizer( wx.VERTICAL )

        self.m_bpButton3 = wx.BitmapButton( self.tab1, ID, wx.Bitmap( "graph1.bmp", wx.BITMAP_TYPE_ANY ), POSITION, SIZE, wx.BU_AUTODRAW )
        self.bSizer30.Add( self.m_bpButton3, PROPORTION0, wx.ALL, BORDER )

        self.statixPlaceholder = wx.StaticText( self.tab1, ID, "the plot goes here", POSITION, SIZE, STYLE )
        self.statixPlaceholder.Wrap( WRAP )
        self.bSizer30.Add( self.statixPlaceholder, PROPORTION0, wx.ALL, BORDER )


        self.tab1.SetSizer( self.bSizer30 )
        self.tab1.Layout()
        self.bSizer30.Fit( self.tab1 )
        self.pageCPlot.AddPage( self.tab1, u"Main Tab", False )
        self.m_panel2 = wx.Panel( self.pageCPlot, ID, POSITION, SIZE, wx.TAB_TRAVERSAL )
        self.pageCPlot.AddPage( self.m_panel2, u"Tab 2", True )

        boxBTop.Add( self.pageCPlot, PROPORTION1, wx.EXPAND |wx.ALL, BORDER )

        #######################################################################
        # / RIGHT TABS
        #######################################################################

        #######################################################################
        #
        # / TOP PANE
        #
        #######################################################################

        boxA.Add( boxBTop, PROPORTION1, wx.EXPAND, BORDER)

        #######################################################################
        #
        #   BOTTOM PANE
        #
        #######################################################################

        boxBBottom = wx.BoxSizer( wx.VERTICAL )

        self.divider5 = wx.StaticLine( self, ID, POSITION, SIZE, wx.LI_HORIZONTAL )
        boxBBottom.Add( self.divider5, PROPORTION0, wx.EXPAND|wx.ALL, BORDER )

        self.titleTestCondition = wx.StaticText( self, ID, "Current Test Conditions", POSITION, SIZE, STYLE )
        self.titleTestCondition.Wrap( WRAP )
        boxBBottom.Add( self.titleTestCondition, PROPORTION0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        self.divider6 = wx.StaticLine( self, ID, POSITION, SIZE, wx.LI_HORIZONTAL )
        boxBBottom.Add( self.divider6, PROPORTION0, wx.EXPAND|wx.ALL, BORDER )

        #######################################################################
        # Buttons

        boxCTestStatus = wx.BoxSizer( wx.HORIZONTAL )

        self.buttonRunTest = wx.Button( self, ID, "Start Test", POSITION, SIZE, STYLE)
        boxCTestStatus.Add( self.buttonRunTest, PROPORTION0, wx.ALL|wx.EXPAND, BORDER )

        self.buttonStopTest = wx.Button( self, ID, "Stop Test", POSITION, SIZE, STYLE)
        boxCTestStatus.Add( self.buttonStopTest, PROPORTION0, wx.ALL|wx.EXPAND, BORDER )

        #######################################################################
        # Now running: ~~~

        boxCProgress = wx.BoxSizer( wx.VERTICAL )

        boxDCurrentModule = wx.BoxSizer( wx.HORIZONTAL )

        self.labelCurrentModule = wx.StaticText( self, ID, "Now running module: ", POSITION, SIZE, STYLE )
        self.labelCurrentModule.Wrap( WRAP )
        boxDCurrentModule.Add( self.labelCurrentModule, PROPORTION0, FLAG, BORDER )

        self.testCurrentModule = wx.StaticText( self, ID, "<current module>", POSITION, SIZE, STYLE )
        self.testCurrentModule.Wrap( WRAP )
        boxDCurrentModule.Add( self.testCurrentModule, PROPORTION0, FLAG, BORDER )

        boxCProgress.Add( boxDCurrentModule, PROPORTION0, wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        #######################################################################
        # Time Passed: ~~~

        boxDCurrentTime = wx.BoxSizer( wx.HORIZONTAL )

        self.labelCurrentTime = wx.StaticText( self, ID, "Time Passed: ", POSITION, SIZE, STYLE )
        self.labelCurrentTime.Wrap( WRAP )
        boxDCurrentTime.Add( self.labelCurrentTime, PROPORTION0, FLAG, BORDER )

        self.testCurrentModule1 = wx.StaticText( self, ID, "<start time - current time>", POSITION, SIZE, STYLE )
        self.testCurrentModule1.Wrap( WRAP )
        boxDCurrentTime.Add( self.testCurrentModule1, PROPORTION0, FLAG, BORDER )

        boxCProgress.Add( boxDCurrentTime, PROPORTION0, wx.ALIGN_CENTER_HORIZONTAL, BORDER )

        #######################################################################
        # Progress Bar

        self.progressGauge = wx.Gauge( self, ID, self.gaugeRange, POSITION, SIZE, wx.GA_HORIZONTAL )
        self.progressGauge.SetValue( 0 )
        boxCProgress.Add( self.progressGauge, PROPORTION0, wx.ALL|wx.EXPAND, BORDER )

        #######################################################################

        boxCTestStatus.Add( boxCProgress, PROPORTION1, wx.EXPAND, BORDER )

        boxBBottom.Add( boxCTestStatus, PROPORTION1, wx.EXPAND, BORDER)

        #######################################################################
        #
        # / BOTTOM PANE
        #
        #######################################################################

        boxA.Add (boxBBottom, PROPORTION0, wx.EXPAND, BORDER)

        self.SetSizer( boxA )

    def updateSettings(self, model):
        self.textSelectTest.SetLabel( model.testSchedule )
        self.textSelectParams.SetLabel( str(model.testParams) )
        self.textCOMStatus.SetLabel( model.COMPort )
        self.textSelectFileName.SetLabel( model.fileName )

    def addTestScheduleHandler(self, handler):
        self.choiceSchedule.Bind( wx.EVT_CHOICE, handler )

    def addXRecordHandler(self, handler):
        self.checkJoyX.Bind( wx.EVT_CHECKBOX, handler )

    def addYRecordHandler(self, handler):
        self.checkJoyY.Bind( wx.EVT_CHECKBOX, handler )

    def addRotorTRecordHandler(self, handler):
        self.checkRotorTemp.Bind( wx.EVT_CHECKBOX, handler )

    def addCalipTRecordHandler(self, handler):
        self.checkCalipTemp.Bind( wx.EVT_CHECKBOX, handler )

    def addMotorRecordHandler(self, handler):
        self.checkMotorSpeed.Bind( wx.EVT_CHECKBOX, handler )

    def addCOMPortHandler(self, handler):
        self.entryCOMPort.Bind( wx.EVT_TEXT, handler )
        self.entryCOMPort.Bind( wx.EVT_TEXT_ENTER, handler )

    def addFileNameHandler(self, handler):
        self.entryFileName.Bind( wx.EVT_TEXT, handler )
        self.entryFileName.Bind( wx.EVT_TEXT_ENTER, handler )

    def addApplySettingsHandler(self, handler):
        self.buttonApply.Bind( wx.EVT_BUTTON, handler )

    def addDefaultSettingsHandler(self, handler):
        self.buttonDefault.Bind( wx.EVT_BUTTON, handler )

    def addStartTestHandler(self, handler):
        self.buttonRunTest.Bind( wx.EVT_BUTTON, handler )

    def addStopTestHander(self, handler):
        self.buttonStopTest.Bind( wx.EVT_BUTTON, handler )

    def addToPanel(self, canvas):
        self.bSizer30.Add(canvas)
        self.Fit()










