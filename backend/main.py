import cv2

from tansee.camera.camera_manager import CameraManager
from tansee.camera.fps_counter import FPSCounter
from tansee.vision.hand_detector import HandDetector
from tansee.vision.hand_landmarks import HandLandmarks


def main():

    camera = CameraManager()
    fps_counter = FPSCounter()
    hand_detector = HandDetector()

    if not camera.start():
        return

    while True:

        success, frame = camera.read_frame()

        if not success:
            print("❌ Unable to read frame.")
            break

        # Detect hands
        results = hand_detector.find_hands(frame)

        # Get frame size
        height, width, _ = frame.shape

        # Extract landmarks
        hands = HandLandmarks.get_landmarks(
            results,
            width,
            height,
        )

        # Draw red circle on index finger
        if hands:

            print(hands[0][8])

            x, y = hands[0][8]

            cv2.circle(
                frame,
                (x, y),
                12,
                (0, 0, 255),
                -1,
            )

        # Draw MediaPipe skeleton
        frame = hand_detector.draw_hands(frame, results)

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

        cv2.imshow("Tansee AI Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.stop()


if __name__ == "__main__":
    main()