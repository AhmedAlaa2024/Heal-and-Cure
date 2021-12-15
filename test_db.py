from utils import *
from models.models import *
from config import *

connection = open_connection("hospital.db")
cursor = get_cursor(connection)


# def test_DB_creation():
#     Database_Setup(cursor)


# def test_employee_insertion():
#     employee1 = Employee(cursor, "Ahmed", "Alaa", 20, "+2", "0", "1028202598", "Egypt", "Cairo", "Dar El-Salam", "M", "ahmedalaa.com2024@gmail.com", "123456789", get_time_now_as_text(), 0, 0)
#     employee1.insert()


# def test_Patient_insertion():
#     patient1 = Patient(cursor, "Ahmed", "Sabry", 20, "+2", "0", "1067371115", "Egypt", "Cairo", "Helwan", "F", "ahmedsabry232348@gmail.com", "fuckfuck123")
#     patient1.insert()

#test_Patient_insertion()
#Columns = [Employee[Employee.Age],Employee[Employee.PhoneNumber]]
# Columns = [Employee.Age.value,Employee.PhoneNumber.value]
# Columns2 = [Employee.All.value]
# Selectors = [(Employee.FNAME.value,"Ahmed"),(Employee.lNAME.value,"Alaa")]
# for i in Columns:
#     print(i)
# #print(Employee.FNAME.value)
# #result = selectFromTable(cursor,'Employee',Employee_attributes,Columns2,Selectors)
# Columns3 = [Patient.All.value]
# Values =["Ahmed", "Sabry", 20, "+2", "1028202598", "Egypt", "Cairo", "Helwan", "M", "ahmedsabry2323455.com2024@gmail.com", "123456789"]
# insert_general(cursor,'Patient',Patient_attributes,Columns3,Values)
# close_connection(connection)

#------------------------------------Prescription----------------------
# Columns = [Prescription.All.value]
# Values = [get_time_now_as_text(),'Cold','Medicine: Congestal for 5 days',1,1]
# insert_general(cursor,'Prescription',Prescription_attributes,Columns,Values)
# Columns2 = [Prescription.All.value]
# Values2 = [get_time_now_as_text(),'Cold','Medicine: Congestal for 5 days',2,2]
# insert_general(cursor,'Prescription',Prescription_attributes,Columns2,Values2)
#result1 = selectFromTable(cursor,'P',Prescription_attributes,[Prescription.All.value],[])
#connection.commit()
#result1 = selectFromTable(cursor,'Prescription',Prescription_attributes,[Prescription.All.value],[])
#connection.commit()
#result2 = Select_From_Prescription_Patient(cursor,'ahmedsabry232348@gmail.com')
#connection.commit()
#result2 = SelecT_ALL_Prescription_Patient(cursor,'ahmedsabry232348@gmail.com')
#connection.commit()
result = Select_From_Prescription_Employee(cursor,'ahmedsabry232345.com2024@gmail.com',[])
connection.commit()

result=Update(cursor,'Patient',[Patient.Email.value,Patient.Patient_ID.value],['''"ahmedsabry@gmail.com"''',1],[Patient.Age.value],[50])

connection.close()
#close_connection(connection)