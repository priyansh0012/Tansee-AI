import cv2

from tansee.camera.camera_manager import CameraManager
from tansee.camera.fps_counter import FPSCounter

from tansee.vision.hand_detector import HandDetector
from tansee.vision.hand_landmarks import HandLandmarks

from tansee.automation.mouse_controller import MouseController
from tansee.automation.motion_filter import MotionFilter

from tansee.gesture.pinch_detector import PinchDetector
from tansee.gesture.click_manager import ClickManager

from tansee.gesture.right_click_detector import RightClickDetector
from tansee.gesture.right_click_manager import RightClickManager


def main():

    camera = CameraManager()
    fps_counter = FPSCounter()

    hand_detector = HandDetector()

    mouse = MouseController()
    motion_filter = MotionFilter()

    pinch_detector = PinchDetector()
    click_manager = ClickManager()

    right_click_detector = RightClickDetector()
    right_click_manager = RightClickManager()

    if not camera.start():
        return

    while True:

        success, frame = camera.read_frame()

        if not success:
            print("❌ Unable to read frame.")
            break

        # Detect Hands
        results = hand_detector.find_hands(frame)

        # Frame Size
        height, width, _ = frame.shape

        # Extract Landmarks
        hands = HandLandmarks.get_landmarks(
            results,
            width,
            height,
        )

        # If Hand Found
        if hands:

            # Index Finger Tip
            x, y = hands[0][8]

            # Convert Camera Coordinates to Screen Coordinates
            screen_x = int((x / width) * mouse.screen_width)
            screen_y = int((y / height) * mouse.screen_height)

            # Smooth Cursor
            screen_x, screen_y = motion_filter.smooth(
                screen_x,
                screen_y,
            )

            # Move Mouse
            mouse.move(
                screen_x,
                screen_y,
            )

            # -----------------------------
            # LEFT CLICK
            # -----------------------------
            is_pinching = pinch_detector.is_pinching(
                hands[0]
            )

            if click_manager.should_click(is_pinching):

                cv2.putText(
                    frame,
                    "CLICK",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2,
                )

                mouse.left_click()

            # -----------------------------
            # RIGHT CLICK
            # -----------------------------
            is_right_click = right_click_detector.is_right_click(
                hands[0]
            )

            if right_click_manager.should_click(is_right_click):

                cv2.putText(
                    frame,
                    "RIGHT CLICK",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    2,
                )
                mouse.right_click()

            # Draw Index Finger
            cv2.circle(
                frame,
                (x, y),
                12,
                (0, 0, 255),
                -1,
            )

        # Draw Hand Skeleton
        frame = hand_detector.draw_hands(
            frame,
            results,
        )

        # FPS
        fps = fps_counter.update()

        cv2.putText(
            frame,
            f"FPS: {fps:.2f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        # Show Camera
        cv2.imshow(
            "Tansee AI Camera",
            frame,
        )

        # Exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.stop()


if __name__ == "__main__":
    main()