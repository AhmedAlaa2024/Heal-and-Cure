from os import abort
from flask import render_template,Blueprint,request, session,Response,make_response
from werkzeug.utils import redirect
LogoutPage=Blueprint("Logout",__name__)
@LogoutPage.route("/logout")
def logout():
    resp = make_response( redirect("/home"))
    resp.set_cookie('username', expires=0)
    session.clear()
    return resp
    
    # return redirect("/home")