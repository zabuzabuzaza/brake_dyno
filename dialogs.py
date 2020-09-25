
import wx 

class SerialDialog(wx.Dialog): 
    def __init__( self, parent , title=""):
        # super().__init__(parent, size = (250,150)) 
        wx.Dialog.__init__ ( self, parent, title=title, size=( 250,250 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
        
        
        bSizer22 = wx.BoxSizer( wx.VERTICAL )
        
        self.dialog_message = wx.StaticText( self, wx.ID_ANY, "Dialog Here", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.dialog_message.Wrap( -1 )
        bSizer22.Add( self.dialog_message, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.SetSizer( bSizer22 )
        self.Layout()
        
        self.Centre( wx.BOTH )


    def setDialogMessage(self, message): 
        self.dialog_message.SetLabel( message )