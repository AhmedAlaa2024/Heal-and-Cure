from flask import Flask,request,render_template,url_for,session,Blueprint
import os
from login import LoginPage
from Home import HomePage
from SignUp import signupPage
from profile import ProfilePage
from werkzeug.utils import redirect
from utils import *
from config import *
SECRET_KEY=os.urandom(32)
connection = open_connection("hospital.db")
cursor = get_cursor(connection)

Database_Setup(cursor)

app=Flask(__name__)

# The bluePrint to help us to connect the files  
app.register_blueprint(HomePage)
app.register_blueprint(LoginPage)
app.register_blueprint(signupPage)
app.register_blueprint(ProfilePage)

if __name__=="__main__":
    app.run(debug=True)