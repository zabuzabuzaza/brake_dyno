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
        PROP0 = 0 # does not expand
        PROP1 = 1 # does expand

        # Other Constants
        self.scheduleList = [
            "Joystick", 
            "Schedule A", 
            "Schedule B", 
            "Schedule C", 
            "Constant Speed", 
            "Torque Control", 
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

        boxBTop = wx.BoxSizer( wx.HORIZONTAL )

        boxCTestParameters = wx.BoxSizer( wx.VERTICAL )

        titleParameters = wx.StaticText( self, label="Test Settings and Parameters")
        divider1 = wx.StaticLine( self, style=wx.LI_HORIZONTAL )

        boxCTestParameters.Add( titleParameters, PROP0, wx.ALL|CEN_H, BORDER )
        boxCTestParameters.Add( divider1, PROP0, EXP |wx.ALL, BORDER )

        #######################################################################
        # List of test settings

        gridDTestParameters = wx.FlexGridSizer( 0, 2, 0, 0 )
        gridDTestParameters.SetFlexibleDirection( wx.BOTH )
        gridDTestParameters.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        #######################################################################
        # Test Schedule Chooser

        labelSchedule = wx.StaticText( self, label="Schedule", style=RIGHT )
        self.choiceSchedule = wx.Choice( self, choices=self.scheduleList)
        self.choiceSchedule.SetSelection( 4 )

        #######################################################################
        # Choose Serial Port to read / write

        labelCOMIn = wx.StaticText( self, label="Data Acq\nCOM Port", style=RIGHT )
        self.entryCOMIn = wx.TextCtrl( self, style=wx.TE_PROCESS_ENTER|wx.TE_RIGHT )

        labelCOMOut = wx.StaticText( self, label="Control Sys\nCOM Port", style=RIGHT )
        self.entryCOMOut = wx.TextCtrl( self, style=wx.TE_PROCESS_ENTER|wx.TE_RIGHT )

        #######################################################################
        # Enter custom csv filename

        labelFileName = wx.StaticText( self, label="Folder Name\n(optional)", style=RIGHT )

        boxEFileName = wx.BoxSizer( wx.HORIZONTAL )

        self.entryFileName = wx.TextCtrl( self, value=wx.EmptyString, style=wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
        labelFileExtension = wx.StaticText( self, label="")

        boxEFileName.Add( self.entryFileName, PROP0, wx.ALL|CEN_V, BORDER )
        boxEFileName.Add( labelFileExtension, PROP0, wx.ALL|CEN_V, BORDER )

        gridDTestParameters.Add( labelSchedule, PROP0, wx.ALL|CEN_V|RIGHT, BORDER )
        gridDTestParameters.Add( self.choiceSchedule, PROP0, wx.ALL|CEN_V, BORDER )
        gridDTestParameters.Add( labelCOMIn, PROP0, wx.ALL|RIGHT|CEN_V, BORDER )
        gridDTestParameters.Add( self.entryCOMIn, PROP0, wx.ALL|CEN_V, BORDER )
        gridDTestParameters.Add( labelCOMOut, PROP0, wx.ALL|RIGHT|CEN_V, BORDER )
        gridDTestParameters.Add( self.entryCOMOut, PROP0, wx.ALL|CEN_V, BORDER )
        gridDTestParameters.Add( labelFileName, PROP0, wx.ALL|CEN_V|RIGHT, BORDER )
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

        divider2 = wx.StaticLine( self, style=wx.LI_HORIZONTAL )
        boxCTestParameters.Add( divider2, PROP0, EXP |wx.ALL, BORDER )

        boxDTextInfo = wx.BoxSizer( wx.VERTICAL )

        titleTestInfo = wx.StaticText( self, label="Test Infomation")
        divider3 = wx.StaticLine( self, style=wx.LI_HORIZONTAL )

        boxDTextInfo.Add( titleTestInfo, PROP0, wx.ALL|CEN_H, BORDER )
        boxDTextInfo.Add( divider3, PROP0, EXP |wx.ALL, BORDER )

        gridETestInfo = wx.FlexGridSizer( 0, 2, 0, 0 )
        gridETestInfo.SetFlexibleDirection( wx.BOTH )
        gridETestInfo.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        #######################################################################
        # List of Information

        labelSelectTest = wx.StaticText( self, label="Selected Test", style=RIGHT )
        self.textSelectTest = wx.StaticText( self, label="No Test\nSelected")
        labelCOMName = wx.StaticText( self, label="COM Port", style=RIGHT )
        self.textCOMName = wx.StaticText( self, label="No Name")

        labelCOMStatus = wx.StaticText( self, label="COM Status", style=RIGHT )
        self.textCOMStatus = wx.StaticText( self, label="No Status")

        labelSelectFileName = wx.StaticText( self, label="Files will be\nsaved in", style=RIGHT )
        self.textSelectFileName = wx.StaticText( self, label="<enter default>")

        gridETestInfo.Add( labelSelectTest, PROP0, wx.ALL|RIGHT, BORDER )
        gridETestInfo.Add( self.textSelectTest, PROP0, wx.ALL, BORDER )
        gridETestInfo.Add( labelCOMName, PROP0, wx.ALL|RIGHT, BORDER )
        gridETestInfo.Add( self.textCOMName, PROP0, wx.ALL|CEN_V, BORDER )
        gridETestInfo.Add( labelCOMStatus, PROP0, wx.ALL|RIGHT, BORDER )
        gridETestInfo.Add( self.textCOMStatus, PROP0, wx.ALL|CEN_V, BORDER )
        gridETestInfo.Add( labelSelectFileName, PROP0, wx.ALL|RIGHT, BORDER )
        gridETestInfo.Add( self.textSelectFileName, PROP0, wx.ALL|CEN_V, BORDER )

        boxDTextInfo.Add( gridETestInfo, PROP1, EXP, BORDER )
        boxCTestParameters.Add( boxDTextInfo, PROP0, CEN_H, BORDER )

        boxBTop.Add( boxCTestParameters, PROP0, EXP, BORDER )

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

        tab1 = wx.Panel( self.pageCPlot, style=wx.TAB_TRAVERSAL )
        boxDTab1 = wx.BoxSizer( wx.VERTICAL )

        bitmapUQR = wx.StaticBitmap( tab1, bitmap=wx.Bitmap( "images/uqr_logo.bmp", wx.BITMAP_TYPE_ANY ))
        staticPlaceholder = wx.StaticText(
            tab1, 
            label="""
                Requires an Arduino with the analog_in.ino and the required inputs for logging.\n
                For now, the test will run without any logging, as the program will be 
                    spitting out pressure values that will hopefully be sent to the brakes. \n
                The pressure tab is what i have for now in terms of programming the pressure profiles.
            """
        )
        labelLink = wx.TextCtrl(tab1, value = "For more info, https://github.com/zabuzabuzaza/brake_dyno", style = wx.TE_READONLY|wx.TE_CENTER) 
        
        boxDTab1.Add( bitmapUQR, PROP0, wx.ALL|CEN_H, BORDER )
        boxDTab1.Add( staticPlaceholder, PROP1, wx.ALL|CEN_H, BORDER )
        boxDTab1.Add( labelLink, PROP0, wx.ALL|wx.EXPAND, BORDER )

        tab1.SetSizer( boxDTab1 )
        tab1.Layout()
        boxDTab1.Fit( tab1 )
        self.pageCPlot.AddPage( tab1, "Home Tab", False )

        # #######################################################################
        # Schedule Information Tab

        self.tab2 = wx.ScrolledWindow( self.pageCPlot, style=wx.HSCROLL|wx.VSCROLL )
        self.tab2.SetScrollRate( 5, 5 )
        self.boxDTab2 = wx.BoxSizer( wx.VERTICAL )

        titleGeneralInfo = wx.StaticText( self.tab2, label="Test Schedule Infomation")
        divider4 = wx.StaticLine( self.tab2, style=wx.LI_HORIZONTAL )
        self.textGeneralInfo = wx.StaticText( self.tab2, label=(
            """The entire text goes here. \nWIll be triggered by the \nclick of a text parameter 
            \nor something. \nMay have multiple \nparagraphs. I don't know. """
            ), style=wx.ALIGN_CENTRE )
        self.bitmapGraph1 = wx.StaticBitmap( self.tab2, bitmap=wx.Bitmap( "images/speed.bmp", wx.BITMAP_TYPE_ANY ))

        self.boxDTab2.Add( titleGeneralInfo, PROP0, wx.ALL|CEN_H, BORDER )
        self.boxDTab2.Add( divider4, PROP0, EXP |wx.ALL, BORDER )
        self.boxDTab2.Add( self.textGeneralInfo, PROP0, wx.ALL|CEN_H, BORDER )
        self.boxDTab2.Add( self.bitmapGraph1, PROP0, wx.ALL|CEN_H, BORDER )
        
        self.tab2.SetSizer( self.boxDTab2 )
        self.tab2.Layout()
        self.boxDTab2.Fit( self.tab2 )
        self.pageCPlot.AddPage( self.tab2, "Schedule Information", False )

        boxBTop.Add( self.pageCPlot, PROP1, EXP |wx.ALL, BORDER )

        #######################################################################
        # / RIGHT TABS
        #######################################################################

        #######################################################################
        #
        # / TOP PANE
        #
        #######################################################################

        boxA.Add( boxBTop, PROP1, EXP, BORDER)

        #######################################################################
        #
        #   BOTTOM PANE
        #
        #######################################################################

        boxBBottom = wx.BoxSizer( wx.VERTICAL )

        divider5 = wx.StaticLine( self, style=wx.LI_HORIZONTAL )
        titleTestCondition = wx.StaticText( self, label="Current Test Conditions")
        divider6 = wx.StaticLine( self, style=wx.LI_HORIZONTAL )

        boxBBottom.Add( divider5, PROP0, EXP|wx.ALL, BORDER )
        boxBBottom.Add( titleTestCondition, PROP0, wx.ALL|CEN_H, BORDER )
        boxBBottom.Add( divider6, PROP0, EXP|wx.ALL, BORDER )

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

        labelCurrentModule = wx.StaticText( self, label="Now running Schedule: ")
        self.textCurrentModule = wx.StaticText( self, label="No Schedule Selected")

        boxDCurrentModule.Add( labelCurrentModule, PROP0, FLAG, BORDER )
        boxDCurrentModule.Add( self.textCurrentModule, PROP0, FLAG, BORDER )

        boxCProgress.Add( boxDCurrentModule, PROP0, CEN_H, BORDER )

        #######################################################################
        # Time Passed: ~~~

        boxDCurrentTime = wx.BoxSizer( wx.HORIZONTAL )

        labelCurrentTime = wx.StaticText( self, label="Time Passed: ")
        self.testCurrentTime = wx.StaticText( self, label="No test running")

        boxDCurrentTime.Add( labelCurrentTime, PROP0, FLAG, BORDER )
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

    def updateSettings(self, model, schedule):
        """Updates selected labels once settings are applied. 

        Parameters
        ----------
        model : Model object
            object that stores the settings
        """

        self.textSelectTest.SetLabel( model.testParameters['testSchedule'] )
        self.textCOMName.SetLabel( model.testParameters['COMPort'] )
        self.textCOMStatus.SetLabel( str(model.testParameters['COMStatus']) )
        self.textSelectFileName.SetLabel( model.testParameters['fileName'] )

        self.textCurrentModule.SetLabel( model.testParameters['testSchedule'] )
        self.updateScheduleInfo(model ,schedule)

    def updateTotalConditions(self, time, total, test, stopped=False):
        """Updates the label and gauge that shows test progress. 

        Parameters
        ----------
        time : float
            current time since test started
        """
        self.progressGauge.SetValue( test )
        self.testCurrentTime.SetLabel( f"{time:.2f} seconds passed (Test #{test} out of {total} tests)" )

        if stopped: 
            self.testCurrentTime.SetLabel( f"Test stopped at {time:.2f} seconds" )

    def updateModuleConditions(self, pressure_tests, temp_tests, module_name):
        """Updates the label and gauge that shows test progress. 

        Parameters
        ----------
        time : float
            current time since test started
        """
        self.moduleGauge.SetValue( temp_tests[0] )
        self.textCurrentModule.SetLabel(f"{module_name} (Temp #{temp_tests[0]} of {temp_tests[1]})(Pressure #{pressure_tests[0]} of {pressure_tests[1]})")
            

    def updateScheduleInfo(self, model, schedule):
        """Updates the infomation on the schedule info tab. 

        Parameters
        ----------
        model : Model object
            stores the currently selected schedule
        """
        schedule_name = model.testParameters['testSchedule']
        self.bitmapGraph1.Hide()

        if schedule_name == self.scheduleList[0]:
            textBlock = ("A testing schedule with a joystick as an analog input.\n"
                         f"The Module list is {schedule.scheduleOrders[schedule_name]}")
            self.bitmapGraph = wx.StaticBitmap( self.tab2, bitmap=wx.Bitmap( "images/empty.bmp", wx.BITMAP_TYPE_ANY ))
        elif schedule_name == self.scheduleList[1]:
            textBlock = ("The proposed Schedule A for the testing for brake squeal.\n"
                         "This is the first part of the test schedules from SAE-J2521"
                         f"The Module list is {schedule.scheduleOrders[schedule_name]}")
            self.bitmapGraph = wx.StaticBitmap( self.tab2, bitmap=wx.Bitmap( "images/empty.bmp", wx.BITMAP_TYPE_ANY ))
        elif schedule_name == self.scheduleList[2]:
            textBlock = ("The proposed Schedule B for the testing for brake squeal.\n"
                         "For now, this is the same as Schedule A"
                         f"The Module list is {schedule.scheduleOrders[schedule_name]}")
            self.bitmapGraph = wx.StaticBitmap( self.tab2, bitmap=wx.Bitmap( "images/empty.bmp", wx.BITMAP_TYPE_ANY ))
        elif schedule_name == self.scheduleList[3]:
            textBlock = ("The proposed Schedule C for the testing for brake squeal.\n"
                         "For now, this is the same as Schedule A"
                         f"The Module list is {schedule.scheduleOrders[schedule_name]}")
            self.bitmapGraph = wx.StaticBitmap( self.tab2, bitmap=wx.Bitmap( "images/empty.bmp", wx.BITMAP_TYPE_ANY ))
        elif schedule_name == self.scheduleList[4]:
            textBlock = ("A Constant Speed test schedule for the testing for brake fade.\n"
                         "In this schedule, the brakes will be applied for a given \n"
                         "pressure and duration. The motor speed will be held constant \n"
                         "during this time. \n"
                         f"Base Speeds are {schedule.moduleList[-2][1]} km\h \n"
                         f"For each base speed, the brake pressures are {schedule.moduleList[-2][2]} bar \n"
                         f"And for each of those, the durations the brake application in seconds are {schedule.moduleList[-2][3]}s \n")
            self.bitmapGraph = wx.StaticBitmap( self.tab2, bitmap=wx.Bitmap( "images/speed.bmp", wx.BITMAP_TYPE_ANY ))
        elif schedule_name == self.scheduleList[5]:
            textBlock = ("A Torque Control test schedule for the testing for brake fade.\n"
                         "In this schedule, the motor will run up to a given initial speed, \n"
                         "the brakes will be applied, and while the torque is held constant, "
                         "will be held until the end set speed is reached. \n"
                         f"The speed pairs (initial speed, end speed) are {schedule.moduleList[-1][1]} km/h \n"
                         f"And for each speed bound, the brake pressure will be applied at {schedule.moduleList[-1][2]} bar \n")
            self.bitmapGraph = wx.StaticBitmap( self.tab2, bitmap=wx.Bitmap( "images/torque.bmp", wx.BITMAP_TYPE_ANY ))
        else:
            textBlock = "No Schedule Selected"
            self.bitmapGraph = wx.StaticBitmap( self.tab2, bitmap=wx.Bitmap( "images/empty.bmp", wx.BITMAP_TYPE_ANY ))

        self.boxDTab2.Add( self.bitmapGraph, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.textGeneralInfo.SetLabel(textBlock)

    def addTestScheduleHandler(self, handler):
        self.choiceSchedule.Bind( wx.EVT_CHOICE, handler )

    def addCOMInHandler(self, handler):
        self.entryCOMIn.Bind( wx.EVT_TEXT, handler )
        self.entryCOMIn.Bind( wx.EVT_TEXT_ENTER, handler )

    def addCOMOutHandler(self, handler):
        self.entryCOMOut.Bind( wx.EVT_TEXT, handler )
        self.entryCOMOut.Bind( wx.EVT_TEXT_ENTER, handler )

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

    











