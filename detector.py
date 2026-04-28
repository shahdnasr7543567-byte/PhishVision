import cv2
import numpy as np

def detect_phishing(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return False, []
    
    reasons = []
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # كشف اللون الأزرق
    blue_mask = cv2.inRange(hsv, 
        np.array([100, 50, 50]), 
        np.array([130, 255, 255]))
    if cv2.countNonZero(blue_mask) > 7600:
        reasons.append("Blue login form detected")
    
    # كشف اللون الأحمر
    red_mask1 = cv2.inRange(hsv,
        np.array([0, 50, 50]),
        np.array([10, 255, 255]))
    red_mask2 = cv2.inRange(hsv,
        np.array([170, 50, 50]),
        np.array([180, 255, 255]))
    red_pixels = cv2.countNonZero(red_mask1) + cv2.countNonZero(red_mask2)
    if red_pixels > 5000:
        reasons.append("Red login form detected")
    
    # كشف المستطيلات
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 30, 100)
    contours, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    fields = []
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w > 200 and 25 < h < 70:
            fields.append((x, y, w, h))
    
    if len(fields) >= 2:
        reasons.append("Multiple input fields detected")
    
    return len(reasons) > 0, reasons