"""
Hand Detection Module

Uses Google's MediaPipe Hands API.
"""

import cv2
import mediapipe as mp


class HandDetector:
    """
    Detects human hands using MediaPipe.
    """

    def __init__(
        self,
        max_num_hands: int = 2,
        detection_confidence: float = 0.7,
        tracking_confidence: float = 0.7,
    ):
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence,
        )

        self.drawer = mp.solutions.drawing_utils

    def find_hands(self, frame):
        """
        Detect hands in a frame.
        """

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb_frame)

        return results

    def draw_hands(self, frame, results):
        """
        Draw landmarks on detected hands.
        """

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                self.drawer.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                )

        return frame