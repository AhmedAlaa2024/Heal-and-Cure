from utils import *
from models.users import Employee
from config import *

connection = open_connection("hospital.db")
cursor = get_cursor(connection)

def test_DB_Creation():
    Database_Setup(cursor)

def test_Employee_Insertion():
    employee1 = Employee(cursor, "Ahmed", "Alaa", 20, "+2", "0", "1028202598", "Egypt", "Cairo", "Dar El-Salam", "M", "ahmedalaa.com2024@gmail.com", "123456789", get_time_now_as_text(), 0, 0)
    employee1.insert()

test_DB_Creation()

# employee = get_object_or_404(Employee, id=1)

# def get_object_or_404(class_type, attribute):
#     # {
#     #     "Message": "Error",
#     #     "Code": 404
#     # }
#     result = []



close_connection(connection)