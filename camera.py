import cv2

while True:
    try:
        camera = cv2.VideoCapture(0)
        while True:
            _, frame = camera.read()
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except:
        print("Error accessing camera.")
    finally:
        camera.release()
        cv2.destroyAllWindows()
