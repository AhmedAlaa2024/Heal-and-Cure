from flask import app
from flask import render_template,Blueprint,session,request,redirect
LoginPage=Blueprint("login",__name__)
#the method of the page after the home page
@LoginPage.route("/login/<int:error>")
def login(error):
    if not ('ID' in session):
        return render_template("Login.html")
    else:
        return redirect("/home")

