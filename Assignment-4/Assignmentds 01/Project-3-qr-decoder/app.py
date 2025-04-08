from pyzbar.pyzbar import decode 
import cv2

image = cv2.imread('D:/Q3/Assignment-4/Assignmentds 01/Project3-qr-decoder/new.png')

decoded_objects = decode(image)

for obj in decoded_objects:
    print(obj.data.decode)