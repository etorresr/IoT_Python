'''
Python Firebase Course for
Beginners
https://codeloop.org/python-firebase-course-for-beginners/
'''
import pyrebase

config = {
"apiKey": "AIkIZxU",
"authDomain": "esp32-aleatorios.firebaseapp.com",
"databaseURL": "https://esdb.firebaseio.com",
"projectId": "esp32-aleatorios",
"storageBucket": "esp32-aleatorios.appspot.com",
"messagingSenderId": "1940",
"appId": "1:197640:web:1a125e895",
"measurementId": "G-GH3Z1"
}

firebase = pyrebase.initialize_app(config)
#accesing database in firebase
db = firebase.database()
#reading some atributes of the onKey elements
all_users = db.child("users").get()
for users in all_users.each():
    print(users.val())
    print(users.key())
