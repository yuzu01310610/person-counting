import cv2
import datetime
import schedule
import time
import os
import numpy
import firebase_upload

deviceid = []
n = 0
firebase_upload.error_count(n)


WIDTH = 1920
HEIGHT = 1080

FPS = 5


#デバイスID読み込み
def cam_set(deviceid, WIDTH, HEIGHT, FPS): 

    cap = cv2.VideoCapture(deviceid)

    #フォーマット・FPSの設定
    #cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y','U','Y','V'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)

    # フォーマット・解像度・FPSの取得
    fourcc = decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC))
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    #print("ID:{} fourcc:{} fps:{}　width:{}　height:{}".format(deviceid, fourcc, fps, width, height))


    return cap

def decode_fourcc(v):
        v = int(v)
        return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])


#カメラのデバイスIDを取得
def check_cam_num():

    #リストが空の時(実行開始時一度だけ)
    if deviceid == []:
        for camera_number in range(0, 10):
            cap = cv2.VideoCapture(camera_number)
            ret, frame = cap.read()

            if ret is True:
                deviceid.append(camera_number)
        #print(deviceid)
        job(deviceid)
    
    #2周目
    else:
        job(deviceid)

def job(deviceid):
    
    dt_now = datetime.datetime.now()
    # print(deviceid[0])
    # print(deviceid[1])
    # print(dt_now)
    #1台目のカメラ
    cap1=cam_set(deviceid[0], WIDTH, HEIGHT, FPS)
    ret1, frame1 = cap1.read()
    fname1="image1.png"
    image1 = cv2.imwrite('/home/user/BusLocationSystem-PersonCount/double_img/fname1.png', frame1)
    im_1 = cv2.imread('/home/user/BusLocationSystem-PersonCount/double_img/fname1.png')


    #2台目のカメラ
    cap2=cam_set(deviceid[1], WIDTH, HEIGHT, FPS)
    ret2, frame2 = cap2.read()
    fname2="image2.png"
    image2 = cv2.imwrite('/home/user/BusLocationSystem-PersonCount/double_img/fname2.png', frame2)

    im_1 = cv2.imread('/home/user/BusLocationSystem-PersonCount/double_img/fname1.png')
    im_2 = cv2.imread('/home/user/BusLocationSystem-PersonCount/double_img/fname2.png')

    #画像サイズの確認
    # print(im_1.shape)
    # print(im_2.shape)

    #2枚の画像サイズを同じにする
    size = (320, 240)

    im1 = cv2.resize(im_1, size)
    im2 = cv2.resize(im_2, size)

    # print(im1.shape)
    # print(im2.shape)

    #画像を縦に結合
    im_v = cv2.vconcat([im1, im2])
    cv2.imwrite('/home/user/BusLocationSystem-PersonCount/save_img/person.png', im_v)
    #im_ch = cv2.imread('/home/user/BusLocationSystem-PersonCount/save_img/person.png')
    # print(im_v.shape)

schedule.every(1).minutes.do(check_cam_num)
while True:
    try:
        schedule.run_pending()
    except cv2.error:
        n += 1
        check_error_number = str(n)
        check_error = check_error_number + "error" 
        firebase_upload.error_count(check_error)
        time.sleep(30)
        pass