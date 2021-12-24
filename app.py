from flask import Flask,request,render_template,url_for,session,Blueprint
import os
from login import LoginPage
from Home import HomePage
from SignUp import signupPage
from profile import ProfilePage
from Logout import LogoutPage
from werkzeug.utils import redirect
from utils import *
from config import *
connection = open_connection("hospital.db")
cursor = get_cursor(connection)

Database_Setup(cursor)

app=Flask(__name__)
app.secret_key=os.urandom(32)
# The bluePrint to help us to connect the files  
app.register_blueprint(HomePage)
app.register_blueprint(LoginPage)
app.register_blueprint(signupPage)
app.register_blueprint(ProfilePage)
app.register_blueprint(LogoutPage)
if __name__=="__main__":
    app.run(debug=True)