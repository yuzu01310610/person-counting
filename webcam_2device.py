import cv2
import datetime
import schedule
import time
import os
import numpy
import index

deviceid = []

#デバイスID読み込み
def cam_set(deviceid): 

    cap = cv2.VideoCapture(deviceid)

    return cap

#カメラのデバイスIDを取得
def check_cam_num():

    #リストが空の時
    if deviceid == []:
        for camera_number in range(0, 10):
            cap = cv2.VideoCapture(camera_number)
            ret, frame = cap.read()

            if ret is True:
                deviceid.append(camera_number)
        print(deviceid)
        job(deviceid)
    
    #2周目
    else:
        print("satisfied list")
        job(deviceid)

def job(deviceid):
    
    deviceid_1 = deviceid[0]
    deviceid_2 = deviceid[1]

    print(deviceid_1)
    print(deviceid_2)        
    #デバイスIDを付けカメラを認識させる
    cap1=cam_set(deviceid_1)
    ret1, frame1 = cap1.read()

    strdate=datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    fname1="image1_"+ strdate + ".png"
    image1 = cv2.imwrite('./double_img/fname1.png', frame1)

    #デバイスIDを認識させる
    cap2=cam_set(deviceid_2)
    ret2, frame2 = cap2.read()
    fname2="image2_"+ strdate + ".png"
    image2 = cv2.imwrite('./double_img/fname2.png', frame2)

    im_1 = cv2.imread('./double_img/fname1.png')
    im_2 = cv2.imread('./double_img/fname2.png')

    #画像サイズの確認
    print(im_1.shape)
    print(im_2.shape)

    #画像サイズを揃える
    size = (1920, 1080)

    im1 = cv2.resize(im_1, size)
    im2 = cv2.resize(im_2, size)

    #画像サイズの確認
    # print(im1.shape)
    # print(im2.shape)

    #画像を縦に結合
    im_v = cv2.vconcat([im1, im2])
    cv2.imwrite('./save_img/person.png', im_v)
    time.sleep(10)

schedule.every(1/6).minutes.do(check_cam_num)
while True:
    try:
        schedule.run_pending()
    except KeyboardInterrupt:
        break