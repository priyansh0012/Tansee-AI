import cv2

from tansee.camera.camera_manager import CameraManager


def main():
    camera = CameraManager()

    if not camera.start():
        return

    while True:

        success, frame = camera.read_frame()

        if not success:
            print("❌ Unable to read frame.")
            break

        cv2.imshow("Tansee AI Camera", frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    camera.stop()


if __name__ == "__main__":
    main()