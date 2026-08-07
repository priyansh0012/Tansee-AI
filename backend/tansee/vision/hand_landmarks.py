"""
Hand Landmark Utilities

Extracts landmark coordinates from MediaPipe results.
"""

from typing import List, Tuple


class HandLandmarks:

    @staticmethod
    def get_landmarks(results, frame_width, frame_height) -> List[List[Tuple[int, int]]]:
        """
        Returns landmark pixel coordinates.

        Returns:
            [
                [(x,y), (x,y), ...21],
                [(x,y), ...21]
            ]
        """

        hands = []

        if not results.multi_hand_landmarks:
            return hands

        for hand in results.multi_hand_landmarks:

            points = []

            for landmark in hand.landmark:

                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                points.append((x, y))

            hands.append(points)

        return hands