from os import abort
from flask import render_template,Blueprint,request, session
from werkzeug.utils import redirect
LogoutPage=Blueprint("Logout",__name__)
@LogoutPage.route("/logout")
def logout():
    session.clear()
    return redirect("/home")