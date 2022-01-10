#department table
Department_TABLE = '''CREATE TABLE IF NOT EXISTS Department
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
         Department_Name  VARCHAR(250)  UNIQUE,
         Manager_id     INT,
         Start_Date     VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
         image  CHAR(250),
         CONSTRAINT Manage FOREIGN KEY (Manager_id) REFERENCES Employee (ID)
         )'''
#patient table
Patient_TABLE = '''CREATE TABLE IF NOT EXISTS Patient
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
         FNAME          CHAR(50)     NOT NULL,
         lNAME          CHAR(50)     NOT NULL,
         AGE            INT     NOT NULL,
         Phonecountry       CHAR(50)  NOT NULL,
         PhoneNumber        CHAR(50)  NOT NULL,
         Addresscountry       CHAR(50)  NOT NULL,
         Addresscity          CHAR(50)  NOT NULL,
         Addressstreet        CHAR(50)  NOT NULL,
         GENDER         CHAR(1)   NOT NULL,
         Email          CHAR(50)  NOT NULL UNIQUE,
         Password       CHAR(200)  NOT NULL,
         image  CHAR(250) )'''
#employee table
Employee_TABLE = '''CREATE TABLE IF NOT EXISTS Employee
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
         FNAME          CHAR(50)     NOT NULL,
         lNAME          CHAR(50)     NOT NULL,
         AGE            INT     NOT NULL,
         Phonecountry       CHAR(50)  NOT NULL,
         PhoneNumber        CHAR(50)  NOT NULL,
         Addresscountry       CHAR(50)  NOT NULL,
         Addresscity          CHAR(50)  NOT NULL,
         Addressstreet        CHAR(50)  NOT NULL,
         GENDER         CHAR(1)   NOT NULL,
         Email          CHAR(50)  NOT NULL UNIQUE,
         Password       CHAR(200)  NOT NULL ,
         image          CHAR(250),
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
         Reservation_id INT      NOT NULL,
         CONSTRAINT Prescription_Reservation FOREIGN KEY (Reservation_id) REFERENCES Reservation (ID)
         )'''
#reservation table
# there are three relationships (prescription,patient,room)
# Type: ("A-" or "O-") + Department_id of the requested doctor
# A: Appointment - > Needs Prescription_id + Doctor_id
# O: Operation -> Needs Room_id + Doctor_id
Reservation_TABLE = '''CREATE TABLE IF NOT EXISTS Reservation
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
         Date           VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
         Appointment    VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
         state          CHAR(1)  NOT NULL,
         Type           VARCHAR(4)  NOT NULL,          
         Doctor_id          INT,
         Patient_id         INT,
         Prescription_id    INT,
         Room_id            INT,
         CONSTRAINT Prescription_Reservation FOREIGN KEY (Prescription_id) REFERENCES Prescription (ID),
         CONSTRAINT Patient_Reservation FOREIGN KEY (Patient_id) REFERENCES Patient (ID),
         CONSTRAINT Room_Reservation FOREIGN KEY (Room_id) REFERENCES Room (ID),
         CONSTRAINT Doctor_Reservation FOREIGN KEY (Doctor_id) REFERENCES Employee (ID)
         )'''
# contracts tables(global)
# GlobalContract_TABLE = '''CREATE TABLE IF NOT EXISTS GlobalContract
#          (ID INTEGER PRIMARY KEY     AUTOINCREMENT NOT NULL,
#          Terms    TEXT           NOT NULL,
#          Penalty  TEXT           NOT NULL
#          )'''

# EmployeeContract_TABLE = '''CREATE TABLE IF NOT EXISTS EmployeeContract
#          (ID INT NOT NULL,
#          E_ID INT  ,
#          GlobalContract_ID INT ,
#          PRIMARY KEY(ID,E_ID, GlobalContract_ID ),
#          CONSTRAINT Employee_Contract FOREIGN KEY (E_ID) REFERENCES Employee (ID),
#          CONSTRAINT GlobalContract_Contract FOREIGN KEY ( GlobalContract_ID ) REFERENCES GContract (ID)
#          )'''
# PatientContract_TABLE = '''CREATE TABLE IF NOT EXISTS PatientContract
#          (P_ID INT,
#          E_ID INT,
#          Doc_ID INT,
#          GlobalContract_ID  INT,
#          OP_ID INT,
#          PRIMARY KEY(P_ID,E_ID, GlobalContract_ID ,OP_ID),
#          CONSTRAINT Employee_Contract FOREIGN KEY (Doc_ID) REFERENCES Employee (ID),
#          CONSTRAINT GlobalContract_Contract FOREIGN KEY ( GlobalContract_ID ) REFERENCES GContract (ID),
#          CONSTRAINT Patient_Contract FOREIGN KEY (P_ID) REFERENCES Patient (ID),
#          CONSTRAINT Operation_Contract FOREIGN KEY (OP_ID) REFERENCES Operation (ID)
#          )'''
#room
Room_TABLE = '''CREATE TABLE IF NOT EXISTS Room
         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         LastStay VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
         Avaliable CHAR(1),
         Department_ID  INT,
         CONSTRAINT Department_Room FOREIGN KEY (Department_ID) REFERENCES Department (ID)
         )'''
#Examination
# the validity will be discussed
# Examination_TABLE = '''CREATE TABLE IF NOT EXISTS Examination
#              (
#                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                ExaminationDate VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
#                Result VARCHAR(100) NOT NULL,
#                Validity  VARCHAR(1) ,
#                ReservationId  INT ,
#                PatientId      INT,
#                DepartmentId   INT,
#                CONSTRAINT RESERVATION_REL FOREIGN KEY (ReservationId) REFERENCES Reservation (ID),
#                CONSTRAINT PATIENT_REL FOREIGN KEY (PatientId) REFERENCES Patient (ID),
#                CONSTRAINT DEPARTMENT_REL FOREIGN KEY (DepartmentId) REFERENCES Department (ID)
#              )
#              '''
#Examination&operation
# Examination_Operation_Table='''CREATE TABLE IF NOT EXISTS ExaminationAndOperation
#               (
#               Ex_ID   INT  ,
#               OP_ID   INT  ,
#               PRIMARY KEY(Ex_ID,OP_ID),
#               CONSTRAINT OPERATION_REL FOREIGN KEY (OP_ID) REFERENCES Operation (ID),
#               CONSTRAINT EXAMINATION_REL FOREIGN KEY (Ex_ID) REFERENCES Examination (ID)
#               )
#               '''
# OPERTAION TABLE
# OPERATION_Teble='''CREATE TABLE IF NOT EXISTS Operation
# (
#   ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#   STATE  CHAR(1)  NOT NULL,
#   STARTTIME  VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
#   Priority    VARCHAR(1)       NOT NULL,
#   Prequistes  VARCHAR(150)    , 
#   RESERVATION_ID     INT  ,
#   CONSTRAINT RESERVATION_OPERATION FOREIGN KEY (RESERVATION_ID) REFERENCES Reservation (ID)
# )
# '''
# DONER TABLE
DONER_Table='''CREATE TABLE IF NOT EXISTS Doner
(
  ID INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL,
  BloodType  CHAR(2)  NOT NULL,
  FNAME          CHAR(50)     NOT NULL,
  lNAME          CHAR(50)     NOT NULL,
  Email       CHAR(50)  NOT NULL,
  Phonenumber          CHAR(50)  NOT NULL
)
'''
DONATION_TABLE ='''CREATE TABLE IF NOT EXISTS Donation
(
  ID INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL,
  DonationDate  VARCHAR(18) DEFAULT '00:00AM,00/00/0000',
  DonationType  VARCHAR(50) NOT NULL ,
  DonarId int ,
  statee char(1),
  CONSTRAINT DONATION_DONAR FOREIGN KEY (DonarId) REFERENCES Doner (ID)
)
'''
Patient_Status_Table='''CREATE TABLE IF NOT EXISTS PatientStatus
              (
              PatientID  INTEGER PRIMARY KEY NOT NULL  ,
              Diabetes  VARCHAR(5) ,
              Cholestrol  VARCHAR(5) ,
              Blood_Pressure VARCHAR(5),
              Depression     VARCHAR(5),
              Max_Haert_Rate  VARCHAR(5),
              CONSTRAINT Status_Rel FOREIGN KEY (PatientID) REFERENCES Patient (ID)
              )
              '''
HOSPITAL_DB_TABLES = [Department_TABLE, Patient_TABLE, Employee_TABLE, Prescription_TABLE, Reservation_TABLE, Room_TABLE, DONER_Table,DONATION_TABLE,Patient_Status_Table]