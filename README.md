Drake Dyno Software for Data Acquisition
=========================

A python program <del>that's compiled into an .exe (with pyinstaller)</del> to run with a Arduino Uno. Used to be compilable to an .exe but it doesn't work with matplotlib. 

![Example](images/example.gif)

Usage
========

Works with a "COM3" port.
Requires the following packages 
- pyserial 
- wxPython
- matplotlib

<del>The executable is in the 'dist' folder.</del>

Notes
=========
Because i keep forgetting; to compile to exe, run Anaconda prompt and use

    pyinstaller --onefile main.py
    
in the directory of main.py

Done 
====================
- Recording functionality with GUI and a button is done and works alright
- live plot in a separate window

To Do
======
- put pyplot window into wx frame
- flesh out the GUI 
- add some test runs for analog/digital output
- figure out a basic PID implementation 
