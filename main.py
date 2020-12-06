"""
Algorithm Implementation for CS 526
Based heavily on "Eye-Hand Behavior in Human-Robot Shared Manipulation" included with this repo for reference
Could theoretically be added to gazebo simulation with project
"""
import time
from eye_model import eye_disp

def saccade(obj, coord1, coord2, times):
    steps = 10
    for i in range(times):
        for n in range(steps):
            pitch = coord1[0] + ((coord2[0] - coord1[0]) * n / steps)
            yaw = coord1[1] + ((coord2[1] - coord1[1]) * n / steps)
            dist = coord1[2] + ((coord2[2] - coord1[2]) * n / steps)
            obj.look(pitch, yaw, dist)
            time.sleep(.002)
        time.sleep(.05)
        for n in range(steps, 0, -1):
            pitch = coord1[0] + ((coord2[0] - coord1[0]) * n / steps)
            yaw = coord1[1] + ((coord2[1] - coord1[1]) * n / steps)
            dist = coord1[2] + ((coord2[2] - coord1[2]) * n / steps)
            obj.look(pitch, yaw, dist)
            time.sleep(.002)
        time.sleep(.05)
    for n in range(steps):
        pitch = coord1[0] + ((coord2[0] - coord1[0]) * n / steps)
        yaw = coord1[1] + ((coord2[1] - coord1[1]) * n / steps)
        dist = coord1[2] + ((coord2[2] - coord1[2]) * n / steps)
        obj.look(pitch, yaw, dist)
        time.sleep(.002)


def slide(obj, coord1, coord2):
    steps = 50
    for n in range(0, steps+1):
        pitch = coord1[0] + ((coord2[0] - coord1[0]) * n / steps)
        yaw = coord1[1] + ((coord2[1] - coord1[1]) * n / steps)
        dist = coord1[2] + ((coord2[2] - coord1[2]) * n / steps)
        obj.look(pitch, yaw, dist)
        time.sleep(.0006)


p1 = (.5, .5, .5)
p2 = (-.3, -.5, 1)
p3 = (.2, .2, .1)
p4 = (-.9, .3, .9)
eyes1 = eye_disp(x_max=700, y_max=400)
# eyes1.look(p1[0], p1[1], p1[2])
# eyes1.look(p2[0], p2[1], p2[2])
# eyes1.follow_mouse_click(10)
slide(eyes1, p1, p2)
time.sleep(.5)
slide(eyes1, p2, p4)
time.sleep(.5)
slide(eyes1, p4, p3)
time.sleep(.5)
slide(eyes1, p3, p1)
time.sleep(.5)
saccade(eyes1, p4, p2, 2)
eyes1.close()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
