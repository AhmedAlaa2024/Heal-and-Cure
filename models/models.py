from Queries import *
from config import *
from utils import *
import enum
# Dictionaries

Department_attributes = {0:"*",1:"ID",2:"FNAME",3:"lNAME",4:"Manager_id",5:"Start_Date"}
Patient_attributes = {0:"*",1:"ID",2:"FNAME",3:"lNAME",4:"AGE",5:"Phonecountry",6:"Phonecity"
,7:"PhoneNumber",8:"Addresscountry",9:"Addresscity",10:"Addressstreet",11:"GENDER",12:"Email",13:"Password"}
Employee_attributes ={0:"*",1:"ID",2:"FNAME",3:"lNAME",4:"AGE",5:"Phonecountry",6:"Phonecity"
,7:"PhoneNumber",8:"Addresscountry",9:"Addresscity",10:"Addressstreet",11:"GENDER",12:"Email",13:"Password",14:"JoinDate",15:"D_id",16:"Group_id"}
Prescription_attributes = {0:"*",1:"ID",2:"Illness",3:"Treatment",4:"Doc_id",5:"Patient_id"}
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
    Phonecity = 6
    PhoneNumber = 7
    Addresscountry = 8
    Addresscity = 9
    Addressstreet = 10
    GENDER = 11
    Email = 12
    Password = 13
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
    Phonecity = 6
    PhoneNumber = 7
    Addresscountry = 8
    Addresscity = 9
    Addressstreet = 10
    GENDER = 11
    Email = 12
    Password = 13

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
                Q2 += table_attributes[Selectors[i][0]] + "="+Selectors[i][1]+" AND "
            else:
                 Q2 += table_attributes[Selectors[i][0]] + "='"+Selectors[i][1]+"' AND "
        if(isinstance(Selectors[i][-1], int)):
            Q2 += table_attributes[Selectors[-1][0]] + "="+ Selectors[-1][1]
        else:
            Q2 += table_attributes[Selectors[-1][0]] + "='"+ Selectors[-1][1]+"'"

    query = 'select '+Q1+' from ' + table_name +Q2+';'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    return result


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
    cursor.execute(query,Values)