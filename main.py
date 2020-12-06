"""
Algorithm Implementation for CS 526
Based heavily on "Eye-Hand Behavior in Human-Robot Shared Manipulation" included with this repo for reference
Could theoretically be added to gazebo simulation with project
"""
import time
from display import eye_disp

eyes1 = eye_disp(x_max=700, y_max=400)
eyes1.look(.5, .5, .5)
eyes1.look(-.3, .5, 1)
eyes1.follow_mouse_click(10)
eyes1.close()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
