

class Employee():
    def __init__(self, cursor, fname, lname, age, phoneCountry, phoneCity, phoneNumber, addressCountry, addressCity, addressStreet, gender, email, password, join_date, department_id, group_id):
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
    def __init__(self, cursor, FNAME,lNAME,AGE,Phonecountry,Phonecity,PhoneNumber,Addresscountry,Addresscity,Addressstreet
    ,GENDER, Email ,Password):
        self.cursor = cursor
        self.fname = FNAME
        self.lname = lNAME
        self.age = AGE
        self.phoneCountry = Phonecountry
        self.phoneCity = Phonecity
        self.phoneNumber = PhoneNumber
        self.addressCountry = Addresscountry
        self.addressCity = Addresscity
        self.addressStreet = Addressstreet
        self.gender = GENDER
        self.email = Email
        self.__password = Password



    def get():
        pass

    def insert(self):
        
        # list_1 = [
        # self.fname,
        # self.lname,
        # self.age,
        # self.phoneCountry,
        # self.phoneCity,
        # self.phoneNumber,
        # self.addressCountry,
        # self.addressCity,
        # self.addressStreet,
        # self.gender,
        # self.email,
        # self.__password ]
        # query = '''INSERT INTO Patient (FNAME,lNAME,AGE,Phonecountry,Phonecity,PhoneNumber,Addresscountry,Addresscity,Addressstreet,GENDER,Email,Password) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
    
        #self.cursor.execute(query,list_1)

        query = "INSERT INTO Patient (FNAME,lNAME,AGE,Phonecountry,Phonecity,PhoneNumber,"
        query += "Addresscountry,Addresscity,Addressstreet"
        query += ",GENDER,Email,Password) "
        query += "VALUES ('"
        query += self.fname + "','" + self.lname + "',"
        query += str(self.age) + ",'" + self.phoneCountry + "','" + self.phoneCity + "','"
        query += self.phoneNumber + "','" + self.addressCountry + "','" + self.addressCity + "','"
        query += self.addressStreet + "','" + self.gender + "','" + self.email + "','" + self.__password + "');"
        #print(query)
        self.cursor.execute(query)

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