

class Employee():
    def __init__(self, cursor, fname, lname, age, phoneCountry, phoneCity, phoneNumber, addressCountry, addressCity, addressStreet, gender, email, password, join_date, department_id, group_id):
        self.id = None
        self.cursor = cursor
        self.fname = fname
        self.lname = lname
        self.age = age
        self.phoneCountry = phoneCountry
        self.phoneCity = phoneCity
        self.phoneNumber = phoneNumber
        self.addressCountry = addressCountry
        self.addressCity = addressCity
        self.addressStreet = addressStreet
        self.gender = gender
        self.email = email
        self.__password = password
        self.join_date = join_date
        self.department_id = department_id
        self.group_id = group_id


    def __init__(self, cursor):
        self.id = None
        self.cursor = cursor
        self.fname = None
        self.lname = None
        self.age = None
        self.phoneCountry = None
        self.phoneCity = None
        self.phoneNumber = None
        self.addressCountry = None
        self.addressCity = None
        self.addressStreet = None
        self.gender = None
        self.email = None
        self.__password = None
        self.join_date = None
        self.department_id = None
        self.group_id = None


    def get():
        pass

    def insert(self):
        query = "INSERT INTO EMPLOYEE (FNAME,lNAME,AGE,Phonecountry,Phonecity,PhoneNumber,"
        query += "Addresscountry,Addresscity,Addressstreet,GENDER,Email,Password,JoinDate,D_id,Group_id) "
        query += "VALUES ('"
        query += self.fname + "','" + self.lname + "',"
        query += str(self.age) + ",'" + self.phoneCountry + "','" + self.phoneCity + "','"
        query += self.phoneNumber + "','" + self.addressCountry + "','" + self.addressCity + "','"
        query += self.addressStreet + "','" + self.gender + "','" + self.email + "','" + self.__password + "','"
        query += self.join_date + "'," + str(self.department_id) + "," + str(self.group_id) + ");"

        self.cursor.execute(query)

    def update():
        pass

    def delete():
        pass


class Patient():
    def __init__(self):
        pass

    def get():
        pass

    def insert():
        pass

    def update():
        pass

    def delete():
        pass


class Donor():
    def __init__(self):
        pass

    def get():
        pass

    def insert():
        pass

    def update():
        pass

    def delete():
        pass