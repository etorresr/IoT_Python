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

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
#get the valid email and password from the user
email = input("Please Enter Your Email : ")
password = input("Please Enter Your Password : ")
#and authenticate the user
user = auth.create_user_with_email_and_password(email, password)
print("User Created Successfully")
#For accesing the firebase after the creation of user by email
try:
    signin = auth.sign_in_with_email_and_password(email, password)
    print("Sign In Was Successfull")
except:
    print("Invalid user or password")
#Verification of user
auth.send_email_verification(signin['idToken'])
print("Email Verification Has Been Sent")
#Reset the password
auth.send_password_reset_email(email)
print("We have sent an email, check your inbox ")
