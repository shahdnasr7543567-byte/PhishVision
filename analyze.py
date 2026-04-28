import cv2
import numpy as np

def analyze_screenshot(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Cannot read image")
        return False
    print(f"Image: {img.shape[1]}x{img.shape[0]}")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blue_lower = np.array([100, 50, 50])
    blue_upper = np.array([130, 255, 255])
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
    blue_pixels = cv2.countNonZero(blue_mask)
    print(f"Blue pixels: {blue_pixels}")
    if blue_pixels > 7600:
        print("WARNING: Login page detected!")
        return True
    else:
        print("SAFE: No login page")
        return False