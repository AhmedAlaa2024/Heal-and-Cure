from os import abort
from flask import render_template,Blueprint,request, session
ProfilePage=Blueprint("profile",__name__)
'''
I already have the data in the session and i will detect if the user is patient or doctor by using group id
id=1 ----> will edit the data
id=0 -----> will go to the profile normally
'''

@ProfilePage.route("/profile/<int:id>",methods=["POST","GET"])
def profile(id):
    if "ID" in session:
        if id==1 and request.method=="POST":
            return render_template("Profile.html",edit=id,data=session)
        elif id==0:
            if request.method=="POST":
                Fname=request.form.get("Fname")
                Lname=request.form.get("Lname")
                email=request.form.get("email")
                password=request.form.get("password")
                Addresscountry=request.form.get("Addresscountry")
                Addressstreet=request.form.get("Addressstreet")
                Addresscity=request.form.get("Addresscity")
                #validations bolbol here
                ls=session
                ls["Fname"]=Fname
                ls["Lname"]=Lname
                ls["Email"]=email
                ls["password"]=password
                ls["Addresscountry"]=Addresscountry
                ls["Addressstreet"]=Addressstreet
                ls["Addresscity"]=Addresscity
                return render_template("Profile.html",edit=id,data=ls)
            else:
                return render_template("Profile.html",edit=id,data=session)
        else:
            return "not allowed"
    else:
        return "login first"
#when click edit button