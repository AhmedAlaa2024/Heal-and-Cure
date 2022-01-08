from config import *
from utils import *
from sqlite3 import Error
from defs import *
import enum
# Dictionaries


def activate_Fks(cursor):
    query = "PRAGMA foreign_keys = ON;"
    try:
        cursor.execute(query)
        return True
    except Error as e:
        print(e)
        return False
#===================================================================================================
# Function: selectFromTable
# Input:    cursor ,string:table_name , list:Columns -> [Enum_Name.attribute.value,...]
#           listof tuples:Selectors -> [(Enum_name.attribute.value,Value of attribute),(...),..]
# Output:   2D list of tuples result / json file
# Prerequistes: None
# Description: Select any attribute(s) from any Table under any condition related to same Table only with AND only
# status: Not Tested
#===================================================================================================

#Columns = [Employee.Age.value,Employee.PhoneNumber.value]
#Selectors = [(Employee.FNAME.value,"Ahmed"),(Employee.lNAME.value,"Alaa")]

def selectFromTable(cursor,table_name,table_attributes,Columns,Selectors):
    Q1 = ''''''
    Q2 = ''' Where '''
    if(len(Columns) <1):
        return []
    for i in range(len(Columns)-1):
        Q1 += table_attributes[Columns[i]]
        Q1 +=","
    Q1 += table_attributes[Columns[-1]]
    if(len(Selectors) <1):
        Q2 =''''''
    else:
        for i in range(len(Selectors)-1):
            if(isinstance(Selectors[i][1], int)):
                Q2 += table_attributes[Selectors[i][0]] + "="+str(Selectors[i][1])+" AND "
            else:
                 Q2 += table_attributes[Selectors[i][0]] + "='"+Selectors[i][1]+"' AND "
        if(isinstance(Selectors[-1][-1], int)):
            Q2 += table_attributes[Selectors[-1][0]] + "="+ str(Selectors[-1][1])
        else:
            Q2 += table_attributes[Selectors[-1][0]] + "='"+ Selectors[-1][1]+"'"

    query = 'select '+Q1+' from ' + table_name +Q2+';'
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return result
    except Error as e:
        print(e)
        return []



# Function: insert General
# Input:    string: Table name ,list:list_1 -> values in to be inserted in patient 
# Output:   
# Prerequistes: None
# Description: insert new tuple in any table
# status: Not Tested
#===================================================================================================
#Columns = [Employee.Age.value,Employee.PhoneNumber.value]
# values = ["Ahmed","Sabry" ,....]
def insert_general(cursor,table_name ,table_attributes,Columns,Values):
    Q1 =''''''
    Q2 = '''?'''
    if(Columns[0] == 0):
        Q1 ='''( '''+table_attributes[2]
        for i in range(3,len(table_attributes)):
            Q1 +=","
            Q1 += table_attributes[i]
        Q1 += ''')'''

    else:
        Q1 +='''('''
        Q1 += table_attributes[Columns[0]]
        for i in range(1,len(Columns)):
            Q1 += ''' , '''+table_attributes[Columns[0]]
        Q1+= ''') '''    
    for i in range(1,len(Values)):
        Q2 +=''','''+'''?'''
    query = '''INSERT INTO '''+table_name+ Q1+''' VALUES(''' + Q2 +''')'''
    try:
        cursor.execute(query,Values)
        return True
    except Error as e:
        print(e)
        return False

# ------------------------- Prescription --------------------------------------
# 1] Retreive From Prescription according to Patient & his Email {Can be General not only Email}
# Before insertion  we must Check Doc_ID is for Doctor Group_ID = 'D'

def SelecT_ALL_Prescription_Patient(cursor,Email):

    #query = '''Select * from Prescription Ps,Patient P where Ps.Patient_id = P.ID And P.Email='''+"'"+Email+"'"
    #cursor.execute(query)
    query = '''Select * from Prescription Ps,Patient P where Ps.Patient_id = P.ID And P.Email=?;'''
    cursor.execute(query,[Email])
    result = cursor.fetchall()
    print (result)
    return result

def Select_From_Prescription_Patient(cursor,Email,Columns = []):

    Q1 = ''''''
    if (len(Columns) > 0):
        Q1 += Prescription_attributes[Columns[0]]
        for i in range(1,len(Columns)):
            Q1 += ''','''
            Q1 += Prescription_attributes[Columns[i]]
    else:
        Q1 += Prescription_attributes[2]
        for i in range(3,len(Prescription_attributes)):
            Q1 += ''','''
            Q1 += Prescription_attributes[i]
    query = '''Select '''+Q1+''' from Prescription Ps,Patient P where Ps.Patient_id = P.ID And P.Email='''+"'"+Email+"';"
    cursor.execute(query)
    result = cursor.fetchall()
    print (result)
    return result

# 2] Retreive From Prescription according to doctor & his Email

def SelecT_ALL_Prescription_Employee(cursor,Email):

    #query = '''Select * from Prescription Ps,Employee E where Ps.Doc_id = E.ID And E.Email='''+"'"+Email+"'"
    #cursor.execute(query)
    query = '''Select * from Prescription Ps,Employee E where Ps.Doc_id = E.ID And E.Email=?;'''
    cursor.execute(query,[Email])
    result = cursor.fetchall()
    print (result)
    return result

def Select_From_Prescription_Employee(cursor,Email,Columns = []):

    Q1 = ''''''
    if (len(Columns) > 0):
        Q1 += Prescription_attributes[Columns[0]]
        for i in range(1,len(Columns)):
            Q1 += ''','''
            Q1 += Prescription_attributes[Columns[i]]
    else:
        Q1 += Prescription_attributes[2]
        for i in range(3,len(Prescription_attributes)):
            Q1 += ''','''
            Q1 += Prescription_attributes[i]
    #query = '''Select '''+Q1+''' from Prescription Ps,Employee E where Ps.Doc_id = E.ID And E.Email='''+"'"+Email+"'"
    #cursor.execute(query)
    query = '''Select '''+Q1+''' from Prescription Ps,Employee E where Ps.Doc_id = E.ID And E.Email=?'''
    cursor.execute(query,[Email])
    result = cursor.fetchall()
    print (result)
    return result




#general update function updates one col without join

def Update(cursor,TableName,SelectingAttributes,SelectingAttributesValues,UpdatedAttributes,UpdatedAttributesValues):
    Q1='''update '''+TableName+''' set '''
    for i in range(len(UpdatedAttributes)-1):
        Q1+=Dicts[TableName][UpdatedAttributes[i]]+''' = '''+str(UpdatedAttributesValues[i])+''' , '''
    Q1+=Dicts[TableName][UpdatedAttributes[-1]]+''' = '''+str(UpdatedAttributesValues[-1])
    if len(SelectingAttributes)>0:
        Q1+=''' where '''
    for i in range (len(SelectingAttributes)-1):
        Q1+=Dicts[TableName][SelectingAttributes[i]]+''' = '''+str(SelectingAttributesValues[i])+''' and '''
    Q1+=Dicts[TableName][SelectingAttributes[-1]]+''' = '''+str(SelectingAttributesValues[-1]) +''' ;'''
    try:
        cursor.execute(Q1)
        return True
    except Error as e:
        print(e)
        return False
        


#general delete from table 

def Delete(cursor,TableName,SelectingAttributes,SelectingAttributesValues):
    Q1='''delete from '''+TableName+' '
    if len(SelectingAttributes)>0:
        Q1+=' where '
    for i in range (len(SelectingAttributes)-1):
        Q1+=Dicts[TableName][SelectingAttributes[i]]+' = '+str(SelectingAttributesValues[i])+' and '
    Q1+=Dicts[TableName][SelectingAttributes[-1]]+' = '+str(SelectingAttributesValues[-1]) +' ;'
    try:
        cursor.execute(Q1)
        return True
    except Error as e:
        print(e)
        return False



# ------------------------- Prescription --------------------------------------
# 1] Retreive From Prescription according to Patient & his Email {Can be General not only Email}
# Before insertion  we must Check Doc_ID is for Doctor Group_ID = 'D'
def SelecT_ALL_Prescription_Patient_sorted_by_date(cursor,patient_id):

    query = '''Select E.FNAME, Ps.DATE,Ps.Treatment from Prescription Ps, Reservation as R ,
    Employee as E where Ps.Reservation_id = R.ID And R.Patient_id=? And R.Doctor_id = E.ID order by Ps.Date desc;'''
    cursor.execute(query,[patient_id])
    result = cursor.fetchall()
    return result

def SelecT_ALL_Prescription_Patient(cursor,Email):

    #query = '''Select * from Prescription Ps,Patient P where Ps.Patient_id = P.ID And P.Email='''+"'"+Email+"'"
    #cursor.execute(query)
    query = '''Select * from Prescription Ps,Patient P where Ps.Patient_id = P.ID And P.Email=?;'''
    cursor.execute(query,[Email])
    result = cursor.fetchall()
    print (result)
    return result

def Select_From_Prescription_Patient(cursor,Email,Columns = []):

    Q1 = ''''''
    if (len(Columns) > 0):
        Q1 += Prescription_attributes[Columns[0]]
        for i in range(1,len(Columns)):
            Q1 += ''','''
            Q1 += Prescription_attributes[Columns[i]]
    else:
        Q1 += Prescription_attributes[2]
        for i in range(3,len(Prescription_attributes)):
            Q1 += ''','''
            Q1 += Prescription_attributes[i]
    query = '''Select '''+Q1+''' from Prescription Ps,Patient P where Ps.Patient_id = P.ID And P.Email='''+"'"+Email+"';"
    cursor.execute(query)
    result = cursor.fetchall()
    print (result)
    return result

# 2] Retreive From Prescription according to doctor & his Email

def SelecT_ALL_Prescription_Employee(cursor,Email):

    #query = '''Select * from Prescription Ps,Employee E where Ps.Doc_id = E.ID And E.Email='''+"'"+Email+"'"
    #cursor.execute(query)
    query = '''Select * from Prescription Ps,Employee E where Ps.Doc_id = E.ID And E.Email=?;'''
    cursor.execute(query,[Email])
    result = cursor.fetchall()
    print (result)
    return result

def Select_From_Prescription_Employee(cursor,Email,Columns = []):

    Q1 = ''''''
    if (len(Columns) > 0):
        Q1 += Prescription_attributes[Columns[0]]
        for i in range(1,len(Columns)):
            Q1 += ''','''
            Q1 += Prescription_attributes[Columns[i]]
    else:
        Q1 += Prescription_attributes[2]
        for i in range(3,len(Prescription_attributes)):
            Q1 += ''','''
            Q1 += Prescription_attributes[i]
    #query = '''Select '''+Q1+''' from Prescription Ps,Employee E where Ps.Doc_id = E.ID And E.Email='''+"'"+Email+"'"
    #cursor.execute(query)
    query = '''Select '''+Q1+''' from Prescription Ps,Employee E where Ps.Doc_id = E.ID And E.Email=?'''
    cursor.execute(query,[Email])
    result = cursor.fetchall()
    print (result)
    return result

# ---------------------------------- Department Queries ------------------------------------------------

def Select_count_Department(cursor):

    query = ''' Select count(*) from Department'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result
# with order by name
def select_All_manager_name(cursor):
    query = '''select E.FNAME,E.lNAME from Department D , Employee E where D.Manager_id = E.ID ORDER BY E.FNAME,E.lNAME ;'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result
# with order by Department_ID
def select_All_manager_name(cursor):
    query = '''select D.ID,E.FNAME,E.lNAME,E.Email from Department D , Employee E where D.Manager_id = E.ID ORDER BY D.ID ;'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def select_manager_name(cursor,Department_ID):
    query = '''select E.FNAME,E.lNAME from Department D , Employee E where D.Manager_id = E.ID and D.ID='''+"'"+Department_ID+"'"+''' ORDER BY E.FNAME,E.lNAME ;'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result
def select_rooms_number(cursor,Department_ID):
    query = '''select count(*) from Room where Department_ID ='''+ str(Department_ID)
    cursor.execute(query)
    result = cursor.fetchall()
    return result

#----------------------- Donations --------------------------

# def select_Donations(cursor):
#     query = '''select * from Donation ;'''
#     cursor.execute(query)
#     result = cursor.fetchall()
#     return result

def insert_Donar(cursor,BloodType,FNAME,lNAME,Addresscountry,Addresscity,Addressstreet):
    values = [BloodType,FNAME,lNAME,Addresscountry,Addresscity,Addressstreet]
    query = '''insert into Doner (BloodType,FNAME,lNAME,Addresscountry,Addresscity,Addressstreet) values (?,?,?,?,?,?);'''
    try:
        cursor.execute(query,values)
        return True
    except Error as e:
        print(e)
        return False

def insert_Donations(cursor,Donation_Date,type,donor):
    values = [Donation_Date,type,donor]
    query = '''insert into Donation (DonationDate,DonationType,DonarId) values (?,?,?);'''
    try:
        cursor.execute(query,values)
        return True
    except Error as e:
        print(e)
        return False
def select_Donations(cursor):
    query = '''select DonationDate,DonationType from Donation order by DonationDate ;'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def count_donations(cursor):
    query = '''select DonationType,count(*) from Donation where statee = "D" group by DonationType order by DonationType ;'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def retrieveTheDoctorsThatArenotManagers(cursor):
    query='''select ID from Employee where ID not in (select Manager_id from Department);'''
    result=cursor.execute(query).fetchall()
    return result


def getJoinDateOfEmployee(cursor,ID):
    query='''select JoinDate from Employee where ID = '''+str(ID)+''';'''
    cursor.execute(query)
    result=cursor.fetchall()
    return result
def getDepartmentnames(cursor,Departmentname):
    print(Departmentname)
    query='''select Department_Name from Department Where Department_Name <> "'''+str(Departmentname)+'''"  ;'''
    cursor.execute(query)
    result=cursor.fetchall()
    return result


def getDepartmentnames(cursor):
    query='''select Department_Name from Department  ;'''
    cursor.execute(query)
    result=cursor.fetchall()
    return result

def retrieveDepartmentIDS(cursor):
    query='''select ID from Department ;'''
    cursor.execute(query)
    result=cursor.fetchall()
    return result

#----------------------------- Reservation ----------------------------------------------
def insert_reservation(cursor, date, appointment, state, type, doctor_id, patient_id):
    query = "INSERT INTO Reservation (Date, Appointment, state, Type, Doctor_id, Patient_id) values (?,?,?,?,?,?);"
    values = [date, appointment, state, type, doctor_id, patient_id]

    try:
        cursor.execute(query,values)
        return True
    except Error as e:
        print(e)
        return False

def selectEmployeesExceptAdmin(cursor):
    query='''select * from Employee where Group_id <>"A";'''
    cursor.execute(query)
    result=cursor.fetchall()
    return result

# 1] Retreive From Prescription according to Patient & his Email {Can be General not only Email}
# Before insertion  we must Check Doc_ID is for Doctor Group_ID = 'D'

def select_patients_reservation_doctor(cursor,doctor_id,type):
    query = '''Select DISTINCT P.ID,P.FNAME,P.lNAME,P.AGE,P.Phonecountry,P.PhoneNumber,P.Addresscountry,P.Addresscity,P.Addressstreet,P.GENDER,P.Email,P.Password,P.image 
    from Patient P , Reservation R  where P.ID=R.Patient_id and R.Doctor_id='''+ str(doctor_id)+''' And R.Type="'''+type+'''";'''
    cursor.execute(query)
    result = cursor.fetchall()
    # print (result)
    return result    

def select_reservation(cursor,doctor_id,patient_id):
    query = '''Select R.ID from Reservation R  where R.Patient_id=''' +str(patient_id) + ''' and R.Doctor_id='''+ str(doctor_id)+''' order by R.Date;'''
    cursor.execute(query)
    result = cursor.fetchall()
    # print (result)
    return result[-1]

# ------------------------- Prescription --------------------------------------
# 1] Retreive From Prescription according to Patient & his Email {Can be General not only Email}
# Before insertion  we must Check Doc_ID is for Doctor Group_ID = 'D'

def select_patient_prescription(cursor,patient_id):
    query = '''Select Ps.ID,Ps.DATE,Ps.Illness,Ps.Treatment,Ps.Reservation_id, R.Doctor_id from Prescription Ps,Reservation R where Ps.Reservation_id=R.ID and  R.Patient_id ='''+str(patient_id)+''' group by Ps.Reservation_id,R.Doctor_id;'''
    cursor.execute(query)
    result = cursor.fetchall()
    # print (result)
    return result

def select_doctor_prescription(cursor,patient_id,doctor_id):
    query = '''Select Ps.ID,Ps.DATE,Ps.Illness,Ps.Treatment,Ps.Reservation_id from Prescription Ps,Reservation R where Ps.Reservation_id=R.ID and  R.Patient_id ='''
    query+= str(patient_id)+''' and R.Doctor_id =''' +str(doctor_id)+''';'''
    cursor.execute(query)
    result = cursor.fetchall()
    # print (result)
    return result

def select_patients_reservation_doctor(cursor,doctor_id):
    query = '''Select DISTINCT P.ID,P.FNAME,P.lNAME,P.AGE,P.Phonecountry,P.PhoneNumber,P.Addresscountry,P.Addresscity,P.Addressstreet,P.GENDER,P.Email,P.Password,P.image 
    from Patient P , Reservation R  where P.ID=R.Patient_id and R.Doctor_id='''+ str(doctor_id)+''' And R.Type like "A%" ;'''
    cursor.execute(query)
    result = cursor.fetchall()
    print (result)
    return result