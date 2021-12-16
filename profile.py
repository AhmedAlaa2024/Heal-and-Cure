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
ProfilePage=Blueprint("profile",__name__)
'''
I already have the data in the session and i will detect if the user is patient or doctor by using group id
id=1 ----> will edit the data
id=0 -----> will go to the profile normally
'''

@ProfilePage.route("/profile/<int:id>",methods=["POST","GET"])
def profile(id):
    if "ID" in session:
        if id==0 and request.method=="POST":
            return render_template("Profile.html",edit=id,data=session)
        elif id==1:
            if request.method=="POST":
                Fname=request.form.get("Fname")
                Lname=request.form.get("Lname")
                email=request.form.get("email")
                password=request.form.get("password")
                phoneNumber =request.form.get("Phone")
                Addresscountry=request.form.get("Addresscountry")
                Addressstreet=request.form.get("Addressstreet")
                Addresscity=request.form.get("Addresscity")
                #validations bolbol here
                PhoneCountry="+"+str(codes[recode(Addresscountry)]) #to check on the phone and get the name of his mather and the data of the birth
                phone = phonenumbers.parse(PhoneCountry+phoneNumber)
                if not(has_numbers(Fname)) and not(has_numbers(Lname)and(phonenumbers.is_valid_number(phone))):
                    Fname='"'+Fname+'"'
                    Lname='"'+Lname+'"'
                    email='"'+email+'"'
                    password='"'+password+'"'
                    Addresscountry='"'+Addresscountry+'"'
                    Addressstreet='"'+Addressstreet+'"'
                    Addresscity='"'+Addresscity+'"'
                    new_info=[Fname,Lname,email,password,phoneNumber,Addresscountry,Addresscity,Addressstreet]
                    is_upadated = Update(Cursor,'Patient',[Patient.Patient_ID.value],[session['ID']],[Patient.FNAME.value,Patient.lNAME.value,Patient.Password.value,Patient.PhoneNumber,Patient.Addresscountry.value,Patient.Addresscity.value,Patient.Addressstreet.value],new_info)
                    if is_upadated:
                        ls=session
                        ls["Fname"]=Fname
                        ls["Lname"]=Lname
                        ls["Email"]=email
                        ls["password"]=password
                        ls["Addresscountry"]=Addresscountry
                        ls["Addressstreet"]=Addressstreet
                        ls["Addresscity"]=Addresscity
                        return render_template("Profile.html",edit=0,data=ls)
                    else:
                        return render_template("Profile.html",edit=id,data=session)
                else :
                    return render_template("Profile.html",edit=id,data=session)
            else :
                return "not allowed"+str(id)+request.method
        else:
            return "not allowed" + str(id)+request.method
    else:
        return "login first"
#when click edit button