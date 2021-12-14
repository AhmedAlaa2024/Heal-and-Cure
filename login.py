from flask import app
from flask import render_template,Blueprint,session
LoginPage=Blueprint("login",__name__)

@LoginPage.route("/login/<int:error>")
def login(error):
    if not ('ID' in session):
        return render_template("Login.html",Error=error)
    else:
        return "not allowed"

