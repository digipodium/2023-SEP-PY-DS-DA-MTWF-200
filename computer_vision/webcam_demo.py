import cv2
import numpy as np
import os
def load_video(camera_index):
    video = cv2.VideoCapture(camera_index)
    while True:
        status , frame = video.read()
        if not status:
            print("🤯 Camera data not read!!")
            break
        cv2.imshow("Camera",frame)
        if cv2.waitKey(1) == ord('q'): # 1 represents 1 millisecond
            break
    # clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cam_idx = 'http://192.168.18.139:4747/video'
    load_video(cam_idx)