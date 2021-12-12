from models.users import Patient
from config import *

connection = open_connection("hospital.db")
cursor = get_cursor(connection)

Database_Setup(cursor)

def test_db():
    patient1 = Patient(cursor, "Ahmed", "Sabry", 20, "+2", "0", "1028202598", "Egypt", "Cairo", "Dar El-Salam", "M", "ahmedsabry232345@gmail.com", "123456789")
    patient1.insert()

test_db()

close_connection(connection)
