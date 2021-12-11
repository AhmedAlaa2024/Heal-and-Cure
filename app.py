from flask import Flask
from utils import *
from models.users import Employee
from .config import *

connection = open_connection("hospital.db")
cursor = get_cursor(connection)

Database_Setup(cursor)

app=Flask(__name__)

if __name__=="__main__":
    app.run(debug=True)