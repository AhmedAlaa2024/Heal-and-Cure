from ..app import cursor


class Department():
    def __init__(self,cursor,FNAME,lNAME,Manager_id = "NULL"):
        self.cursor = cursor
        self.fname = FNAME
        self.lname = lNAME
        self.manager_id = Manager_id

    def get():
        pass

    def insert(self):
        # list_1 =[self.fname,self.lname,self.manager_id]
        # query = '''INSERT INTO Department (FNAME,lNAME,Manager_id)
        #     VALUES(?,?,?)'''
        # self.cursor.execute(query,list_1)
        query = '''INSERT INTO Department (FNAME,lNAME,Manager_id) 
                VALUES(' '''
        query += self.fname +''' ',' '''+ self.lname+ ''' ', '''+str(self.manager_id) + ''');'''

    def update():
        pass

    def delete():
        pass


class Room():
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


class EmploymentContract():
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


class OperationContract():
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