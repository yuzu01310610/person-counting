import cv2
import datetime
import schedule
import time
import os
import numpy

def cam_set(deviceid):
    # video capture
    cap = cv2.VideoCapture(deviceid)

    return cap

def job():

    deviceid = 0
    cap1=cam_set(deviceid)
    ret1, frame1 = cap1.read()

    strdate=datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    fname1="image1_"+ strdate + ".jpg"
    image1 = cv2.imwrite('./double_img/fname1.jpg', frame1)

    deviceid = 1
    cap2=cam_set(deviceid)
    ret2, frame2 = cap2.read()
    fname2="image2_"+ strdate + ".jpg"
    image2 = cv2.imwrite('./double_img/fname2.jpg', frame2)

    im1 = cv2.imread('./double_img/fname1.jpg')
    im_2 = cv2.imread('./double_img/fname2.jpg')

    size = (1920, 1080)

    im2 = cv2.resize(im_2, size)

    print(im1.shape)
    print(im2.shape)

    im_v = cv2.vconcat([im1, im2])
    cv2.imwrite('./save_img/person.jpg', im_v)
   
schedule.every(1/6).minutes.do(job)
while True:
    try:
        schedule.run_pending()
        time.sleep(20)#20
    except KeyboardInterrupt:
        break