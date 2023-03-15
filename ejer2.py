'''
Python Firebase Course for
Beginners
https://codeloop.org/python-firebase-course-for-beginners/
'''
import pyrebase

config = {
"apiKey": "AIdkIZxU",
"authDomain": "esp32-aleatorios.firebaseapp.com",
"databaseURL": "https://esp3db.firebaseio.com",
"projectId": "esp32-aleatorios",
"storageBucket": "esp32-aleatorios.appspot.com",
"messagingSenderId": "197640",
"appId": "1:19740:web:160bd9a125e895",
"measurementId": "G-G3Z1"
}
#create authetication
firebase = pyrebase.initialize_app(config)
#accesing database in firebase
db = firebase.database()
data = {"name":"Ignacio Altamirano"}
data1 = {"job":"Periodista"}
db.child("users").push(data)
db.child("users").push(data1)
print("Data added to real time database ")
