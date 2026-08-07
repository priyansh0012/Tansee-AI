import cv2

from tansee.camera.camera_manager import CameraManager
from tansee.camera.fps_counter import FPSCounter


def main():
    camera = CameraManager()
    fps_counter = FPSCounter()

    if not camera.start():
        return

    while True:

        success, frame = camera.read_frame()

        if not success:
            print("❌ Unable to read frame.")
            break

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