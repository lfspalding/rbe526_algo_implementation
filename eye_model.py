import time
from graphics import *

# Features that won't move
def fixed_features(x_max, y_max, x_off, win):
    left_eye = Circle(Point(x_max / 2 - x_off, y_max / 2), x_max * .1)
    left_eye.setWidth(3)
    left_eye.draw(win)

    right_eye = Circle(Point(x_max / 2 + x_off, y_max / 2), x_max * .1)
    right_eye.setWidth(3)
    right_eye.draw(win)

    message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to continue.')
    message.draw(win)

class eye_disp:
    def __init__(self, x_max=600, y_max=400):
        # Size of display in pixels
        self.x_max = x_max
        self.y_max = y_max
        # Pupil Coordinates
        self.y = y_max/2
        self.x_off = x_max * .23
        self.left_x = x_max/2 - self.x_off
        self.right_x = x_max/2 + self.x_off
        self.rad = x_max * .01
        # Start graphics window
        self.win = GraphWin('Face', x_max, y_max)  # give title and dimensions
        # Movable graphic objects
        self.left_pup = Circle(Point(self.left_x, self.y), self.rad)
        self.left_pup.setFill('black')
        self.right_pup = Circle(Point(self.right_x, self.y), self.rad)
        self.right_pup.setFill('black')
        self.label = Text(Point(x_max/2, y_max-50), 'Initialization Mode')
        # Call unchanging parts of display
        fixed_features(self.x_max, self.y_max, self.x_off, self.win)
        # Draw changeable features
        self.left_pup.draw(self.win)
        self.right_pup.draw(self.win)
        self.label.draw(self.win)
        # Wait for mouse click
        self.win.getMouse()

    """
    This is the top level function to control where the model looks
    pitch (x-axis) -1 to 1 
    yaw (y-axis) -1 to 1
    distance (mirror correction to x) 0 to 1
    """
    def look(self, pitch, yaw, distance):
        f1 = .05  # factor correction for direction of gaze
        f2 = .01  # factor correction for distance of gaze

        # Update Y
        y = self.y_max/2 + (self.x_max * f1 * yaw)
        dy = self.y - y
        self.y = y

        # Update left X
        raw_lx = self.x_max/2 - self.x_off + (self.x_max * f1 * pitch)
        cor_lx = raw_lx - (self.x_max * f2 * distance)
        dx_left = self.left_x - cor_lx
        self.left_x = cor_lx

        # Update right X
        raw_rx = self.x_max/2 + self.x_off + (self.x_max * f1 * pitch)
        cor_rx = raw_rx + (self.x_max * f2 * distance)
        dx_right = self.right_x - cor_rx
        self.right_x = cor_rx

        self.left_pup.move(dx_left, dy)
        self.right_pup.move(dx_right, dy)

        # Update label
        self.label.undraw()
        self.label = Text(Point(self.x_max/2, self.y_max-50), f"Looking ({pitch}, {yaw}, {distance}).")
        self.label.draw(self.win)

    def follow_mouse_click(self, duration):
        t_end = time.time() + duration
        while time.time() < t_end:
            coord = self.win.getMouse()
            pitch = (self.x_max - coord.getX() - self.x_max/2)/self.x_max
            yaw = (self.y_max - coord.getY() - self.y_max/2)/self.y_max
            self.look(pitch, yaw, 0)

    def close(self):
        self.win.getMouse()
        self.win.close()