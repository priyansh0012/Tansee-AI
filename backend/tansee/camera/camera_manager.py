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

from typing import Any
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
        """

        self.capture = cv2.VideoCapture(self.camera_index)

        if not self.capture.isOpened():
            print("❌ Failed to open camera.")
            return False

        print("✅ Camera started successfully.")
        return True

    def read_frame(self) -> tuple[bool, Any]:
        """
        Read a single frame from the webcam.
        """

        if self.capture is None:
            return False, None

        success, frame = self.capture.read()

        return success, frame

    def stop(self):
        """
        Release the webcam.
        """

        if self.capture is not None:
            self.capture.release()
            self.capture = None

        cv2.destroyAllWindows()

        print("🛑 Camera stopped.")