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

class ConstantSpeedOptions(wx.Dialog): 
    def __init__( self, parent , title=""):
        """Options window for brake fade schedules. 

        Parameters
        ----------
        parent : wx.Frame
            The parent frame to spawn this dialog window. 
        title : str, optional
            window title, by default ""
        """
        # formatting constants
        CEN_H = wx.ALIGN_CENTER_HORIZONTAL
        CEN_V = wx.ALIGN_CENTER_VERTICAL
        ALL = wx.ALL
        FLAG = wx.ALL
        BORDER = 5
        PROP0 = 0 # does not expand
        PROP1 = 1 # does expand

        # selected options 
        self.speed_list = []
        self.pressure_list = []
        self.duration_list = []

        wx.Frame.__init__ ( self, parent, title = "Constant Speed Test Schedule", size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        boxA = wx.BoxSizer( wx.VERTICAL )
        
        #######################################################################
        # INSTRUCTIONS AND EXAMPLE
        #######################################################################
        instructions = wx.StaticText( self, label="Enter a list of values separated by commas")
        boxA.Add( instructions, PROP0, ALL|CEN_H, BORDER )
        
        boxBExamples = wx.BoxSizer( wx.HORIZONTAL )
        
        example = wx.StaticText( self, label="eg.")
        example_values = wx.TextCtrl( self, value="10, 20, 30, 40", style=wx.TE_READONLY )

        boxBExamples.Add( example, PROP0, ALL|CEN_V, BORDER )
        boxBExamples.Add( example_values, PROP0, ALL|wx.EXPAND, BORDER )
        boxA.Add( boxBExamples, PROP0, CEN_H|wx.EXPAND|wx.SHAPED, BORDER )
        
        #######################################################################
        # INPUT FOR OPTIONS
        #######################################################################

        boxBInputs = wx.BoxSizer( wx.HORIZONTAL )
        
        gridOptions = wx.FlexGridSizer( 0, 2, 0, 0 )
        gridOptions.SetFlexibleDirection( wx.BOTH )
        gridOptions.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        #######################################################################
        # Speeds
        labelSpeeds = wx.StaticText( self, label="Speeds")
        gridOptions.Add( labelSpeeds, PROP0, FLAG, BORDER )
        
        boxCSpeeds = wx.BoxSizer( wx.HORIZONTAL )
        
        self.inputSpeeds = wx.TextCtrl( self, id=1, style=wx.TE_PROCESS_ENTER )
        labelSpeedUnits = wx.StaticText( self, label="km/h")

        boxCSpeeds.Add( self.inputSpeeds, PROP0, FLAG, BORDER )
        boxCSpeeds.Add( labelSpeedUnits, PROP0, FLAG, BORDER )
        gridOptions.Add( boxCSpeeds, PROP1, wx.EXPAND, BORDER )
        
        #######################################################################
        # Pressures
        labelPressures = wx.StaticText( self, label="Brake Pressures")
        gridOptions.Add( labelPressures, PROP0, FLAG, BORDER )
        
        boxCPressures = wx.BoxSizer( wx.HORIZONTAL )
        
        self.inputPressures = wx.TextCtrl( self, id=2, style=wx.TE_PROCESS_ENTER )
        labelPressureUnits = wx.StaticText( self, label="bar")

        boxCPressures.Add( self.inputPressures, PROP0, FLAG, BORDER )
        boxCPressures.Add( labelPressureUnits, PROP0, FLAG, BORDER )
        gridOptions.Add( boxCPressures, PROP1, wx.EXPAND, BORDER )
        
        #######################################################################
        # Durations
        labelDurations = wx.StaticText( self, label="Brake Application\nDuration")
        gridOptions.Add( labelDurations, PROP0, FLAG, BORDER )
        
        boxCDurations = wx.BoxSizer( wx.HORIZONTAL )
        
        self.inputDurations = wx.TextCtrl( self, id=3, style=wx.TE_PROCESS_ENTER )
        labelDurationUnits = wx.StaticText( self, label="seconds")

        boxCDurations.Add( self.inputDurations, PROP0, FLAG, BORDER )
        boxCDurations.Add( labelDurationUnits, PROP0, FLAG, BORDER )
        gridOptions.Add( boxCDurations, PROP1, wx.EXPAND, BORDER )
        
        boxBInputs.Add( gridOptions, PROP1, wx.EXPAND, BORDER )
        boxA.Add( boxBInputs, PROP1, CEN_H, BORDER )

        #######################################################################
        # CHOSEN SETTINGS
        #######################################################################
        
        labelChosenOptions = wx.StaticText( self, label="Parameters")
        boxA.Add( labelChosenOptions, PROP0, FLAG|CEN_H, BORDER )
        
        boxBChosenOptions = wx.BoxSizer( wx.HORIZONTAL )
        
        gridChosenOptions = wx.FlexGridSizer( 0, 2, 0, 0 )
        gridChosenOptions.SetFlexibleDirection( wx.BOTH )
        gridChosenOptions.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        labelChosenSpeeds = wx.StaticText( self, label="Speeds")
        self.labelSpeedList = wx.StaticText( self, label="[]")
        labelChosenPressures = wx.StaticText( self, label="Brake Pressures")
        self.labelPressureList = wx.StaticText( self, label="[]")
        labelChosenDuration = wx.StaticText( self, label="Brake Application\nDuration")
        self.labelDurationList = wx.StaticText( self, label="[]")

        gridChosenOptions.Add( labelChosenSpeeds, PROP0, FLAG, BORDER )
        gridChosenOptions.Add( self.labelSpeedList, PROP0, FLAG, BORDER )
        gridChosenOptions.Add( labelChosenPressures, PROP0, FLAG, BORDER )
        gridChosenOptions.Add( self.labelPressureList, PROP0, FLAG, BORDER )
        gridChosenOptions.Add( labelChosenDuration, PROP0, FLAG, BORDER )
        gridChosenOptions.Add( self.labelDurationList, PROP0, FLAG, BORDER )
        boxBChosenOptions.Add( gridChosenOptions, PROP1, wx.EXPAND, BORDER )
        
        boxA.Add( boxBChosenOptions, PROP1, CEN_H, BORDER )
        boxBButtons = wx.BoxSizer( wx.HORIZONTAL )
        
        #######################################################################
        # APPLY BUTTON
        #######################################################################
        
        self.buttonApply = wx.Button( self, label="Apply Settings")
        # self.buttonDefault = wx.Button( self, label="Default Values")

        boxBButtons.Add( self.buttonApply, PROP0, FLAG, BORDER )
        # boxBButtons.Add( self.buttonDefault, PROP0, FLAG, BORDER )
        
        boxA.Add( boxBButtons, PROP0, CEN_H, BORDER )
        
        self.SetSizer( boxA )
        self.Layout()
        self.Centre( wx.BOTH )
        
    def testPrint(self): 
        print("Testslkrghdlg")

    def setDialogMessage(self, message): 
        self.dialog_message.SetLabel( message )

    def setSettingsHandler(self, handler):
        self.inputSpeeds.Bind( wx.EVT_TEXT, handler )
        self.inputSpeeds.Bind( wx.EVT_TEXT_ENTER, handler )

        self.inputPressures.Bind( wx.EVT_TEXT, handler )
        self.inputPressures.Bind( wx.EVT_TEXT_ENTER, handler )

        self.inputDurations.Bind( wx.EVT_TEXT, handler )
        self.inputDurations.Bind( wx.EVT_TEXT_ENTER, handler )

    def setApplyButtonHandler(self, handler): 
        self.buttonApply.Bind( wx.EVT_BUTTON, handler )

    def setDefaultButtonHandler(self, handler): 
        self.buttonDefault.Bind( wx.EVT_BUTTON, handler )

    def setSettingsLabels(self, id, message): 
        if id == 1: 
            self.speed_list = self.string2list(message)
            self.labelSpeedList.SetLabel(str(self.speed_list))
        elif id == 2: 
            self.pressure_list = self.string2list(message)
            self.labelPressureList.SetLabel(str(self.pressure_list))
        elif id == 3: 
            self.duration_list = self.string2list(message)
            self.labelDurationList.SetLabel(str(self.duration_list))
        else: 
            pass
    
    def string2list(self, string): 
        try: 
            input_list = [int(n) for n in string.split(",")]
        except ValueError: 
            return "INVALID INPUT"
        return input_list

    def getSettings(self): 
        return self.speed_list, self.pressure_list, self.duration_list

    def getOptionValidity(self): 
        if (self.labelSpeedList.Label == "[]" or 
            self.labelPressureList.Label == "[]" or 
            self.labelDurationList.Label == "[]" or
            self.labelSpeedList.Label == "INVALID INPUT" or 
            self.labelPressureList.Label == "INVALID INPUT" or 
            self.labelDurationList.Label == "INVALID INPUT"): 
            return False
        else: 
            return True

