#department table
Department_TABLE = '''CREATE TABLE IF NOT EXISTS Department
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
         FNAME           CHAR(50)  NOT NULL,
         lNAME          CHAR(50)     NOT NULL,
         Manager_id     INT,
         Start_Date     VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
         CONSTRAINT Manage
         FOREIGN KEY (Manager_id)
         REFERENCES Employee (ID)
         )'''
#patient table
Patient_TABLE = '''CREATE TABLE IF NOT EXISTS Patient
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
         FNAME          CHAR(50)     NOT NULL,
         lNAME          CHAR(50)     NOT NULL,
         AGE            INT     NOT NULL,
         Phonecountry       CHAR(50)  NOT NULL,
         Phonecity          CHAR(50)  NOT NULL,
         PhoneNumber        CHAR(50)  NOT NULL,
         Addresscountry       CHAR(50)  NOT NULL,
         Addresscity          CHAR(50)  NOT NULL,
         Addressstreet        CHAR(50)  NOT NULL,
         GENDER         CHAR(1)   NOT NULL,
         Email          CHAR(50)  NOT NULL UNIQUE,
         Password       CHAR(50)  NOT NULL)'''
#employee table
Employee_TABLE = '''CREATE TABLE IF NOT EXISTS Employee
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
         FNAME          CHAR(50)     NOT NULL,
         lNAME          CHAR(50)     NOT NULL,
         AGE            INT     NOT NULL,
         Phonecountry       CHAR(50)  NOT NULL,
         Phonecity          CHAR(50)  NOT NULL,
         PhoneNumber        CHAR(50)  NOT NULL,
         Addresscountry       CHAR(50)  NOT NULL,
         Addresscity          CHAR(50)  NOT NULL,
         Addressstreet        CHAR(50)  NOT NULL,
         GENDER         CHAR(1)   NOT NULL,
         Email          CHAR(50)  NOT NULL UNIQUE,
         Password       CHAR(50)  NOT NULL ,
         JoinDate       VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
         D_id           INT,
         Group_id       CHAR(1)   NOT NULL,
         CONSTRAINT employee_department FOREIGN KEY(D_id) REFERENCES Department(ID)
           )'''
# prescription table
# there are two relationships (employee,patient)
Prescription_TABLE = '''CREATE TABLE IF NOT EXISTS Prescription
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
         DATE           VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
         Illness        CHAR(50)     NOT NULL,
         Treatment      TEXT     NOT NULL,
         Doc_id         INT  ,
         Patient_id         INT  ,
         CONSTRAINT BelongsTo
         FOREIGN KEY (Doc_id)
         REFERENCES Employee (ID),
         CONSTRAINT Has
         FOREIGN KEY (Patient_id) REFERENCES Patient (ID)
         )'''
#reservation table
# there are three relationships (prescription,patient,room)
Reservation_TABLE = '''CREATE TABLE IF NOT EXISTS Reservation
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
         DATE           VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
         Appointment    TEXT     NOT NULL,
         state          CHAR(1)  NOT NULL,
         Price          INT      NOT NULL,
         Patient_id         INT,
         Prescription_id    INT,
         Room_id         INT,
         CONSTRAINT Prescription_Reservation
         FOREIGN KEY (Prescription_id)
         REFERENCES Prescription (ID),
         CONSTRAINT Patient_Reservation
         FOREIGN KEY (Patient_id)
         REFERENCES Patient (ID),
         CONSTRAINT Room_Reservation
         FOREIGN KEY (Room_id)
         REFERENCES Room (ID)
         )'''
# contracts tables(global)
GlobalContract_TABLE = '''CREATE TABLE IF NOT EXISTS GlobalContract
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
         Terms    TEXT           NOT NULL,
         Penalty  TEXT           NOT NULL
         )'''

EmployeeContract_TABLE = '''CREATE TABLE IF NOT EXISTS EmployeeContract
         (ID INT NOT NULL,
         E_ID INT  ,
         GlobalContract_ID INT ,
         PRIMARY KEY(ID,E_ID, GlobalContract_ID ),
         CONSTRAINT Employee_Contract
         FOREIGN KEY (E_ID)
         REFERENCES Employee (ID),
         CONSTRAINT GlobalContract_Contract
         FOREIGN KEY ( GlobalContract_ID )
         REFERENCES GContract (ID)
         )'''
PatientContract_TABLE = '''CREATE TABLE IF NOT EXISTS PatientContract
         (P_ID INT,
         E_ID INT,
         Doc_ID INT,
         GlobalContract_ID  INT,
         OP_ID INT,
         PRIMARY KEY(P_ID,E_ID, GlobalContract_ID ,OP_ID),
         CONSTRAINT Employee_Contract FOREIGN KEY (Doc_ID) REFERENCES Employee (ID),
         CONSTRAINT GlobalContract_Contract FOREIGN KEY ( GlobalContract_ID ) REFERENCES GContract (ID),
         CONSTRAINT Patient_Contract FOREIGN KEY (P_ID) REFERENCES Patient (ID),
         CONSTRAINT Operation_Contract FOREIGN KEY (OP_ID) REFERENCES Operation (ID)
         )'''
#room
Room_TABLE = '''CREATE TABLE IF NOT EXISTS Room
         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         LastStay VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
         Avaliable CHAR(1),
         Department_ID  INT,
         CONSTRAINT Department_Room FOREIGN KEY (Department_ID) REFERENCES Department (ID)
         )'''
#Examination
Examination_TABLE = '''CREATE TABLE IF NOT EXISTS Examination
             (
               ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               DATE VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
               RESULT VARCHAR(150)
             )
             '''


HOSPITAL_DB_TABLES = [Department_TABLE, Patient_TABLE, Employee_TABLE, Prescription_TABLE, Reservation_TABLE, GlobalContract_TABLE, EmployeeContract_TABLE, PatientContract_TABLE, Room_TABLE, Examination_TABLE]