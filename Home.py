from flask import render_template,Blueprint,request,redirect,url_for,session
from phonenumbers.phonenumber import PhoneNumber
from functions import *
from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers
from Models.models import *
from config import *
#open the connection
connection = open_connection("hospital.db")
cursor = get_cursor(connection)
Database_Setup(cursor)
# =============================================
HomePage=Blueprint("Home",__name__)
@HomePage.route('/home',methods=["GET"])
def mainpage():
    return "Alaa and Sabry"
#from the signup page
#TODO:(validations to the input data)
@HomePage.route("/signup/home",methods=["POST"])
def SignupHome():
    if (request.method == "POST"):
                # checks on the data from the user in signup
                # take the variables
                #////////////////////////////////////////////////////////////
                password=request.form.get("password")
                email=request.form.get("email")
                Fname=request.form.get('Fname')
                Lname=request.form.get('Lname')
                AddressCountry=request.form.get('country')
                AddressCity=request.form.get('city')
                AddressStreet=request.form.get('street')
                PhoneCountry="+"+str(codes[recode(AddressCountry)]) #to check on the phone and get the name of his mather and the data of the birth
                phoneNumber =request.form.get('Number')
                #///////////////////////////////////////////////////////////////////
                phone = phonenumbers.parse(PhoneCountry+phoneNumber)
                if not(has_numbers(Fname)) and not(has_numbers(Lname)and(phonenumbers.is_valid_number(phone))):
                    #the query of the insert
                    # and then store the data in the session 
                    Columns = [Patient.All.value]
                    Values =[Fname, Lname, 20, "+"+PhoneCountry,  str(phoneNumber), AddressCountry, AddressCity, AddressStreet, "M", email, password]
                    insert_general(cursor,'Patient',Patient_attributes,Columns,Values)
                    # session['ID']=id
                    session['Password']= password
                    session['Email']=email
                    session['Fname']=Fname
                    session['Lname']=Lname
                    return render_template("HomePage.html")
                else:
                    return redirect('/signup/1')
@HomePage.route("/login/home",methods=["POST"])
def LoginHome():
    if(request.method=="POST"):
                # from the login page
                #TODO:query to ckeck if the email and the password is correct
                #if the data is not correct the will direct to the login ag
                password=request.form.get("password")
                email=request.form.get("email")
                result1= selectFromTable(cursor,"Patient",Patient_attributes,[Patient.All.value],[(Patient.Email.value,email),(Patient.Password.value,password)])
                result2= selectFromTable(cursor,"Employee",Employee_attributes,[Employee.All.value],[(Employee.Email.value,email),(Employee.Password.value,password)])
                #using the session to store the data of the current user
                if len(result1)!=0:#take the complete data
                    session['ID']=result1[0][0]
                    session['Password']= password
                    session['Email']=email
                    return render_template("HomePage.html")
                elif len(result2)!=0:
                    session['ID']=result2[0][0]
                    session['Password']= password
                    session['Email']=email
                    return render_template("HomePage.html")
                else:
                    return redirect("/login/1")
