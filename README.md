Drake Dyno Software for Data Acquisition
=========================

A python program that's compiled into an .exe (with pyinstaller) to run with a Arduino Uno.

Usage
========

Works with a "COM3" port. 
Now works with serial, don't need pyfirmata anymore. The pyfirmata_case folder is deprecated now. 
Requires the folliwng packages 
- pyserial 
- wxPython

The old pyfirmata version executable is in the dist folder, called main.exe. 

Notes
=========
Because i keep forgetting; to compile to exe, run Anaconda prompt and use

    pyinstaller --onefile main.py
    
in the directory of main.py

Done 
====================
- Recording functionality with GUI and a button is done and works alright

To Do
======
- flesh out the GUI 
- add some test runs for analog/digital output
- figure out a basic PID implementation 
