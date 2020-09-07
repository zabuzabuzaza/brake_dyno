# -*- coding: utf-8 -*-
"""
Data aquisition software for the 2020 MECH4552 Brake Dyno team.
"""
import sys
import wx


from controller import Controller


def main():
    """
    Entry point to data aquisition software. Initialises the wxPython frame
    and runs the event handling loop.
    """

    gooey = wx.App()
    Controller()
    gooey.MainLoop()



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        # haven't been able to get the serial port ot properly close in the
        # event of an Exception. It's not serious or anything, just have to
        # unplug it and plug the Arduino back in every time an Exception
        # happens

        # tempArduino = serial.Serial('COM3')
        # tempArduino.close()
        print(e)
        sys.exit(0)