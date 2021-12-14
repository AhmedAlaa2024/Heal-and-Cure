from flask import render_template,Blueprint,request
ProfilePage=Blueprint("profile",__name__)

@ProfilePage.route("/profile/<id>")
def profile(id):
    return id