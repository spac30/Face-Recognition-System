import cv2
import sys
import time


class Photo_webcam:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # We load the cascade for the face.
        self.a = 25
        
    def detect(self, gray, frame): # We create a function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles. 
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5) # We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
        for (x, y, w, h) in faces: # For each detected face:
            self.a = self.a - 1
            b = '{:02d}'.format(self.a)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # We paint a rectangle around the face.
            roi_color = frame[y:y+h, x:x+w] # We get the region of interest in the colored image.
            FaceFileName = "unknownfaces/face_" + str(y) + ".jpg"
            cv2.imwrite(FaceFileName, roi_color)
            cv2.imshow('Result',frame)
            sys.stdout.write('\r' + str(b))
            time.sleep(1)
        return frame # We return the image with the detector rectangles.
    
    def run(self):
        video_capture = cv2.VideoCapture(0) # We turn the webcam on.
        
        while True: # We repeat infinitely (until break):
            if self.a == 0:
#                print("\tThank you")
                break
            ret, frame = video_capture.read() # We get the last frame.
            if ret is True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # We do some colour transformations.
            else:
               continue
            canvas = self.detect(gray, frame) # We get the output of our detect function.
        #    cv2.imshow('Video', canvas) # We display the outputs.
            if cv2.waitKey(1) & 0xFF == ord('q'): # If we type on the keyboard:
                break # We stop the loop.
        
        video_capture.release() # We turn the webcam off.
        cv2.destroyAllWindows() # We destroy all the windows inside which the images were displayed.

