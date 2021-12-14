import sqlite3
from sqlite3.dbapi2 import Cursor
from Models.models_sql_queries import *
################################## DB Connection Configurations ####################################

#===================================================================================================
# Function: open_connection
# Input:    <sting:db_name> => the relative path of required database to be connected with
# Output:   <(Sqlite3::Connection):connection> => An object of class connection from sqlite3 module
# Prerequistes: None
# Description: Open connection with the required database
#===================================================================================================
def open_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

#===================================================================================================
# Function: get_cursor
# Input:    <(Sqlite3::Connection):connection> => An object of class connection from sqlite3 module
# Output:   <(Sqlite3::Connection::Cursor):cursor> => An object of class cursor from class connection
#           which is from sqlite3 module
# Prerequistes: The passed connection is already opened
# Description: Get a cursor to connected database's data and return the cursor
#===================================================================================================
def get_cursor(connection):
    return connection.cursor()

# Function used to close the given connection
#===================================================================================================
# Function: close_connection
# Input:    <(Sqlite3::Connection):connection> => An object of class connection from sqlite3 module
# Output:   None
# Prerequistes: The passed connection is already opened
# Description: Close the given connection
#===================================================================================================
def close_connection(connection):
    connection.commit()
    connection.close()
####################################################################################################

def Database_Setup(cursor):
    for table in HOSPITAL_DB_TABLES:
        cursor.execute(table)