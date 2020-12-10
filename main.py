#!/usr/bin/env python
"""
Algorithm Implementation for CS 526
Based heavily on "Eye-Hand Behavior in Human-Robot Shared Manipulation" included with this repo for reference
Could theoretically be added to gazebo simulation with project
"""
import time
import sys

from eye_model import eye_disp


def saccade(obj, coord1, coord2, times):
    steps = 10
    obj.look(coord1[0], coord1[1], coord1[2])
    time.sleep(.05)
    for i in range(times):
        for n in range(steps):
            pitch = coord1[0] + ((coord2[0] - coord1[0]) * n / steps)
            yaw = coord1[1] + ((coord2[1] - coord1[1]) * n / steps)
            dist = coord1[2] + ((coord2[2] - coord1[2]) * n / steps)
            obj.look(pitch, yaw, dist)
            time.sleep(.001)
        time.sleep(.05)
        for n in range(steps, 0, -1):
            pitch = coord1[0] + ((coord2[0] - coord1[0]) * n / steps)
            yaw = coord1[1] + ((coord2[1] - coord1[1]) * n / steps)
            dist = coord1[2] + ((coord2[2] - coord1[2]) * n / steps)
            obj.look(pitch, yaw, dist)
            time.sleep(.001)
        time.sleep(.05)
    for n in range(steps):
        pitch = coord1[0] + ((coord2[0] - coord1[0]) * n / steps)
        yaw = coord1[1] + ((coord2[1] - coord1[1]) * n / steps)
        dist = coord1[2] + ((coord2[2] - coord1[2]) * n / steps)
        obj.look(pitch, yaw, dist)
        time.sleep(.001)


def smooth_pursuit(obj, coord1, coord2):
    steps = 50
    for n in range(0, steps+1):
        pitch = coord1[0] + ((coord2[0] - coord1[0]) * n / steps)
        yaw = coord1[1] + ((coord2[1] - coord1[1]) * n / steps)
        dist = coord1[2] + ((coord2[2] - coord1[2]) * n / steps)
        obj.look(pitch, yaw, dist)
        time.sleep(.0006)


p2 = (.5, .5, 1)
p1 = (-.6, -.5, .1)
p3 = (.4, .4, .1)
p4 = (0, .3, .5)
# eyes1 = eye_disp(x_max=700, y_max=400)
# for i in range(3):
#     eyes1.look(p1[0], p1[1], p1[2])
#     time.sleep(2)
#     eyes1.look(p2[0], p2[1], p2[2])
#     time.sleep(.08)
#     eyes1.look(p1[0], p1[1], p1[2])

# eyes1.follow_mouse_click(10)
# slide(eyes1, p1, p2)
# time.sleep(.5)
# slide(eyes1, p2, p4)
# time.sleep(.5)
# slide(eyes1, p4, p3)
# time.sleep(.5)
# slide(eyes1, p3, p1)
# time.sleep(.5)

# saccade(eyes1, p3, p4, 1)
# time.sleep(.5)
# saccade(eyes1, p3, p1, 1)
# time.sleep(.5)
# saccade(eyes1, p3, p4, 1)
# time.sleep(.5)
# saccade(eyes1, p3, p1, 1)
# time.sleep(.5)
# saccade(eyes1, p3, p4, 1)



if __name__ == "__main__":
    eyes1 = eye_disp(x_max=700, y_max=400) # can be customized
    old_pitch = 0
    old_yaw = 0
    old_dist = 0
    try:
        start = sys.argv[1:4]
        old_pitch = float(start[0])
        old_yaw = float(start[1])
        old_dist = float(start[2])
        eyes1.look(old_pitch, old_yaw, old_yaw)
    except:
        print("Please enter 3 numbers between -1 to 1 as starting coordinates")
    try:
        direc = sys.argv[4:]
        for i, com in enumerate(direc):
            if com == 'saccade':
                new_p = float(direc[i+1])
                new_y = float(direc[i+2])
                new_d = float(direc[i+3])
                saccade(eyes1, [old_pitch, old_yaw, old_dist], [new_p, new_y, new_d], 1)
                old_pitch = new_p
                old_yaw = new_y
                old_dist = new_d
            if com == "smooth":
                new_p = float(direc[i + 1])
                new_y = float(direc[i + 2])
                new_d = float(direc[i + 3])
                smooth_pursuit(eyes1, [old_pitch, old_yaw, old_dist], [new_p, new_y, new_d])
                old_pitch = new_p
                old_yaw = new_y
                old_dist = new_d
            if com == "fixation":
                new_p = float(direc[i + 1])
                new_y = float(direc[i + 2])
                new_d = float(direc[i + 3])
                eyes1.look(new_p, new_y, new_d)
                time.sleep(.005)
                eyes1.look(old_pitch, old_yaw, old_dist)
            if com == "mouse":
                eyes1.follow_mouse_click(int(i+1))
    except:
        print("Directions incorrect - check format in readme")
    eyes1.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
