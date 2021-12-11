import sqlite3
conn = sqlite3.connect('test.db')
#creat the tables
#department table
conn.execute('''CREATE TABLE Department
         (ID INT PRIMARY KEY     NOT NULL AUTOINCREMENT,
         FNAME           CHAR(50)  NOT NULL,
         lNAME          CHAR(50)     NOT NULL,
         Manager_id     INT,
         Start_Date     TEXT         NOT NULL,
         CONSTRAINT Manage
         FOREIGN KEY (Manager_id)
         REFERENCES Employee (ID),
         );''')
#patient table
conn.execute('''CREATE TABLE Patient
         (ID INT PRIMARY KEY     NOT NULL AUTOINCREMENT,
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
         Password       CHAR(50)  NOT NULL);''')
#employee table
conn.execute('''CREATE TABLE Employee
         (ID INT PRIMARY KEY     NOT NULL AUTOINCREMENT,
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
         JoinDate       TEXT      NOT NULL,
         D_id           INT,
         CONSTRAINT emp&Dep
         FOREIGN KEY (D_id)
         REFERENCES Department (ID),
         Group_id       CHAR(1)   NOT NULL,
           );''')
# prescription table
# there are two relationships (employee,patient)
conn.execute('''CREATE TABLE Prescription
         (ID INT PRIMARY KEY     NOT NULL AUTOINCREMENT,
         DATE           TEXT     NOT NULL,
         Illness        CHAR(50)     NOT NULL,
         Treatment      TEXT     NOT NULL,
         Doc_id         INT  ,
         Patient_id         INT  ,
         CONSTRAINT BelongsTo
         FOREIGN KEY (Doc_id)
         REFERENCES Employee (ID),
         CONSTRAINT Has
         FOREIGN KEY (Patient_id)
         REFERENCES Patient (ID),
         );''')
#reservation table
# there are three relationships (prescription,patient,room)
conn.execute('''CREATE TABLE Reservation
         (ID INT PRIMARY KEY     NOT NULL AUTOINCREMENT,
         DATE           TEXT     NOT NULL,
         Appointment    TEXT     NOT NULL,
         state          CHAR(1)  NOT NULL,
         Price          INT      NOT NULL ,
         Patient_id         INT  ,
         Prescription_id    INT  ,
         Room_id         INT  ,
         CONSTRAINT Pre&Res
         FOREIGN KEY (Prescription_id)
         REFERENCES Prescription (ID),
         CONSTRAINT Patient&Res
         FOREIGN KEY (Patient_id)
         REFERENCES Patient (ID),
         CONSTRAINT Room&Res
         FOREIGN KEY (Room_id)
         REFERENCES Room (ID),
         );''')
# contracts tables(global)
conn.execute('''CREATE TABLE GlobalContract
         (ID INT PRIMARY KEY     NOT NULL AUTOINCREMENT ,
         Terms    TEXT           NOT NULL,
         Penalty  TEXT           NOT NULL
         );''')
conn.execute('''CREATE TABLE EmployeeContract
         (ID INT NOT NULL AUTOINCREMENT,
         E_ID INT  ,
         GlobalContract_ID INT ,
         PRIMARY KEY(ID,E_ID, GlobalContract_ID ),
         CONSTRAINT E&C
         FOREIGN KEY (E_ID)
         REFERENCES Employee (ID),
         CONSTRAINT GC&C
         FOREIGN KEY ( GlobalContract_ID )
         REFERENCES GContract (ID)
         );''')
conn.execute('''CREATE TABLE PatientContract
         (P_ID INT ,
         Doc_ID INT  ,
         GlobalContract_ID  INT ,
         OP_ID INT,
         PRIMARY KEY(P_ID,E_ID, GlobalContract_ID ,OP_ID),
         CONSTRAINT E&C
         FOREIGN KEY (Doc_ID)
         REFERENCES Employee (ID),
         CONSTRAINT GC&C
         FOREIGN KEY ( GlobalContract_ID )
         REFERENCES GContract (ID),
         CONSTRAINT P&C
         FOREIGN KEY (P_ID)
         REFERENCES Patient (ID),
         CONSTRAINT OP&C
         FOREIGN KEY (OP_ID)
         REFERENCES Operation (ID)
         );''')
#room
conn.execute('''CREATE TABLE Room
         (ID INT PRIMARY KEY NOT NULL,
         LastStay TEXT    ,
         Avaliable CHAR(1) ,
         Department_ID  INT,
         CONSTRAINT D&R
         FOREIGN KEY (DE_ID)
         REFERENCES Department (ID)
         );''')
#Examination
conn.execute('''
             CREATE TABLE EXAMINATION
             (
               ID INT PRIMARY KEY NOT NULL,
               DATE VARCHAR(18) DEFAULT='00:00AM,00/00/0000',
               RESULT VARCHAR(150)
             )
             ''')
