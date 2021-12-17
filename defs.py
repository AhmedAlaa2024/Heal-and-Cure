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
    Donor_ID=7
    Donor_Blood_Type=1
    Donor_Street=2
    Donor_City=3
    Donor_Country=4
    Donor_Fname=5
    Donor_Lname=6

Donor_attributes={
    0:'All',
    7:'Donor_ID',
    1:'Donor_Blood_Type',
    2:'Donor_Street',
    3:'Donor_City',
    4:'Donor_Country',
    5:'Donor_Fname',
    6:'Donor_Lname'
}

class Donation(enum.Enum):
    All=0
    Donation_ID=1
    Donation_Date=2
    Donation_Donation_Type=3
    Donation_Donor_ID=4


Donation_attributes={
    0:'All',
    1:'Donation_ID',
    2:'Donation_Date',
    3:'Donation_Donation_Type',
    4:'Donation_Donor_ID'
}

class Resrvation(enum.Enum):
    All=0
    Rservation_Id=1
    Resrvation_Date=2
    Resrvation_illness=3
    Resrvation_Treatment=4
    Resrvation_Doctor_ID=5
    Resrvation_Patient_ID=6

Resrvation_attributes={
    0:'All',
    1:'Rservation_Id',
    2:'Resrvation_Date',
    3:'Resrvation_illness',
    4:'Resrvation_Treatment',
    5:'Resrvation_Doctor_ID',
    6:'Resrvation_Patient_ID',
    }

####################################################################################
Department_attributes = {0:"*",1:"ID",2:"FNAME",3:"lNAME",4:"Manager_id",5:"Start_Date"}
Patient_attributes = {0:"*",1:"ID",2:"FNAME",3:"lNAME",4:"AGE",5:"Phonecountry"
,6:"PhoneNumber",7:"Addresscountry",8:"Addresscity",9:"Addressstreet",10:"GENDER",11:"Email",12:"Password"}
Employee_attributes ={0:"*",1:"ID",2:"FNAME",3:"lNAME",4:"AGE",5:"Phonecountry"
,6:"PhoneNumber",7:"Addresscountry",8:"Addresscity",9:"Addressstreet",10:"GENDER",11:"Email",12:"Password",13:"JoinDate",14:"D_id",15:"Group_id"}
Prescription_attributes = {0:"*",1:"ID",2:"DATE",3:"Illness",4:"Treatment",5:"Doc_id",6:"Patient_id"}
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
    JoinDate = 13
    D_id = 14
    Group_id =15
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

class Deparment (enum.Enum):
    All = 0
    Department_ID = 1
    FNAME = 2
    lNAME = 3
    Manager_id = 4
    Start_Date = 5

class Prescription (enum.Enum):
    All = 0
    ID = 1
    Illness = 2
    Treatment = 3
    Doc_id = 4
    Patient_id = 5
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
    Cholestrol = 2
    BloodPressure = 4
    Depression = 5
    MaxHR = 6

PatientStatus_attributes={
    0:"*",
    1: "Patient_ID",
    2: "Diabetes",
    3:"Cholestrol",
    4:"BloodPressure",
    5:"Depression",
    6:"MaxHR"
}

Dicts={
    'Patient':Patient_attributes,
    'Prescription':Prescription_attributes,
    'Reservation' : Resrvation_attributes,
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

