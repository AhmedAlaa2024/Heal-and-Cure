from os import abort
from sqlite3.dbapi2 import Cursor
from flask import render_template,Blueprint,request, session
from phonenumbers.phonenumber import PhoneNumber
from werkzeug.utils import redirect
from defs import Patient
from functions import *
from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers
from models.models import *
from config import *
from datetime import datetime
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

@ProfilePage.route("/profile/<string:id>",methods=["POST","GET"])
def profile(id):
    if "ID" in session: #Edit page
        if("Group_id" not in session):
            # the query to get the status
            result3= selectFromTable(cursor,"PatientStatus",PatientStatus_attributes,[PatientStatus.All.value],[(PatientStatus.Patient_ID.value,session['ID'])])
            if len(result3)!=0:
                session["disease1"]=result3[0][0]
                session["disease2"]=result3[0][1]
                session["disease3"]=result3[0][2]
                session["disease4"]=result3[0][3]
                session["disease5"]=result3[0][4]
            # Queries to the prescripation
            session["DoctorName"]="Bolbol"
            session["DATE"]="28-10-2000"
            session["Treatment"]="eb3d 3n alaa"
        if id=="Edit" and request.method=="POST":
            return render_template("Profile.html",edit=id,data=session)
        elif id=="mainprofile": #main profile page
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
                    if("Group_id" not in session):
                        is_upadated = Update(cursor,'Patient',[Patient.Patient_ID.value],[session['ID']],[Patient.FNAME.value,Patient.lNAME.value,Patient.Email.value,Patient.Password.value,Patient.PhoneNumber.value,Patient.Addresscountry.value,Patient.Addresscity.value,Patient.Addressstreet.value],new_info)
                    else:
                        is_upadated = Update(cursor,'Employee',[Employee.Employee_ID.value],[session['ID']],[Employee.FNAME.value,Employee.lNAME.value,Employee.Email.value,Employee.Password.value,Employee.PhoneNumber.value,Employee.Addresscountry.value,Employee.Addresscity.value,Employee.Addressstreet.value],new_info)
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
            return redirect("/home")
    else:
        return "login first"

#the profile page of the admin 
#when the home page is ended i will add a button to the profile page and i will select which route should be called
#if Group_id==A  


@ProfilePage.route("/AdminProfile/<Operation>",methods=["POST","GET"])
def Admin(Operation):
    if session["Group_id"]=="A":
        if(Operation=="Department"):
            #query to get the data of the departments
            Result= selectFromTable(cursor,'Department',Department_attributes,[Deparment.All.value] ,[] )
            return render_template("ShowDataToAdmin.html",Type=Operation,Data=Result)
        elif Operation=="Employee":
            #query to get the data of the employees
            Result= selectFromTable(cursor,'Employee',Employee_attributes,[Employee.All.value] ,[] )
            return render_template("ShowDataToAdmin.html",Type=Operation,Data=Result)
        
    else:
        return "you are not allowed"

#route to insert the Departments by the Admin
@ProfilePage.route("/AdminProfile/Departments/<string:operation>",methods=["POST","GET"])
def AdminSettingsDepartments(operation):
    if session["Group_id"]=="A":
        if operation=="Insert":
            return render_template("AdminSettings.html",SSNList=session,Type="Departments",selector=operation)
    else:
        return "you are not allowed"
#route to insert the employees by the Admin
@ProfilePage.route("/AdminProfile/Employees/<string:operation>",methods=["POST","GET"])
def AdminSettingsEmployees(operation):
    if session["Group_id"]=="A":
        if operation=="Insert":
            return render_template("AdminSettings.html",SSNList=session,Type="Employees",selector=operation)
    else:
        return "you are not allowed"
#rout to check the data form the Admin
@ProfilePage.route("/AdminProfile/checkdata/<string:opertaion>",methods=["POST"])
def AdmincheckoutData():
    if request.form.get("Departmentname") !=None :
        #the data of the department
        Departmentname=request.form.get("Departmentname")
        Startdate=request.form.get("StartDate")
        # I just added department manager manually to test the validations
        Departmentmanager=1#request.form.get("Manager") 
        DepartmentDes=request.form.get("Descripation")
        #Bolbol check the data and insert it in the database
        #check the department manager and check the start date of him 
        Employee_ID=cursor.execute('''select ID from Employee ;''').fetchall()
        if(not (Departmentmanager in Employee_ID[0])):
            return "the manager doesn't exist in Employees"
        Employee_joinDate = cursor.execute('''select JoinDate from Employee where ID = '''+str(Departmentmanager)+''';''').fetchall()
        Startdate1=datetime.strptime(str(Startdate),'%Y-%m-%d')
        if(not(datetime.strptime(Employee_joinDate[0][0],'%d-%m-%Y')<Startdate1)):
            return "this Employee joined the hospital after this date " 
        # I have checked the data but will change the return of faults
        cursor.execute('''insert into Department values("'''+str(Departmentname)+'''",'''+str(Departmentmanager)+''',"'''+str(Startdate1)+'''");''')
        #fix the auto increment fault
        connection.commit()
        return redirect("/AdminProfile/Department")
        
    else:
        # the data of the employee
        Fname=request.form.get("Fname")
        Lname=request.form.get("Lname")
        Email=request.form.get("Email")
        Password=request.form.get("Password")
        Manager=request.form.get("Manager")
        Age=request.form.get("Age")
        PhonNumber=request.form.get("PhonNumber")
        Addresscountry=request.form.get("Addresscountry")
        Addressstreet=request.form.get("Addressstreet")
        Addresscity=request.form.get("Adresscity")
        #Bolbol check the data and insert it in the database
        PhoneCountry="+"+str(codes[recode(Addresscountry)]) 
        phone = phonenumbers.parse(PhoneCountry+PhonNumber)
        if not(has_numbers(Fname)) and not(has_numbers(Lname)and(phonenumbers.is_valid_number(phone))):
            info=['"'+Fname+'"','"'+Lname+'"','"'+Email+'"','"'+Password+'"',PhonNumber,'"'+Addresscountry+'"','"'+Addresscity+'"','"'+Addressstreet+'"']
            cursor.execute('''insert into Employee values (?,?,?,?,?,?,?,?)''',info)
            #it doesn't work yet until add the department id
            connection.commit()
        return redirect("/AdminProfile/Employee")
# route to delete the Departments by using the id
@ProfilePage.route('/DeleteDepartment/<int:id>')
def deleteDepartment(id):
    # query to delete
    return redirect("/AdminProfile/Department")
# route to delete the Employees by using the id
@ProfilePage.route('/DeleteEmployee/<int:id>')
def deleteEmployee(id):
    # query to delete
    return redirect("/AdminProfile/Employee")
#route to edit the data of the Employees
@ProfilePage.route('/EditEmployee/<int:id>')
def EditEmployee(id):
    # query to get the data of the id
    employee_Data = selectFromTable(cursor,'Employee',Employee_attributes,[Employee.All.value] ,[(Employee.Employee_ID.value,id)] )
    return render_template("EditData.html",Type="Employees",SSNList =session,DataEmp=employee_Data)
    #bolbol get the data and check it
#route to edit the data of the Departments
@ProfilePage.route('/EditDepartment/<int:id>')
def EditDepartment(id):
    # query to retrive the data of the id
    department_Data = selectFromTable(cursor,'Department',Department_attributes,[Deparment.All.value] ,[(Deparment.Department_ID.value,id)] )
    return render_template("EditData.html",Type="Departments",SSNList=session,DataDP=department_Data)
    #bolbol get the data and check it