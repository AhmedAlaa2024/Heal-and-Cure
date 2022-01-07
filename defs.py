import enum
from models import *
import models

class Room(enum.Enum):
    All=0
    Room_ID=1
    Last_stay=2
    Available=3
    Department_ID=4

Room_attributes={
    0:'All',
    1:"Room_ID",
    2:"Last_stay",
    3:'Available',
    4:'Department_ID'}



class Examination(enum.Enum):
    All=0
    Examination_ID=1
    Examination_Date=2
    Result=3
    Validity=4
    Reservation_ID=5
    Patient_ID=6
    Department_ID=7

Examination_attributes={
    0:'All',
    1:'Examination_ID',
    2:'Examination_Date',
    3:'Result',
    4:'Validity',
    5:'Reservation_ID',
    6:'Patient_ID',
    7:'Department_ID'
}



class Examintion_and_Operation(enum.Enum):
    All=0
    Examination_Id=1
    Operation_ID=2

Examintion_and_Operation_attributes={
    0:'All',
    1:'Examination_Id',
    2:'Operation_ID'
}

class Operation(enum.Enum):
    All=0
    Operation_ID=1
    Operation_State=2
    Operation_start_Time=3
    Operation_End_Time=4
    Operation_Priority=5
    Operation_prequisites=6
    Res_ID=7

Operation_attributes={
    0:'All',
    1:'Operation_ID',
    2:'Operation_State',
    3:'Operation_start_Time',
    4:'Operation_End_Time',
    5:'Operation_Priority',
    6:'Operation_prequisites',
    7:'Res_ID'
}


class Donor(enum.Enum):
    All=0
    Donor_ID=1
    Donor_Blood_Type=2
    Donor_Fname=3
    Donor_Lname=4
    Donor_Email=5
    Donor_phonenumber= 6

Donor_attributes={
    0:'*',
    1:'ID',
    2:'BloodType',
    3:'FNAME',
    4:'lNAME',
    5:'Email',
    6:'Phonenumber'
}

class Donation(enum.Enum):
    All=0
    Donation_ID=1
    Donation_Date=2
    Donation_Donation_Type=3
    Donation_Donor_ID=4
    state=5


Donation_attributes={
    0:'*',
    1:'ID',
    2:'DonationDate',
    3:'DonationType',
    4:'DonarId',
    5:'statee'
}
class Reservation(enum.Enum):
    All=0
    ID=1
    Date=2
    Appointment=3
    state=4
    Type=5
    Doctor_id=6
    Patient_id=7
    Prescription_id=8
    Room_id=9

Reservation_attributes={
    0:"*",
    1:"ID",
    2:"Date",
    3:"Appointment",
    4:"state",
    5:"Type",
    6:"Doctor_id",
    7:"Patient_id",
    8:"Prescription_id",
    9:"Room_id"
    }

####################################################################################
Department_attributes = {0:"*",1:"ID",2:"Department_Name",3:"Manager_id",4:"Start_Date",5:"image"}
Patient_attributes = {0:"*",1:"ID",2:"FNAME",3:"lNAME",4:"AGE",5:"Phonecountry"
,6:"PhoneNumber",7:"Addresscountry",8:"Addresscity",9:"Addressstreet",10:"GENDER",11:"Email",12:"Password",13:"image"}
Employee_attributes ={0:"*",1:"ID",2:"FNAME",3:"lNAME",4:"AGE",5:"Phonecountry"
,6:"PhoneNumber",7:"Addresscountry",8:"Addresscity",9:"Addressstreet",10:"GENDER",11:"Email",12:"Password",13:"image",14:"JoinDate",15:"D_id",16:"Group_id"}
Prescription_attributes = {0:"*",1:"ID",2:"DATE",3:"Illness",4:"Treatment",5:"Reservation_id"}
GlobalContract_attributes = {0:"*",1:"ID",2:"Terms",3:"Penalty"}
EmployeeContract_attributes = {0:"*",1:"ID",2:"E_ID",3:"GlobalContract_ID"}
PatientContract_attributes = {0:"*",1:"P_ID",2:"E_ID",3:"Doc_ID",4:"GlobalContract_ID",5:"OP_ID"}

# Enums
class Employee(enum.Enum):
    All = 0
    Employee_ID = 1
    FNAME = 2
    lNAME = 3
    Age = 4
    Phonecountry = 5    
    PhoneNumber = 6
    Addresscountry = 7
    Addresscity = 8
    Addressstreet = 9
    GENDER = 10
    Email = 11
    Password = 12
    image=13
    JoinDate = 14
    D_id = 15
    Group_id =16

class Patient (enum.Enum):
    All = 0
    Patient_ID = 1
    FNAME = 2
    lNAME = 3
    Age = 4
    Phonecountry = 5    
    PhoneNumber = 6
    Addresscountry = 7
    Addresscity = 8
    Addressstreet = 9
    GENDER = 10
    Email = 11
    Password = 12
    image=13

class Deparment (enum.Enum):
    All = 0
    Department_ID = 1
    Department_Name = 2
    Manager_id = 3
    Start_Date = 4
    image=5

class Prescription (enum.Enum):
    All = 0
    ID = 1
    Date = 2
    Illness = 3
    Treatment = 4
    Reservation_id = 5
class GlobalContract (enum.Enum):
    All = 0
    GlobalContract_ID = 1
    Terms= 2
    Penalty =3 
class EmployeeContract (enum.Enum):
    All = 0
    ID = 1
    E_ID=2
    GlobalContract_ID=3


class PatientContract (enum.Enum):
    All = 0
    P_ID = 1
    E_ID = 2
    Doc_ID=3
    GlobalContract_ID=4
    OP_ID=5




####################################################################################




class PatientStatus (enum.Enum):
    All = 0
    Patient_ID = 1
    Diabetes = 2
    Cholestrol = 3
    Blood_Pressure = 4
    Depression = 5
    Max_Heart_Rate = 6

PatientStatus_attributes={
    0:"*",
    1: "PatientID",
    2: "Diabetes",
    3:"Cholestrol",
    4:"Blood_Pressure",
    5:"Depression",
    6:"Max_Heart_Rate"
}

Dicts={
    'Patient':Patient_attributes,
    'Prescription':Prescription_attributes,
    'Reservation' :Reservation_attributes,
    'Department' : Department_attributes,
    'Employee' : Employee_attributes,
    'Contracts' : GlobalContract_attributes,
    'Emplyee_Contract' : EmployeeContract_attributes,
    'Room' : Room_attributes,
    'Examination': Examination_attributes,
    'Examination_Operation' : Examintion_and_Operation_attributes,
    'Operations' : Operation_attributes,
    'Donor' : Donor_attributes,
    'Donation' : Donation_attributes,
    'PatientStatus':PatientStatus_attributes
}

