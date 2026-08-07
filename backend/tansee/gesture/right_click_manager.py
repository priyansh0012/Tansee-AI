"""
Right Click Manager
"""

class RightClickManager:

    def __init__(self):
        self.clicked = False

    def should_click(self, is_pinching):

        if is_pinching and not self.clicked:
            self.clicked = True
            return True

        if not is_pinching:
            self.clicked = False

        return False