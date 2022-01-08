from flask import render_template,Blueprint,request,redirect,url_for,session,make_response
from phonenumbers.phonenumber import PhoneNumber
from functions import *
from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers
from models.models import *
from config import *
import bcrypt
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
@HomePage.route('/',methods=["GET"])
@HomePage.route('/home',methods=["GET"])
def mainpage():
    #count = Select_count_Department(cursor)
    connection.commit()
    DataDp = selectFromTable(cursor,'Department',Department_attributes,[Deparment.All.value],[])
    Manager_Data = select_All_manager_name(cursor)
    Donations = select_Donations(cursor)
    count =count_donations(cursor)
    if(len(count) ==0):
        count = [("Blood",0),("Equipment",0),("Money",0)]
    Admin  = selectFromTable(cursor,'Employee',Employee_attributes,[Employee.All.value],[(Employee.Group_id.value,'A')])
    if(len(Admin) == 0):
        Admin = [(0,"","")]
    return render_template('HomePage.html',Principle = Admin,Donations =count,Manager_Data =Manager_Data,data_of_department = DataDp,no_departments = count[0][0],Data=session) # pass your Data here  like Departments & Donations & all other informations

@HomePage.route('/home',methods=["POST"])
def make_donation():
    #count = Select_count_Department(cursor)

    if (request.method == "POST"):
        if("ID" not in session):
            donationtype = request.form.get("donationtype")
            bloodtype = request.form.get("bloodtype")
            DonorFname = request.form.get("DonorFname")
            DonorLname = request.form.get("DonorLname")
            DonorEmail = request.form.get("DonorEmail")
            Donorphone = request.form.get("Donorphone")
        else:
            donationtype = request.form.get("donationtype")
            bloodtype = request.form.get("bloodtype")
            if('Group_id' not in session):
                patient_data = selectFromTable(cursor,"Patient",Patient_attributes,[Patient.All.value],[(Patient.Patient_ID.value,session["ID"])])
                DonorFname = patient_data[0][1]
                DonorLname = patient_data[0][2]
                DonorEmail = patient_data[0][10]
                Donorphone = patient_data[0][5]
            else:
                employee_data = selectFromTable(cursor,"Employee",Employee_attributes,[Employee.All.value],[(Employee.Employee_ID.value,session["ID"])])
                DonorFname = employee_data[0][1]
                DonorLname = employee_data[0][2]
                DonorEmail = employee_data[0][10]
                Donorphone = employee_data[0][5]

        Columns = [Donor.All.value]
        Values = [bloodtype,DonorFname,DonorLname,DonorEmail,Donorphone]
        is_added = insert_general(cursor,"Doner",Donor_attributes,Columns,Values)
        connection.commit()
        print (is_added)
        Columns = [Donor.Donor_ID.value]
        Values = [(Donor.Donor_Blood_Type.value,bloodtype),(Donor.Donor_Fname.value,DonorFname),
        (Donor.Donor_Lname.value,DonorLname),(Donor.Donor_Email.value,DonorEmail),(Donor.Donor_phonenumber.value,Donorphone)]
        donor_id = selectFromTable(cursor,"Doner",Donor_attributes,Columns,Values)
        print(donor_id)
        Columns = [Donation.All.value]
        Values = [get_time_now_as_text(),donationtype,donor_id[0][0],"W"]
        is_added = insert_general(cursor,"Donation" ,Donation_attributes,Columns,Values)
        connection.commit()
        print (is_added)

    return redirect("/home")

@HomePage.route('/Departments/<ID_Department>',methods=["GET"])
def Dapartments(ID_Department):
    no_rooms = select_rooms_number(cursor,ID_Department)
    Manager_name = select_manager_name(cursor,ID_Department)
    Doctors = selectFromTable(cursor,'Employee',Employee_attributes,[Employee.All.value],[(Employee.Group_id.value,'D'),(Employee.D_id.value,ID_Department)])
    Data_Department = selectFromTable(cursor,'Department',Department_attributes,[Deparment.All.value],[(Deparment.Department_ID.value,ID_Department)])
    return render_template('Departments.html',Data=session,Manager_name =Manager_name,Data_Department=Data_Department,Doctors =Doctors,no_rooms =no_rooms[0][0]) # pass your Data here  like Departments & Donations & all other informations

@HomePage.route('/Departments/<ID_Department>',methods=["POST"])
def Make_Appointment(ID_Department):
    if (request.method == "POST"):
        doctor_id = request.form.get("doctor_id")
        appointment = request.form.get("appointment")
        type = str(request.form.get("type")) + str(ID_Department)
        is_added = insert_reservation(cursor, get_time_now_as_text(), appointment, 'W', type, doctor_id, session['ID'])
        connection.commit()
        if(is_added):
            return redirect("/home")
        else:
            return "Error 404"
#from the signup page
#TODO:(validations to the input data)
@HomePage.route("/signup/home",methods=["POST"])
def SignupHome():
    if (request.method == "POST"):
                # checks on the data from the user in signup
                # take the variables
                #////////////////////////////////////////////////////////////
                password=request.form.get("password")
                # Ahmed Alaa Edited here (Start)
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                password = hashed_password.decode('utf-8')
                print("###################################################################################")
                print("Ahmed Alaa is debugging here right now! Watch Out!!")
                print("Password: ", password.decode('utf-8'))
                print("###################################################################################")
                # Ahmed Alaa Edited here (End)
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
                    Values =[Fname, Lname, 20 ,PhoneCountry,  str(phoneNumber), AddressCountry, AddressCity, AddressStreet, "M", email, password, "NULL"]
                    is_added = insert_general(cursor,'Patient',Patient_attributes,Columns,Values)
                    if(is_added):
                        connection.commit()
                        result1= selectFromTable(cursor,"Patient",Patient_attributes,[Patient.Patient_ID.value],[(Patient.Email.value,email),(Patient.Password.value,password)])
                        session['ID']           =result1[0][0]
                        session["Email"]        =email
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
                result1= selectFromTable(cursor,"Patient",Patient_attributes,[Patient.All.value],[(Patient.Email.value,email)])
                result2= selectFromTable(cursor,"Employee",Employee_attributes,[Employee.All.value],[(Employee.Email.value,email),(Employee.Password.value,password)])
                # print("###################################################################################")
                # print("Ahmed Alaa is debugging here right now! Watch Out!!")
                # hashed_password = result1[0][11]
                # hashed_password = hashed_password.encode('utf-8')
                # print("Password: ", bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))
                # print("stored Password: ", hashed_password)
                # print("###################################################################################")
                #using the session to store the data of the current user
                if len(result1)!=0:#take the complete data
                    # Ahmed Alaa Edited here! (Start)
                    if bcrypt.checkpw(password.encode('utf-8'), result1[0][11].encode('utf-8')):
                    # Ahmed Alaa Edited here! (End)
                        session['ID']           =result1[0][0]
                        session["Email"]        =email
                        return redirect("/home")
                elif len(result2)!=0:
                    session['ID']           =result2[0][0]
                    session['Group_id']     =result2[0][15]
                    session["Email"]        =email
                    return redirect("/home")
                else:
                    return redirect("/login/1")