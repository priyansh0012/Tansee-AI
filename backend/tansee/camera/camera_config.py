"""
Camera Configuration

Stores all camera-related settings.
"""


class CameraConfig:
    """
    Camera configuration class.
    """

    def __init__(
        self,
        width: int = 1280,
        height: int = 720,
        fps: int = 30,
        camera_index: int = 0,
    ):
        self.width = width
        self.height = height
        self.fps = fps
        self.camera_index = camera_index