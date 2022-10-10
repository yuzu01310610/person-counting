import cv2
import datetime
import schedule
import time

deviceid = []

def check_cam_num():

    if deviceid == []: 
        for camera_number in range(0, 10):
            cap = cv2.VideoCapture(camera_number)
            ret, frame = cap.read()

            if ret is True:
                deviceid.append(camera_number)
        print(deviceid)
    else:
        print("satisfied list!")
    print(deviceid)

schedule.every(1/6).minutes.do(check_cam_num)
while True:
    try:
        schedule.run_pending()
        # time.sleep(20)#20
    except KeyboardInterrupt:
        break