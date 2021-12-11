from flask import Flask
from .config import *

connection = open_connection("hospital.db")
cursor = get_cursor(connection)


app=Flask(__name__)

if __name__=="__main__":
    app.run(debug=True)