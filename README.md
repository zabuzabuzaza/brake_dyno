Drake Dyno Software for Data Acquisition
=========================

A python program that's compiled into an .exe (with pyinstaller) to run with a Arduino Uno.

Usage
========

Works with a "COM3" port. 
Requires the package: 
- pyfirmata 
- matplotlib

The executable is in the dist folder, called main.exe. 

Notes
=========
Because i keep forgetting; to compile to exe, run Anaconda prompt and use::

    pyinstaller --onefile main.py
    
in the directory of main.py

To Do
======
- create tk frame for gui (and all the functionality that comes with it)
