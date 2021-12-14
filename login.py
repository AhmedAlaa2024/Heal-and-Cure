from flask import app
from flask import render_template,Blueprint
LoginPage=Blueprint("login",__name__)

@LoginPage.route("/login/<int:error>")
def login(error):
    return render_template("Login.html",Error=error)

