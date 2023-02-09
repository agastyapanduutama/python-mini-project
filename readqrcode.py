# Importing library
import cv2
from pyzbar.pyzbar import decode
import time
from datetime import datetime
import schedule
import os
import keyboard
import shutil


def send_enter_key(datana):
    # Send the "Enter" key
    keyboard.write(datana)
    keyboard.press_and_release("enter")


# Function for read barcode
def BarcodeReader(image):

    # read the image in numpy array using cv2
    # img = cv2.imread(image)
    img = image
    # Decode the barcode image
    detectedBarcodes = decode(img)

    # If not detected then print the message
    if not detectedBarcodes:
        print("Tidak ada barcode terdeteksi")
        # tes = tes
    else:

        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)

            if barcode.data != "":

                datana = str(barcode.data)
                

pTime = 0
no = 0

while True:
    try:
        cap = cv2.VideoCapture(0)
        while True:
            check, frame = cap.read()

            schedule.run_pending()

            BarcodeReader(frame)

            # FPS
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(frame, f'FPS: {int(fps)}', (120, 70),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 1)
            # End FPS

            cv2.imshow('video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except:
        print("Error accessing camera.")
    finally:
        cap.release()
        cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()
