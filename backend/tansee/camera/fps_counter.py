"""
FPS Counter Module

Calculates live Frames Per Second.
"""

import time


class FPSCounter:
    """
    Calculates real-time FPS.
    """

    def __init__(self):
        self.previous_time = time.perf_counter()
        self.current_time = self.previous_time
        self.fps = 0.0

    def update(self) -> float:
        """
        Update FPS value.

        Returns:
            float: Current FPS
        """

        self.current_time = time.perf_counter()

        delta = self.current_time - self.previous_time

        if delta > 0:
            self.fps = 1.0 / delta

        self.previous_time = self.current_time

        return self.fps