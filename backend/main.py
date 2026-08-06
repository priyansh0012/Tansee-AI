from tansee.camera.camera_manager import CameraManager


def main():
    camera = CameraManager()

    if camera.start():
        print("🚀 Tansee AI Camera Engine Started Successfully!")
    else:
        print("❌ Camera initialization failed.")


if __name__ == "__main__":
    main()