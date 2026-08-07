"""
Click Manager

Prevents multiple clicks while
the pinch gesture is held.
"""


class ClickManager:

    def __init__(self):
        self.clicked = False

    def should_click(self, is_pinching: bool) -> bool:

        if is_pinching and not self.clicked:
            self.clicked = True
            return True

        if not is_pinching:
            self.clicked = False

        return False