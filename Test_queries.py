from Queries import *
Department_attributes = {1:"ID",2:"FNAME",3:"lNAME",4:"Manager_id",5:"Start_Date"}
Patient_attributes = {1:"ID",2:"FNAME",3:"lNAME",4:"AGE",5:"Phonecountry",6:"Phonecity"
,7:"PhoneNumber",8:"Addresscountry",9:"Addresscity",10:"Addressstreet",11:"GENDER",12:"Email",13:"Password"}
Employee_attributes ={1:"ID",2:"FNAME",3:"lNAME",4:"AGE",5:"Phonecountry",6:"Phonecity"
,7:"PhoneNumber",8:"Addresscountry",9:"Addresscity",10:"Addressstreet",11:"GENDER",12:"Email",13:"Password",14:"JoinDate",15:"D_id",16:"Group_id"}
Prescription_attributes = {1:"ID",2:"Illness",3:"Treatment",4:"Doc_id",5:"Patient_id"}

# Enums of each Table
#list_0 ={}
# selected attributes
#list_1 = []
# selecting attributes in where
#list_2 = []
# values of selecting attributes
# list_3 = []


#===================================================================================================
# Function: selectFromTable
# Input:    string:table_name , Dictionary:list_0 -> Enums contain attributes with numbers list:list_1 -> enums to select from attributes
#           list:list_2 -> enums to select attributes conditions list in where ,list:list_3 -> values in condition attributes
# Output:   2D list of tuples result
# Prerequistes: None
# Description: Select any attribute(s) from any Table under any condition related to same Table only
# status: Not Tested
#===================================================================================================
def selectFromTable(table_name,list_0,list_1,list_2,list_3):

    Q1 = ''''''
    Q2 = ''''''
    for i in range(len(list_1)-1):
        Q1 += list_0[list_1[i]]
        Q1 +=","
    Q1 += list_0[list_1[-1]]
    
    for i in range(len(list_2)-1):
        Q2 += list_0[list_2[i]] + "="+list_3[i]+" AND "
    Q2 += list_0[list_2[-1]] + "="+ list_3[-1]
    query = 'select '+Q1+' from ' + table_name +' where '+Q2+';'
    conn = create_connection('test.db')
    result = read_query(conn,query)

    return result

# list_1 = [2,3,4,5,6]
# # selecting attributes in where
# list_2 = [12,13]
# # values of selecting attributes
# list_3 = ["'ahmed232345@gmail.com'","'12345678'"]

# # Q1 = selectFromTable("Patient",Patient_attributes,list_1,list_2,list_3)
# # print (Q1)
# result = selectFromTable("Patient",Patient_attributes,list_1,list_2,list_3)


#===================================================================================================
# Function: insert General
# Input:    string: Table name ,list:list_1 -> values in to be inserted in patient 
# Output:   
# Prerequistes: None
# Description: insert new tuple in any table
# status: Not Tested
#===================================================================================================
def insert_general(table_name ,list_1,list_2,list_3):
    conn = create_connection('test.db')
    Q1 =''''''
    

    query = '''iINSERT INTO '''+table_name+''' (FNAME,lNAME,AGE,Phonecountry,Phonecity,PhoneNumber,Addresscountry,Addresscity,Addressstreet
    ,GENDER,Email,Password)
    VALUES(?,?,?,?,?,?.?.?.?.?.?,?,?)'''
    execute_query_list(conn,query,list_3)
#===================================================================================================
# Function: insert patient
# Input:    list:list_1 -> values in to be inserted in patient 
# Output:   
# Prerequistes: None
# Description: insert new tuple 
# status: Not Tested
#===================================================================================================
def insert_Patient(list_1):
    conn = create_connection('test.db')
    query = '''iINSERT INTO Patient (FNAME,lNAME,AGE,Phonecountry,Phonecity,PhoneNumber,Addresscountry,Addresscity,Addressstreet
    ,GENDER,Email,Password)
    VALUES(?,?,?,?,?.?.?.?.?.?,?,?)'''
    execute_query_list(conn,query,list_1)


#===================================================================================================
# Function: insert_Department
# Input:    list:list_1 -> values in to be inserted in Department 
# Output:   
# Prerequistes: None
# Description: insert new tuple 
# status: Not Tested
#===================================================================================================
def insert_Department(list_1):
    conn = create_connection('test.db')
    query = '''iINSERT INTO Department (FNAME,lNAME,Manager_id,Start_Date)
            VALUES(?,?,?,?)'''
    execute_query_list(conn,query,list_1)
#===================================================================================================
# Function: insert_Employee
# Input:    list:list_1 -> values in to be inserted in Department 
# Output:   
# Prerequistes: None
# Description: insert new tuple 
# status: Not Tested
#===================================================================================================
# FNAME,lNAME,AGE,Phonecountry,Phonecity,PhoneNumber,Addresscountry,Addresscity,Addressstreet,GENDER,Email,Password,JoinDate,D_id,Group_id
def insert_Employee(list_1):
    conn = create_connection('test.db')
    query = '''iINSERT INTO Employee (FNAME,lNAME,AGE,Phonecountry,Phonecity,PhoneNumber,Addresscountry
    ,Addresscity,Addressstreet,GENDER,Email,Password,JoinDate,D_id,Group_id)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    execute_query_list(conn,query,list_1)
#===================================================================================================
# Function: insert_Prescription
# Input:    list:list_1 -> values in to be inserted in Department 
# Output:   
# Prerequistes: None
# Description: insert new tuple 
# status: Not Tested
#===================================================================================================

def insert_Prescription(list_1):
    conn = create_connection('test.db')
    query = '''iINSERT INTO Prescription (Illness,Treatment,Doc_id,Patient_id)
            VALUES(?,?,?,?)'''
    execute_query_list(conn,query,list_1)

#===================================================================================================
# Function: insert_GlobalContract
# Input:    list:list_1 -> values in to be inserted in Department 
# Output:   
# Prerequistes: None
# Description: insert new tuple 
# status: Not Tested
#===================================================================================================
def insert_GlobalContract(list_1):
    conn = create_connection('test.db')
    query = '''iINSERT INTO GlobalContract (Terms,Penalty)
            VALUES(?,?)'''
    execute_query_list(conn,query,list_1)

#===================================================================================================
# Function: insert_EmployeeContract
# Input:    list:list_1 -> values in to be inserted in Department 
# Output:   
# Prerequistes: None
# Description: insert new tuple 
# status: Not Tested
#===================================================================================================
def insert_EmployeeContract(list_1):
    conn = create_connection('test.db')
    query = '''iINSERT INTO EmployeeContract (E_ID,GlobalContract_ID)
            VALUES(?,?)'''
    execute_query_list(conn,query,list_1)

#===================================================================================================
# Function: insert_PatientContract
# Input:    list:list_1 -> values in to be inserted in Department 
# Output:   
# Prerequistes: None
# Description: insert new tuple 
# status: Not Tested
#===================================================================================================
def insert_PatientContract(list_1):
    conn = create_connection('test.db')
    query = '''iINSERT INTO PatientContract (Doc_ID,GlobalContract_ID,OP_ID)
            VALUES(?,?,?)'''
    execute_query_list(conn,query,list_1)

#===================================================================================================
# Function: insert_Room
# Input:    list:list_1 -> values in to be inserted in Department 
# Output:   
# Prerequistes: None
# Description: insert new tuple 
# status: Not Tested
#===================================================================================================
def insert_Room(list_1):
    conn = create_connection('test.db')
    query = '''iINSERT INTO Room (LastStay,Avaliable,Department_ID)
            VALUES(?,?,?)'''
    execute_query_list(conn,query,list_1)
