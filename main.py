"""
Algorithm Implementation for CS 526
Based heavily on "Eye-Hand Behavior in Human-Robot Shared Manipulation" included with this repo for reference
Could theoretically be added to gazebo simulation with project
"""
import time
from eye_model import eye_disp

def saccade(obj, coord1, coord2, duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        obj.look(coord1[0], coord1[1], coord1[2])
        obj.look(coord2[0], coord2[1], coord2[2])

p1 = (.5, .5, .5)
p2 = (-.3, .5, 1)
eyes1 = eye_disp(x_max=700, y_max=400)
eyes1.look(p1)
eyes1.look(p2)
eyes1.follow_mouse_click(10)
eyes1.close()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
