# -*- coding: utf-8 -*-
"""
Class for plotting
"""

import wx
import wx.xrc
import wx.adv
import wx.lib.plot as wxplot

class MainPanel(wx.Panel):
    def __init__(self, parent):
        """
        Initialises the main GUI frame for all user interation and event
        handling. Split into the: 
        - top left settings pane 
        - top right tab windows 
        - bottom test conditions pane

        Parameters
        ----------
        parent : Frame
            a parent frame in which to initialise in. Usually 'None'.
        title : string
            a title for the window.
        """
        super().__init__(parent)

        # Formatting constants
        RIGHT = wx.ALIGN_RIGHT
        CEN_H = wx.ALIGN_CENTER_HORIZONTAL
        CEN_V = wx.ALIGN_CENTER_VERTICAL
        EXP = wx.EXPAND
        EMPTY = wx.EmptyString
        FLAG = wx.ALL
        BORDER = 5
        PROP0 = 0 # Proportion = 0
        PROP1 = 1 # Proportion = 1

        # Other Constants
        self.scheduleList = [
            "Joystick", 
            "Schedule A", 
            "Schedule B", 
            "Schedule C", 
        ]
        self.plot_tabs = {}
        self.gaugeRange = 100

        boxA = wx.BoxSizer( wx.VERTICAL )

        #######################################################################
        #
        #   TOP PANE
        #
        #######################################################################

        #######################################################################
        # LEFT SETTINGS
        #######################################################################

        self.boxBTop = wx.BoxSizer( wx.HORIZONTAL )

        boxCTestParameters = wx.BoxSizer( wx.VERTICAL )

        self.titleParameters = wx.StaticText( self, label="Test Settings and Parameters")
        self.divider1 = wx.StaticLine( self, style=wx.LI_HORIZONTAL )

        boxCTestParameters.Add( self.titleParameters, PROP0, wx.ALL|CEN_H, BORDER )
        boxCTestParameters.Add( self.divider1, PROP0, EXP |wx.ALL, BORDER )

        #######################################################################
        # List of test settings

        gridDTestParameters = wx.FlexGridSizer( 0, 2, 0, 0 )
        gridDTestParameters.SetFlexibleDirection( wx.BOTH )
        gridDTestParameters.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        #######################################################################
        # Test Schedule Chooser

        self.labelSchedule = wx.StaticText( self, label="Schedule", style=RIGHT )
        self.choiceSchedule = wx.Choice( self, choices=self.scheduleList)
        self.choiceSchedule.SetSelection( 0 )

        #######################################################################
        # Choose which parameters to record

        self.labelRecording = wx.StaticText( self, label="Parameter\nRecording", style=RIGHT )

        self.scrollEWinParam = wx.ScrolledWindow( self, style=wx.HSCROLL|wx.VSCROLL )
        self.scrollEWinParam.SetScrollRate( 5, 5 )
        self.scrollEWinParam.SetMinSize( ( -1,150 ) )

        boxFParamChoices = wx.BoxSizer( wx.VERTICAL )

        #######################################################################
        # Checkbox list of parameters

        self.checkJoyX = wx.CheckBox( self.scrollEWinParam, id=1, label="X-Position")
        self.checkJoyY = wx.CheckBox( self.scrollEWinParam, id=2, label="Y-Position")
        self.checkRotorTemp = wx.CheckBox( self.scrollEWinParam, id=3, label="Rotor Temp")
        self.checkCalipTemp = wx.CheckBox( self.scrollEWinParam, id=4, label="Caliper Temp")
        self.checkMotorSpeed = wx.CheckBox( self.scrollEWinParam, id=5, label="Motor Speed")
        
        self.checkJoyX.SetValue(True)
        self.checkJoyY.SetValue(True)

        boxFParamChoices.Add( self.checkJoyX, PROP0, FLAG, BORDER )
        boxFParamChoices.Add( self.checkJoyY, PROP0, FLAG, BORDER )
        boxFParamChoices.Add( self.checkRotorTemp, PROP0, FLAG, BORDER )
        boxFParamChoices.Add( self.checkCalipTemp, PROP0, FLAG, BORDER )
        boxFParamChoices.Add( self.checkMotorSpeed, PROP0, FLAG, BORDER )

        self.scrollEWinParam.SetSizer( boxFParamChoices )
        self.scrollEWinParam.Layout()
        boxFParamChoices.Fit( self.scrollEWinParam )

        #######################################################################
        # Choose Serial Port to read / write

        self.labelCOMPort = wx.StaticText( self, label="COM Port", style=RIGHT )
        self.entryCOMPort = wx.TextCtrl( self, style=wx.TE_PROCESS_ENTER|wx.TE_RIGHT )

        #######################################################################
        # Enter custom csv filename

        self.labelFileName = wx.StaticText( self, label="File Name\n(optional)", style=RIGHT )

        boxEFileName = wx.BoxSizer( wx.HORIZONTAL )

        self.entryFileName = wx.TextCtrl( self, value=wx.EmptyString, style=wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
        self.labelFileExtension = wx.StaticText( self, label=".csv")

        boxEFileName.Add( self.entryFileName, PROP0, wx.ALL|CEN_V, BORDER )
        boxEFileName.Add( self.labelFileExtension, PROP0, wx.ALL|CEN_V, BORDER )

        gridDTestParameters.Add( self.labelSchedule, PROP0, wx.ALL|CEN_V|RIGHT, BORDER )
        gridDTestParameters.Add( self.choiceSchedule, PROP0, wx.ALL|CEN_V, BORDER )
        gridDTestParameters.Add( self.labelRecording, PROP0, wx.ALL|RIGHT, BORDER )
        gridDTestParameters.Add( self.scrollEWinParam, PROP1, EXP|wx.ALL|CEN_V, BORDER )
        gridDTestParameters.Add( self.labelCOMPort, PROP0, wx.ALL|RIGHT|CEN_V, BORDER )
        gridDTestParameters.Add( self.entryCOMPort, PROP0, wx.ALL|CEN_V, BORDER )
        gridDTestParameters.Add( self.labelFileName, PROP0, wx.ALL|CEN_V|RIGHT, BORDER )
        gridDTestParameters.Add( boxEFileName, PROP1, EXP|CEN_V, BORDER )

        boxCTestParameters.Add( gridDTestParameters, PROP1, CEN_H, BORDER )

        #######################################################################
        # Apply / Reset settings

        boxDParamButtons = wx.BoxSizer( wx.HORIZONTAL )

        self.buttonApply = wx.Button( self, label="Apply")
        self.buttonDefault = wx.Button( self, label="Default")

        boxDParamButtons.Add( self.buttonApply, PROP1, wx.ALL|CEN_V, BORDER )
        boxDParamButtons.Add( self.buttonDefault, PROP1, wx.ALL|CEN_V, BORDER )

        boxCTestParameters.Add( boxDParamButtons, PROP0, EXP, BORDER )

        #######################################################################
        # Test Information

        self.divider2 = wx.StaticLine( self, style=wx.LI_HORIZONTAL )
        boxCTestParameters.Add( self.divider2, PROP0, EXP |wx.ALL, BORDER )

        boxDTextInfo = wx.BoxSizer( wx.VERTICAL )

        self.titleTestInfo = wx.StaticText( self, label="Test Infomation")
        self.divider3 = wx.StaticLine( self, style=wx.LI_HORIZONTAL )

        boxDTextInfo.Add( self.titleTestInfo, PROP0, wx.ALL|CEN_H, BORDER )
        boxDTextInfo.Add( self.divider3, PROP0, EXP |wx.ALL, BORDER )

        gridETestInfo = wx.FlexGridSizer( 0, 2, 0, 0 )
        gridETestInfo.SetFlexibleDirection( wx.BOTH )
        gridETestInfo.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        #######################################################################
        # List of Information

        self.labelSelectTest = wx.StaticText( self, label="Selected Test", style=RIGHT )
        self.textSelectTest = wx.StaticText( self, label="No Test\nSelected")
        self.labelSelectParams = wx.StaticText( self, label="Parameters\nto be\nrecorded", style=RIGHT )
        self.textSelectParams = wx.StaticText( self, label="None Selected")
        self.labelCOMName = wx.StaticText( self, label="COM Port", style=RIGHT )
        self.textCOMName = wx.StaticText( self, label="No Name")

        self.labelCOMStatus = wx.StaticText( self, label="COM Status", style=RIGHT )
        self.textCOMStatus = wx.StaticText( self, label="No Status")

        self.labelSelectFileName = wx.StaticText( self, label="File will be\nsaved as", style=RIGHT )
        self.textSelectFileName = wx.StaticText( self, label="<enter default>")

        gridETestInfo.Add( self.labelSelectTest, PROP0, wx.ALL|RIGHT, BORDER )
        gridETestInfo.Add( self.textSelectTest, PROP0, wx.ALL, BORDER )
        gridETestInfo.Add( self.labelSelectParams, PROP0, wx.ALL|RIGHT, BORDER )
        gridETestInfo.Add( self.textSelectParams, PROP0, wx.ALL|CEN_V, BORDER )
        gridETestInfo.Add( self.labelCOMName, PROP0, wx.ALL|RIGHT, BORDER )
        gridETestInfo.Add( self.textCOMName, PROP0, wx.ALL|CEN_V, BORDER )
        gridETestInfo.Add( self.labelCOMStatus, PROP0, wx.ALL|RIGHT, BORDER )
        gridETestInfo.Add( self.textCOMStatus, PROP0, wx.ALL|CEN_V, BORDER )
        gridETestInfo.Add( self.labelSelectFileName, PROP0, wx.ALL|RIGHT, BORDER )
        gridETestInfo.Add( self.textSelectFileName, PROP0, wx.ALL|CEN_V, BORDER )

        boxDTextInfo.Add( gridETestInfo, PROP1, EXP, BORDER )

        boxCTestParameters.Add( boxDTextInfo, PROP0, CEN_H, BORDER )

        self.boxBTop.Add( boxCTestParameters, PROP0, EXP, BORDER )

        #######################################################################
        # / LEFT SETTINGS
        #######################################################################

        #######################################################################
        #   RIGHT TABS
        #######################################################################

        self.pageCPlot = wx.Notebook( self)
        self.pageCPlot.SetMinSize( ( 800,-1 ) )

        # #######################################################################
        # Main Home Tab

        self.tab1 = wx.Panel( self.pageCPlot, style=wx.TAB_TRAVERSAL )
        self.boxDTab1 = wx.BoxSizer( wx.VERTICAL )

        self.bitmapUQR = wx.StaticBitmap( self.tab1, bitmap=wx.Bitmap( "images/uqr_logo.bmp", wx.BITMAP_TYPE_ANY ))
        self.staticPlaceholder = wx.StaticText( self.tab1, label="placeholder")

        self.boxDTab1.Add( self.bitmapUQR, PROP0, wx.ALL|CEN_H, BORDER )
        self.boxDTab1.Add( self.staticPlaceholder, PROP0, wx.ALL|CEN_H, BORDER )

        self.tab1.SetSizer( self.boxDTab1 )
        self.tab1.Layout()
        self.boxDTab1.Fit( self.tab1 )
        self.pageCPlot.AddPage( self.tab1, "Home Tab", False )

        # #######################################################################
        # Schedule Information Tab

        self.tab2 = wx.Panel( self.pageCPlot, style=wx.TAB_TRAVERSAL )
        self.boxDTab2 = wx.BoxSizer( wx.VERTICAL )

        self.titleGeneralInfo = wx.StaticText( self.tab2, label="Test Schedule Infomation")
        self.divider4 = wx.StaticLine( self.tab2, style=wx.LI_HORIZONTAL )
        self.textGeneralInfo = wx.StaticText( self.tab2, label=(
            """The entire text goes here. \nWIll be triggered by the \nclick of a text parameter 
            \nor something. \nMay have multiple \nparagraphs. I don't know. """
            ), style=wx.ALIGN_CENTRE )
        self.bitmapGraph = wx.StaticBitmap( self.tab2, bitmap=wx.Bitmap( "images/graph1.bmp", wx.BITMAP_TYPE_ANY ))

        self.boxDTab2.Add( self.titleGeneralInfo, PROP0, wx.ALL|CEN_H, BORDER )
        self.boxDTab2.Add( self.divider4, PROP0, EXP |wx.ALL, BORDER )
        self.boxDTab2.Add( self.textGeneralInfo, PROP0, wx.ALL|CEN_H, BORDER )
        self.boxDTab2.Add( self.bitmapGraph, PROP0, wx.ALL|CEN_H, BORDER )

        self.tab2.SetSizer( self.boxDTab2 )
        self.tab2.Layout()
        self.boxDTab2.Fit( self.tab2 )
        self.pageCPlot.AddPage( self.tab2, "Schedule Information", False )

        # #######################################################################
        # Plot Tab
        # self.tab3 = wxplot.PlotCanvas(self.pageCPlot)

        # self.tab3.Draw(self.draw1Objects())

        # #self.tab3.SetSizer( self.boxDTab2 )
        # self.tab3.Layout()
        # self.boxDTab2.Fit( self.tab3 )
        # self.pageCPlot.AddPage( self.tab3, "X_Y_Plot", True )

        self.boxBTop.Add( self.pageCPlot, PROP1, EXP |wx.ALL, BORDER )

        #######################################################################
        # / RIGHT TABS
        #######################################################################

        #######################################################################
        #
        # / TOP PANE
        #
        #######################################################################

        boxA.Add( self.boxBTop, PROP1, EXP, BORDER)

        #######################################################################
        #
        #   BOTTOM PANE
        #
        #######################################################################

        boxBBottom = wx.BoxSizer( wx.VERTICAL )

        self.divider5 = wx.StaticLine( self, style=wx.LI_HORIZONTAL )
        self.titleTestCondition = wx.StaticText( self, label="Current Test Conditions")
        self.divider6 = wx.StaticLine( self, style=wx.LI_HORIZONTAL )

        boxBBottom.Add( self.divider5, PROP0, EXP|wx.ALL, BORDER )
        boxBBottom.Add( self.titleTestCondition, PROP0, wx.ALL|CEN_H, BORDER )
        boxBBottom.Add( self.divider6, PROP0, EXP|wx.ALL, BORDER )

        #######################################################################
        # Buttons

        boxCTestStatus = wx.BoxSizer( wx.HORIZONTAL )

        self.buttonRunTest = wx.Button( self, label="Start Test")
        self.buttonStopTest = wx.Button( self, label="Stop Test")

        boxCTestStatus.Add( self.buttonRunTest, PROP0, wx.ALL|EXP, BORDER )
        boxCTestStatus.Add( self.buttonStopTest, PROP0, wx.ALL|EXP, BORDER )

        #######################################################################
        # Now running: ~~~

        boxCProgress = wx.BoxSizer( wx.VERTICAL )

        boxDCurrentModule = wx.BoxSizer( wx.HORIZONTAL )

        self.labelCurrentModule = wx.StaticText( self, label="Now running Schedule: ")
        self.textCurrentModule = wx.StaticText( self, label="No Schedule Selected")

        boxDCurrentModule.Add( self.labelCurrentModule, PROP0, FLAG, BORDER )
        boxDCurrentModule.Add( self.textCurrentModule, PROP0, FLAG, BORDER )

        boxCProgress.Add( boxDCurrentModule, PROP0, CEN_H, BORDER )

        #######################################################################
        # Time Passed: ~~~

        boxDCurrentTime = wx.BoxSizer( wx.HORIZONTAL )

        self.labelCurrentTime = wx.StaticText( self, label="Time Passed: ")
        self.testCurrentTime = wx.StaticText( self, label="No test running")

        boxDCurrentTime.Add( self.labelCurrentTime, PROP0, FLAG, BORDER )
        boxDCurrentTime.Add( self.testCurrentTime, PROP0, FLAG, BORDER )

        boxCProgress.Add( boxDCurrentTime, PROP0, CEN_H, BORDER )

        #######################################################################
        # Module Progress Bar

        self.moduleGauge = wx.Gauge( self, range=self.gaugeRange, style=wx.GA_HORIZONTAL )
        self.moduleGauge.SetValue( 0 )
        boxCProgress.Add( self.moduleGauge, PROP0, wx.ALL|EXP, BORDER )

        #######################################################################
        # Total Progress Bar

        self.progressGauge = wx.Gauge( self, range=self.gaugeRange, style=wx.GA_HORIZONTAL )
        self.progressGauge.SetValue( 0 )
        boxCProgress.Add( self.progressGauge, PROP0, wx.ALL|EXP, BORDER )

        boxCTestStatus.Add( boxCProgress, PROP1, EXP, BORDER )

        boxBBottom.Add( boxCTestStatus, PROP1, EXP, BORDER)

        #######################################################################
        #
        # / BOTTOM PANE
        #
        #######################################################################

        boxA.Add (boxBBottom, PROP0, EXP, BORDER)

        self.SetSizer( boxA )

    def updateSettings(self, model):
        """Updates selected labels once settings are applied. 

        Parameters
        ----------
        model : Model object
            object that stores the settings
        """

        self.textSelectTest.SetLabel( model.testParameters['testSchedule'] )
        # self.textSelectParams.SetLabel( str(model.testParameters['testParams']) )
        self.textSelectParams.SetLabel( '\n'.join(model.testParameters['testParams'])  )
        self.textCOMName.SetLabel( model.testParameters['COMPort'] )
        self.textCOMStatus.SetLabel( str(model.testParameters['COMStatus']) )
        self.textSelectFileName.SetLabel( model.testParameters['fileName'] )

        self.textCurrentModule.SetLabel( model.testParameters['testSchedule'] )
        self.updateScheduleInfo(model)

    def updateTotalConditions(self, time, stopped=False):
        """Updates the label and gauge that shows test progress. 

        Parameters
        ----------
        time : float
            current time since test started
        """
        self.progressGauge.SetValue( time )
        self.testCurrentTime.SetLabel( f"{time:.2f} seconds" )
        if stopped: 
            self.testCurrentTime.SetLabel( f"Test stopped at {time:.2f} seconds" )

    def updateModuleConditions(self, time, module):
        """Updates the label and gauge that shows test progress. 

        Parameters
        ----------
        time : float
            current time since test started
        """
        self.moduleGauge.SetValue( time )

        self.textCurrentModule.SetLabel( module )
            

    def updateScheduleInfo(self, model):
        """Updates the infomation on the schedule info tab. 

        Parameters
        ----------
        model : Model object
            stores the currently selected schedule
        """
        schedule = model.testParameters['testSchedule']
        if schedule == self.scheduleList[0]:
            textBlock = ("A testing schedule with a joystick as an analog input.\n"
                         "The test lasts 20 seconds or until the stop button\n"
                         "is pressed.")
        elif schedule == self.scheduleList[1]:
            textBlock = ("The proposed Schedule A for the testign for brake squeal.\n"
                         "I've no clue how in implement this yet. ")
        elif schedule == self.scheduleList[2]:
            textBlock = ("The proposed Schedule B for the testign for brake squeal.\n"
                         "I've no clue how in implement this yet. ")
        elif schedule == self.scheduleList[3]:
            textBlock = ("The proposed Schedule C for the testign for brake squeal.\n"
                         "I've no clue how in implement this yet. ")
        else:
            textBlock = "No Schedule Selected"

        self.textGeneralInfo.SetLabel(textBlock)

    def addTestScheduleHandler(self, handler):
        self.choiceSchedule.Bind( wx.EVT_CHOICE, handler )

    def addParamRecordHandler(self, handler):
        self.checkJoyX.Bind( wx.EVT_CHECKBOX, handler )
        self.checkJoyY.Bind( wx.EVT_CHECKBOX, handler )
        self.checkRotorTemp.Bind( wx.EVT_CHECKBOX, handler )
        self.checkCalipTemp.Bind( wx.EVT_CHECKBOX, handler )
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

    def drawPlot(self, title, plotGraphics, select=False): 
        if title not in self.plot_tabs: 
            self.plot_tabs[title] = wxplot.PlotCanvas(self.pageCPlot)
            self.pageCPlot.AddPage( self.plot_tabs[title], title, select )

        self.plot_tabs[title].Draw(plotGraphics)
    
    def updatePlot(self, title, plotGraphics): 

        self.plot_tabs[title].Draw(plotGraphics)

    











