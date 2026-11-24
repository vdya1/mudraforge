"""
Environment check script for MudraForge.
Validates Python runtime, library dependencies, and camera accessibility.
"""
import argparse
import sys
import time


def check_python() -> None:
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    if (version.major, version.minor) not in [(3, 10), (3, 11)]:
        print("WARNING: MudraForge requires Python 3.10 or 3.11.")
    else:
        print("Python version satisfies requirement (3.10 or 3.11).")


def check_dependencies() -> None:
    packages = [
        ("mediapipe", "mediapipe"),
        ("cv2", "opencv-python"),
        ("numpy", "numpy"),
        ("pandas", "pandas"),
        ("sklearn", "scikit-learn"),
        ("joblib", "joblib"),
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("pyautogui", "pyautogui"),
        ("streamlit", "streamlit"),
    ]
    print("\nDependency Check:")
    for mod_name, label in packages:
        try:
            mod = __import__(mod_name)
            ver = getattr(mod, "__version__", "available")
            print(f"  [OK] {label} ({mod_name}): {ver}")
        except ImportError:
            print(f"  [MISSING] {label} ({mod_name})")


def check_camera(camera_id: int, no_camera: bool) -> None:
    if no_camera:
        print("\nCamera check skipped (--no-camera flag enabled).")
        return

    print(f"\nTesting camera at index {camera_id}...")
    try:
        import cv2
    except ImportError:
        print("Cannot test camera: opencv-python is not installed.")
        return

    cap = cv2.VideoCapture(camera_id)
    if not cap.isOpened():
        print(f"ERROR: Unable to open camera device at index {camera_id}.")
        return

    print("Camera successfully opened. Previewing feed for 2 seconds...")
    start_time = time.time()
    try:
        while time.time() - start_time < 2.0:
            ret, frame = cap.read()
            if not ret or frame is None:
                print("WARNING: Failed to grab frame from camera.")
                break
            cv2.imshow("MudraForge Environment Check - Camera Test", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
    print("Camera check completed.")


def main() -> None:
    parser = argparse.ArgumentParser(description="MudraForge Environment Verification")
    parser.add_argument("--camera", type=int, default=0, help="Camera device index (default: 0)")
    parser.add_argument("--no-camera", action="store_true", help="Skip webcam verification")
    args = parser.parse_args()

    check_python()
    check_dependencies()
    check_camera(args.camera, args.no_camera)


if __name__ == "__main__":
    main()
