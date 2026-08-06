"""
===========================================================

Module: Camera Manager

Project: Tansee AI
Version: 1.0.0

Author: Priyanshu Sharma

Description:
-------------
This module is responsible for managing the webcam.

Responsibilities:
- Initialize camera
- Read frames
- Release camera
- Check camera status
- Configure resolution
- Calculate FPS (future)

===========================================================
"""

import cv2


class CameraManager:
    """
    Handles webcam initialization and frame capture.
    """

    def __init__(self, camera_index: int = 0):
        """
        Initialize Camera Manager.
        """
        self.camera_index = camera_index
        self.capture = None

    def start(self) -> bool:
        """
        Start the webcam.

        Returns:
            bool: True if camera starts successfully,
                  False otherwise.
        """

        self.capture = cv2.VideoCapture(self.camera_index)

        if not self.capture.isOpened():
            print("❌ Failed to open camera.")
            return False

        print("✅ Camera started successfully.")
        return True