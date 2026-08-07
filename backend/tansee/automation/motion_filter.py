"""
Motion Filter

Smooths cursor movement using
Exponential Moving Average (EMA).
"""

class MotionFilter:

    def __init__(self, alpha: float = 0.25):

        self.alpha = alpha

        self.prev_x = None
        self.prev_y = None

    def smooth(self, x: int, y: int):

        if self.prev_x is None:
            self.prev_x = x
            self.prev_y = y
            return x, y

        smooth_x = self.alpha * x + (1 - self.alpha) * self.prev_x
        smooth_y = self.alpha * y + (1 - self.alpha) * self.prev_y

        self.prev_x = smooth_x
        self.prev_y = smooth_y

        return int(smooth_x), int(smooth_y)