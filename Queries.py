import sqlite3
from sqlite3 import Error
#conn = sqlite3.connect('test.db')


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

conn  = create_connection('test.db')

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
    connection.close()

def execute_query_list(connection, query,list):
    cursor = connection.cursor()
    try:
        cursor.execute(query,list)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
    connection.close()


