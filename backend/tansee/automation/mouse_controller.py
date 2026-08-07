"""
Mouse Controller

Controls Windows cursor.
"""

import pyautogui


class MouseController:

    def __init__(self):

        pyautogui.FAILSAFE = False

        self.screen_width, self.screen_height = pyautogui.size()

    def move(self, x: int, y: int):

        pyautogui.moveTo(x, y)