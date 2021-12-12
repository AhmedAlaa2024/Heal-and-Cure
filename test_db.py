from utils import *
from models.users import *
from config import *

connection = open_connection("hospital.db")
cursor = get_cursor(connection)


def test_DB_creation():
    Database_Setup(cursor)


def test_employee_insertion():
    employee1 = Employee(cursor, "Ahmed", "Alaa", 20, "+2", "0", "1028202598", "Egypt", "Cairo", "Dar El-Salam", "M", "ahmedalaa.com2024@gmail.com", "123456789", get_time_now_as_text(), 0, 0)
    employee1.insert()


def test_Patient_insertion():
    patient1 = Patient(cursor, "Ahmed", "Sabry", 20, "+2", "0", "1067371115", "Egypt", "Cairo", "Helwan", "F", "ahmedsabry232348@gmail.com", "fuckfuck123")
    patient1.insert()

test_Patient_insertion()

close_connection(connection)