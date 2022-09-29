import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import datetime


def upload_firebase(person_number):
    #cred = credentials.Certificate("./firebase_key/personcount-29e8c-firebase-adminsdk-gyj3h-8ccb136f18.json")
    
    if not firebase_admin._apps:
        cred = credentials.Certificate("./firebase_key/personcount-29e8c-firebase-adminsdk-gyj3h-8ccb136f18.json")
        firebase_admin.initialize_app(cred,{
            'databaseURL':'https://personcount-29e8c-default-rtdb.firebaseio.com/',
        })

    dt_now = datetime.datetime.now()
    print(dt_now)
    quiz_ref = db.reference('/user')

    quiz_ref.child('1').update({
            'date': dt_now.strftime('%Y年%m月%d日 %H:%M:%S'),
            'total': person_number,
        })

    return

def counting_person(check_num):

    check_num = int(check_num[0])
    upload_firebase(check_num)
    #     print("OK!")
    #     upload_firebase(check_num)

    return

def no_counting_person(check_num):

    upload_firebase(check_num)

    return