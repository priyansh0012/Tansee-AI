"""
Pinch Detector

Detects pinch gesture between
thumb tip and index finger tip.
"""

import math


class PinchDetector:

    def __init__(self, threshold: int = 35):
        self.threshold = threshold

    def is_pinching(self, hand_landmarks):

        thumb_x, thumb_y = hand_landmarks[4]
        index_x, index_y = hand_landmarks[8]

        distance = math.hypot(
            index_x - thumb_x,
            index_y - thumb_y,
        )

        return distance < self.threshold