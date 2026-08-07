"""
Right Click Detector

Detects pinch between
thumb tip and middle finger tip.
"""

import math


class RightClickDetector:

    def __init__(self, threshold: int = 35):
        self.threshold = threshold

    def is_right_click(self, hand_landmarks):

        thumb_x, thumb_y = hand_landmarks[4]
        middle_x, middle_y = hand_landmarks[12]

        distance = math.hypot(
            middle_x - thumb_x,
            middle_y - thumb_y,
        )

        return distance < self.threshold