# 👁️ PhishVision

AI-Powered Phishing Website Detector

## What is PhishVision?
A system that detects phishing websites using Computer Vision and AI.
It takes a screenshot of any website and analyzes it to determine if it's safe or a phishing attempt.

## How it works
1. Enter a URL
2. System takes a screenshot
3. AI analyzes the image
4. Returns: SAFE ✅ or PHISHING ⚠️

## Technologies
- Python
- OpenCV (Computer Vision)
- Selenium (Screenshot)
- Flask (API)
- HTML/CSS/JS (Frontend)

## How to run
pip install flask selenium opencv-python pillow
python app.py

## Results
- Google.com → ✅ SAFE
- Gmail.com → ⚠️ PHISHING DETECTED