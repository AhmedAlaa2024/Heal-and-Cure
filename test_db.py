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
Columns = [Employee.Age.value,Employee.PhoneNumber.value]
Columns2 = [Employee.All.value]
Selectors = [(Employee.FNAME.value,"Ahmed"),(Employee.lNAME.value,"Alaa")]
for i in Columns:
    print(i)
#print(Employee.FNAME.value)
#result = selectFromTable(cursor,'Employee',Employee_attributes,Columns2,Selectors)
Columns3 = [Patient.All.value]
Values =["Ahmed", "Sabry", 20, "+2", "1028202598", "Egypt", "Cairo", "Helwan", "M", "ahmedsabry2323455.com2024@gmail.com", "123456789"]
insert_general(cursor,'Patient',Patient_attributes,Columns3,Values)
close_connection(connection)