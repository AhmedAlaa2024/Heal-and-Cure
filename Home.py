from flask import render_template,Blueprint,request,redirect,url_for,session,make_response
from phonenumbers.phonenumber import PhoneNumber
from functions import *
from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers
from models.models import *
from config import *
#open the connection
connection = open_connection("hospital.db")
cursor = get_cursor(connection)
Database_Setup(cursor)
activate_Fks(cursor)
# =============================================
# HomePage=Blueprint("Home",__name__)
# @HomePage.route('/home',methods=["GET"])
# def mainpage():
#     return "Alaa and Sabry"



HomePage=Blueprint("Home",__name__)
@HomePage.route('/',methods=["GET", "POST"])
@HomePage.route('/home',methods=["GET", "POST"])
def mainpage():
    #count = Select_count_Department(cursor)
    connection.commit()
    DataDp = selectFromTable(cursor,'Department',Department_attributes,[Deparment.All.value],[])
    Manager_Data = select_All_manager_name(cursor)
    Donations = select_Donations(cursor)
    count =count_donations(cursor)
    Admin  = selectFromTable(cursor,'Employee',Employee_attributes,[Employee.All.value],[(Employee.Group_id.value,'A')])
    if(len(Admin) == 0):
        Admin = [(0,"","")]
    return render_template('HomePage.html',Principle = Admin,Donations =count,Manager_Data =Manager_Data,data_of_department = DataDp,no_departments = count[0][0],Data=session) # pass your Data here  like Departments & Donations & all other informations

@HomePage.route('/Departments/<ID_Department>',methods=["GET", "POST"])
def Dapartments(ID_Department):
    no_rooms = select_rooms_number(cursor,ID_Department)
    Manager_name = select_manager_name(cursor,ID_Department)
    Doctors = selectFromTable(cursor,'Employee',Employee_attributes,[Employee.All.value],[(Employee.Group_id.value,'D'),(Employee.D_id.value,ID_Department)])
    Data_Department = selectFromTable(cursor,'Department',Department_attributes,[Deparment.All.value],[(Deparment.Department_ID.value,ID_Department)])
    return render_template('Departments.html',is_loggedin = True,Manager_name =Manager_name,Data_Department=Data_Department,Doctors =Doctors,no_rooms =no_rooms[0][0]) # pass your Data here  like Departments & Donations & all other informations


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
                    Values =[Fname, Lname, 20 ,PhoneCountry,  str(phoneNumber), AddressCountry, AddressCity, AddressStreet, "M", email, password]
                    is_added = insert_general(cursor,'Patient',Patient_attributes,Columns,Values)
                    if(is_added):
                        connection.commit()
                        result1= selectFromTable(cursor,"Patient",Patient_attributes,[Patient.Patient_ID.value],[(Patient.Email.value,email),(Patient.Password.value,password)])
                        session['ID']           =result1[0][0]
                        session['Fname']        =result1[0][1]
                        session['Lname']        =result1[0][2]
                        session['Age']          =result1[0][3]
                        session['Phonecountry'] =result1[0][4]
                        session['PhoneNumber']  =result1[0][5]
                        session['Addresscountry']=result1[0][6]
                        session['Addresscity']   =result1[0][7]
                        session['Addressstreet'] =result1[0][8]
                        session['Gender']        =result1[0][9]
                        session['Password']      = password
                        session['Email']         =email
                        return redirect("/home")
                    else:
                        return redirect('/signup/0')
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
                    session['ID']           =result1[0][0]
                    session['Fname']        =result1[0][1]
                    session['Lname']        =result1[0][2]
                    session['Age']          =result1[0][3]
                    session['Phonecountry'] =result1[0][4]
                    session['PhoneNumber']  =result1[0][5]
                    session['Addresscountry']=result1[0][6]
                    session['Addresscity']   =result1[0][7]
                    session['Addressstreet'] =result1[0][8]
                    session['Gender']        =result1[0][9]
                    session['Password']      = password
                    session['Email']         =email
                    return redirect("/home")
                elif len(result2)!=0:
                    session['ID']           =result2[0][0]
                    session['Fname']        =result2[0][1]
                    session['Lname']        =result2[0][2]
                    session['Age']          =result2[0][3]
                    session['Phonecountry'] =result2[0][4]
                    session['PhoneNumber']  =result2[0][5]
                    session['Addresscountry']=result2[0][6]
                    session['Addresscity']   =result2[0][7]
                    session['Addressstreet'] =result2[0][8]
                    session['Gender']        =result2[0][9]
                    session['Goindate']      =result2[0][12]
                    session['De_id']        =result2[0][13]
                    session['Group_id']     =result2[0][14]
                    session['Password']     = password
                    session['Email']        =email
                    return redirect("/home")
                else:
                    return redirect("/login/1")