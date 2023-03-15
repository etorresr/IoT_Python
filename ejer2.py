'''
Python Firebase Course for
Beginners
https://codeloop.org/python-firebase-course-for-beginners/
'''
import pyrebase

config = {
"apiKey": "AIzaSyAjjTHMIV0y394tayvijhU-aVVcKdkIZxU",
"authDomain": "esp32-aleatorios.firebaseapp.com",
"databaseURL": "https://esp32-aleatorios-default-rtdb.firebaseio.com",
"projectId": "esp32-aleatorios",
"storageBucket": "esp32-aleatorios.appspot.com",
"messagingSenderId": "197506906640",
"appId": "1:197506906640:web:160bd9370c5300a125e895",
"measurementId": "G-GH5PT1E3Z1"
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
