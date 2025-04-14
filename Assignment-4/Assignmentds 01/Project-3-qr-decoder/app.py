import cv2
import os

image_path = r"D:\Q3\Assignment-4\Assignmentds 01\Project-3-qr-decoder\new.png"

# Check if file exists
if not os.path.exists(image_path):
    print("❌ File not found. Please check the path.")
else:
    image = cv2.imread(image_path)
    if image is None:
        print("❌ Failed to load the image. File might be corrupted.")
    else:
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(image)
        if bbox is not None and data:
            print("✅ QR Code Data:", data)
        else:
            print("⚠️ No QR code found in the image.")
