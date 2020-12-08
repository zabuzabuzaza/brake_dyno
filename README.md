Drake Dyno Software for Data Acquisition
=========================

A python program for the running and data collection of the UQR brake dyno. Requires two Arduinos for the data collection and control system respedctively. Due to the size limits on Github, the exe (compiled with pyinstaller) cannot be uploaded here, so follow the instructions below to create the exe. Otherwise, you will need Python installed to run the program. 

![Example](images/program.gif)

Usage
========

Default is COM3, but you can input whatever port and it'll check it. 
Requires the following packages 
- pyserial 
- wxPython
- numpy (although I might get rid of this dependancy to reduce file size

Notes
=========
To create and compile the exe to compile to exe, run 

    pyinstaller --onefile main.py
    
in the directory of main.py. You will still need Python installed to compile. 

Done 
====================
- basic framework for spitting out the required speed values and pressure values is up. 
- Test options for the brake fade tests are working
- Serial in (data acquisition) should be all set 

To Do
======
- implement temperature check for frake squeal tests
- test with actual values 
- test with implemented control system (vfd and brake system)
