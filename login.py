from sqlite3.dbapi2 import Error
from flask import app
from flask import render_template,Blueprint,session,request,redirect
LoginPage=Blueprint("login",__name__)
#the method of the page after the home page
@LoginPage.route("/login")
def login():
    if not ('ID' in session):
        return render_template("Login.html")
    else:
        return redirect("/home")

