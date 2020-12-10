# rbe526_algo_implementation
Individual Algorithm Implementation Assignment for RBE/CS 526 by Lisa Spalding

#### A simple program that renders robot eye-gaze with saccades and other methods on a simple display. 

## Description: 
There are 4 types of eye movement that can be shown with this program. 
* Saccade
* Smooth Pursuit
* Gaze Fixation
* Follow Mouse Click
See the research paper cited below for detailed descriptions of these behaviors and where they're from.
  
The program consists of three files
* graphics.py (credit at the bottom)
* eye_model.py - contains the object template for the graphical interface
* main.py - run this file with parameters to show eye behaviors

## Instructions:
Example - from the directory folder run: python3 main.py .2 .1 -1 fixation 0 .6 .8 saccade -.6 .5 .8 mouse 10 smooth .3 -.4 -1

'mouse' indicates that the eyes should look at the last mouse click - click around, it's fun. This continues for the integer duration (in seconds) given following the command.

All other numbers should be coordinates between -1 and 1. The units are abstract, but they're calibrated to look good on the eyes. 
The first float of three is the pitch - how far left (-1) or right (1) the eyes look (x-axis).
The second is yaw - how far up (1) or down (-1) the eyes look (y-axis).
The third is the distance - close focus (-1) vs far object (1)
The names of the commands correlate to the movements introduced above.
Many parameters can be adjusted from the main.py file - I encourage this. 
The eye_model file should not need to be edited for most applications. 

## Warnings:
If you don't click when your routine is finished, the program will raise a graphical error. This can be ignored. 
**This code is not robust**, there is minimal error checking. If the commands are not put in properly, the program may act unexpectedly. 
If numbers out of range are put in, the pupils will not behave realistically - they can move out of range. 
However, it is a simple graphical interface, it won't break your computer either. 


## Credits:
Research Paper (included in repo):
Aronson, Reuben & Santini, Thiago & Kübler, Thomas & Kasneci, Enkelejda & Srinivasa, Siddhartha & Admoni, Henny. (2018). Eye-Hand Behavior in Human-Robot Shared Manipulation. 4-13. 10.1145/3171221.3171287.

Uses the graphics.py file, version source [here](https://stackoverflow.com/questions/15886455/simple-graphics-for-python).
Credit John Zelles
