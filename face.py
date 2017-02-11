import cv2

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    go = True
    while go:
        ret, img = cam.read()
        cv2.imshow('my webcam', img)
        if cv2.waitKey(33) == ord('a'):
            go = False
            cv2.imwrite('resources/vince.png', img)
            cv2.destroyAllWindows()
            return
    cv2.destroyAllWindows()
        



show_webcam()
