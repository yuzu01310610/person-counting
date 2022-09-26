import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("./firebase_key/personcount-29e8c-firebase-adminsdk-gyj3h-8ccb136f18.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://personcount-29e8c-default-rtdb.firebaseio.com/',
    'databaseAuthVariableOverride':{
        'uid': 'my-service-worker'
    }
})

quiz_ref = db.reference('questions')
quiz_ref.child('question001').set({
        'sentence': 'This () a pen',
        'a': 'are',
        'b': 'is',
        'c': 'were',
        'd': 'was',
        'answer': 'b'
    })
