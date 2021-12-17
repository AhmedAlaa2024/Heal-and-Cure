from os import abort
from sqlite3.dbapi2 import Cursor
from flask import render_template,Blueprint,request, session
from phonenumbers.phonenumber import PhoneNumber
from defs import Patient
from functions import *
from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers
from models.models import Update
from config import *
ProfilePage=Blueprint("profile",__name__)
'''
I already have the data in the session and i will detect if the user is patient or doctor by using group id
id=1 ----> will edit the data
id=0 -----> will go to the profile normally
The methods of the page if the method is Post and id=1 then the user will come from the profile page to profile edit Page to edit the data
if the method is post and the id=0 then the user will come from the update page to the normal profile page 
if the method is Get and id=0 then the user will come form the home page 
call the query Update and if the query is succeed it will return the bool value is_updated=true to tall me and i will save the new data in the session  
Some NOTES: 1-if the user not login the link of the profile page will lead to login first if he attemps to get profile will the URI
2- in the profile the job will decide according to the GroupID 
3- 
'''
#start the connection 
connection = open_connection("hospital.db")
cursor = get_cursor(connection)
Database_Setup(cursor)

@ProfilePage.route("/profile/<int:id>",methods=["POST","GET"])
def profile(id):
    if "ID" in session: #Edit page
        if id==1 and request.method=="POST":
            return render_template("Profile.html",edit=id,data=session)
        elif id==0: #main profile page
            if request.method=="POST":
                Fname=request.form.get("Fname")
                Lname=request.form.get("Lname")
                email=request.form.get("email")
                password=request.form.get("password")
                phoneNumber =request.form.get("Phone")
                Addresscountry=request.form.get("Addresscountry")
                Addressstreet=request.form.get("Addressstreet")
                Addresscity=request.form.get("Addresscity")
                PhoneCountry="+"+str(codes[recode(Addresscountry)]) 
                phone = phonenumbers.parse(PhoneCountry+phoneNumber)
                if not(has_numbers(Fname)) and not(has_numbers(Lname)and(phonenumbers.is_valid_number(phone))):
                    new_info=['"'+Fname+'"','"'+Lname+'"','"'+email+'"','"'+password+'"',phoneNumber,'"'+Addresscountry+'"','"'+Addresscity+'"','"'+Addressstreet+'"']
                    is_upadated = Update(cursor,'Patient',[Patient.Patient_ID.value],[session['ID']],[Patient.FNAME.value,Patient.lNAME.value,Patient.Email.value,Patient.Password.value,Patient.PhoneNumber.value,Patient.Addresscountry.value,Patient.Addresscity.value,Patient.Addressstreet.value],new_info)
                    if is_upadated:
                        connection.commit()
                        session["Fname"]=Fname
                        session["Lname"]=Lname
                        session["Email"]=email
                        session["password"]=password
                        session["PhoneNumber"]=phoneNumber
                        session["Addresscountry"]=Addresscountry
                        session["Addressstreet"]=Addressstreet
                        session["Addresscity"]=Addresscity
                        return render_template("Profile.html",edit=0,data=session)
                    else:
                        return render_template("Profile.html",edit=id,data=session)
                else :
                    return render_template("Profile.html",edit=id,data=session)
            else :
                return render_template("Profile.html",edit=id,data=session)
        else:
            return render_template("Profile.html",edit=id,data=session)
    else:
        return "login first"