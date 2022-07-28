from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
    
conn=sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")

#Class for BOOKING APPOINTMENT   
class Appointment:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.pat_ID=IntVar()
        self.emp_ID=StringVar()
        self.ap_no=StringVar()
        self.ap_time=StringVar()
        self.ap_date=StringVar()
        self.des=StringVar()

        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "APPOINTMENT FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpid.grid(row=0,column=0)
        self.lblpid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_ID)
        self.lblpid.grid(row=0,column=1)
        
        self.lbldid = Label(self.LoginFrame,text="DOCTOR ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldid.grid(row=1,column=0)
        self.lbldid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.emp_ID )
        self.lbldid.grid(row=1,column=1)

    
        self.lblap = Label(self.LoginFrame,text="APPOINTMENT NO",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblap.grid(row=2,column=0)
        self.lblap  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ap_no )
        self.lblap.grid(row=2,column=1)
            
        self.lblapt = Label(self.LoginFrame,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapt.grid(row=0,column=2)
        self.lblapt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ap_time )
        self.lblapt.grid(row=0,column=3)

        self.lblapd = Label(self.LoginFrame,text="APPOINTMENT DATE(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapd.grid(row=1,column=2)
        self.lblapd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.ap_date)
        self.lblapd.grid(row=1,column=3)
        
        self.lbldes = Label(self.LoginFrame,text="DESCRIPTION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldes.grid(row=2,column=2)
        self.lbldes  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.des)
        self.lbldes.grid(row=2,column=3)
        
        #===========BUTTONS============= 
        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_AP)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_AP_DISPLAY)
        self.button3.grid(row=3,column=2)
        
        
        self.button3 = Button(self.LoginFrame2, text="SEARCH APPOINTMENTS",width =20,font="Helvetica 14 bold",bg="cadet blue",command= self.S_AP_DISPLAY)
        self.button3.grid(row=3,column=3)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=4)
        
    #FUNCTION TO EXIT APPOINTMENT WINDOW
    def Exit(self):            
        self.master.destroy()
        
    #FUNCTION TO INSERT DATA IN APPOINTMENT FORM   
    def INSERT_AP(self):
        global e1,e2,e3,e4,e5,e6,var
        e1=(self.pat_ID.get())
        e2=(self.emp_ID.get())
        e3=(self.ap_no.get())
        e4=(self.ap_time.get())
        e5=(self.ap_date.get())
        e6=(self.des.get())
        conn = sqlite3.connect("HospitalDB.db")
        p = list(conn.execute("SELECT * FROM appointment WHERE AP_NO =?",(e3,)))
        x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "APPOINTMENT ALREADY EXISTS")     
        else:
            conn.execute("Insert into appointment values(?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,))
            tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "APPOINTMENT SET SUCCSESSFULLY")
        conn.commit()

    #FUNCTION TO OPEN DELETE APPOINTMENT DISPLAY WINDOW
    def DE_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DEL_AP(self.newWindow)
        
    #FUNCTION TO OPEN SEARCH APPOINTMENT DISPLAY WINDOW
    def S_AP_DISPLAY(self):
        self.newWindow= Toplevel(self.master)
        self.app = SEA_AP(self.newWindow)
           

#CLASS FOR DISPLAY MENU FOR DELETE APPOINTMENT   
class DEL_AP:
    def __init__(self,master):    
        global de1_ap,de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de1_ap=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER APPOINTMENT NO TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_ap)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_AP)
        self.DeleteB.grid(row=3,column=1)

    #FUNCTION TO DELETE DATA IN APPOINTMENT FORM      
    def DELETE_AP(self):        
        global inp_d
        inp_d = str(self.de1_ap.get())
        conn = sqlite3.connect("HospitalDB.db")
        v=list(conn.execute("select * from appointment where AP_NO=?", (inp_d ,)))
        if (len(v)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT APPOINTMENT NOT FIXED")     
        else:
            conn.execute('DELETE FROM APPOINTMENT where AP_NO=?',(inp_d ,))
            tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "PATIENT APPOINTMENT DELETED")
        conn.commit()
        
#CLASS FOR DISPLAY MENU FOR SEARCH APPOINTMENT          
class SEA_AP:
    def __init__(self,master):    
        global inp_s,entry,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.entry=StringVar()
        self.lblTitle = Label(self.frame,text = "SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER DATE TO VIEW APPOINTMENTS(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.entry)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SEARCH_AP)
        self.SearchB.grid(row=0,column=1)
        
    #FUNCTION TO SEARCH DATA IN APPOINTMENT FORM   
    def SEARCH_AP(self):
        global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
        c1=conn.cursor()
        ap=(self.entry.get())
        p = list(c1.execute("select * from appointment where AP_DATE=?", (ap,)))
        if (len(p) == 0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","THERE'S NO APPOINTMENT BOOKED")
        else:
            t=c1.execute('SELECT PATIENT_ID,NAME,AP_NO,EMP_ID,AP_DATE,AP_TIME FROM PATIENT NATURAL JOIN appointment where AP_DATE=?',(ap,))          
            for i in t:
                self.l1 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l1.grid(row=1,column=0)
                self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
                self.dis1.grid(row=1,column=1)                        
                self.l2 = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l2.grid(row=2,column=0)
                self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[1])
                self.dis2.grid(row=2,column=1)

                self.l3 = Label(self.LoginFrame,text="APPOINTMENT NO",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l3.grid(row=3,column=0)
                self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[2])
                self.dis3.grid(row=3,column=1)

                self.l4 = Label(self.LoginFrame,text="DOCTOR ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l4.grid(row=4,column=0)
                self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[3])
                self.dis4.grid(row=4,column=1)
                        
                self.l5 = Label(self.LoginFrame,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l5.grid(row=5,column=0)
                self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[5])
                self.dis5.grid(row=5,column=1)


  
               
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
    
conn=sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")

#Class for BILLING  
class Billing:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.P_id=IntVar()
        self.dd = StringVar()
        self.treat_1=StringVar()
        self.treat_2=StringVar()
        self.cost_t=IntVar()
        self.med=StringVar()
        self.med_q=IntVar()
        self.price=IntVar()
                
        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "BILLING WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpid.grid(row=0,column=0)
        self.lblpid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.P_id )
        self.lblpid.grid(row=0,column=1)
        
        self.lbldid = Label(self.LoginFrame,text="DATE DISCHARGED(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldid.grid(row=1,column=0)
        self.lbldid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.dd )
        self.lbldid.grid(row=1,column=1)       
        self.button2 = Button(self.LoginFrame, text="UPDATE DISCHARGE DATE",width =25,font="Helvetica 14 bold",bg="cadet blue",command = self.UPDATE_DATE)
        self.button2.grid(row=1,column=3)
        
        self.lbltreat= Label(self.LoginFrame,text="TREATMENT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbltreat.grid(row=2,column=0)
        self.lbltreat  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.treat_1 )
        self.lbltreat.grid(row=2,column=1) 
  
        self.lblcode_t1= Label(self.LoginFrame,text="TREATMENT CODE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblcode_t1.grid(row=3,column=0)
        self.lblcode_t1= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.treat_2)
        self.lblcode_t1.grid(row=3,column=1)

        
        self.lblap = Label(self.LoginFrame,text="TREATMENT COST ₹",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblap.grid(row=4,column=0)
        self.lblap  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.cost_t)
        self.lblap.grid(row=4,column=1)
            
        self.lblmed = Label(self.LoginFrame,text="MEDICINE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblmed.grid(row=2,column=2)
        self.lblmed  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.med)
        self.lblmed.grid(row=2,column=3)
        
        self.med_t1= Label(self.LoginFrame,text="MEDICINE QUANTITY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.med_t1.grid(row=3,column=2)
        self.med_t1 = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.med_q)
        self.med_t1.grid(row=3,column=3)
        
        self.lblapd = Label(self.LoginFrame,text="MEDICINE PRICE ₹",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapd.grid(row=4,column=2)
        self.lblapd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.price)
        self.lblapd.grid(row=4,column=3)

        #===========BUTTONS=============    
        self.button3 = Button(self.LoginFrame2, text="UPDATE DATA",width =15,font="Helvetica 14 bold",bg="cadet blue",command= self.UPDATE_DATA)
        self.button3.grid(row=3,column=2)
        
        self.button3 = Button(self.LoginFrame2, text="GENERATE BILL",width =15,font="Helvetica 14 bold",bg="cadet blue",command= self.GEN_BILL)
        self.button3.grid(row=3,column=3)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=4)

    #FUNCTION TO UPDATE DATE IN BILLING FORM 
    def UPDATE_DATE(self):
        global b1,b2
        conn = sqlite3.connect("HospitalDB.db")
        conn.cursor()
        b1 = (self.P_id.get())
        b2 =(self.dd.get())  
        conn.execute("UPDATE ROOM SET DATE_DISCHARGED=? where PATIENT_ID=?", (b2, b1,))
        conn.commit()
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DISCHARGE DATE UPDATED")
        
    #FUNCTION TO UPDATE DATA IN BILLING FORM 
    def UPDATE_DATA(self):
        global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
        conn = sqlite3.connect("HospitalDB.db")
        c1 = conn.cursor()
        b1 = (self.P_id.get())
        b3 = (self.treat_1.get())
        b4 = (self.treat_2.get())
        b5 = (self.cost_t.get())
        b6 = (self.med.get())
        b7 = (self.med_q.get())
        b8 = (self.price.get())   
        p = list(conn.execute("Select * from TREATMENT where TREATMENT.PATIENT_ID=?", (b1,)))  
        if len(p) != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT ID IS ALREADY REGISTERED")
        else:
            conn.execute("INSERT INTO TREATMENT VALUES(?,?,?,?)", (b1, b3, b4, b5,))
            conn.execute("INSERT INTO MEDICINE VALUES(?,?,?,?)", (b1, b6, b7, b8,))
            conn.commit()
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "BILLING DATA SAVED")
            
    #FUNCTION TO GENERATE BILL IN BILLING FORM 
    def GEN_BILL(self):
        global b1
        b1 = (self.P_id.get())
        conn = sqlite3.connect("HospitalDB.db")
        u=conn.execute("Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM NATURAL JOIN TREATMENT natural JOIN MEDICINE where PATIENT_ID=?",(b1,) )
        for ii in u:
            self.pp=Label(self.LoginFrame,text="TOTAL AMOUNT OUTSTANDING",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.pp.grid(row=5,column=0)
            self.uu=Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=22,text=ii[0])
            self.uu.grid(row=5,column=1) 

    #FUNCTION TO EXIT BILLING WINDOW       
    def Exit(self):            
        self.master.destroy()
        

import sqlite3
conn=sqlite3.connect("HospitalDB.db")

print("DATABASE CONNECTION SUCCESSFUL")
#conn.execute("Drop table if EXISTS PATIENT")
#c = conn.cursor()
#conn.execute("""Create table PATIENT
 #           (PATIENT_ID int(10) primary key,
  #           NAME VARCHAR(20) not null,
   #          SEX varchar(10) not null,
    #         BLOOD_GROUP varchar(5) not null,
     #        DOB date not null,
      #       ADDRESS varchar(100) not null,
       #      CONSULT_TEAM varchar(50) not null,
        #     EMAIL varchar(20) not null
         #    )""")
print("PATIENT TABLE CREATED SUCCESSFULLY")         
#conn.execute("Drop table if EXISTS CONTACT_NO")
#c = conn.cursor()
#conn.execute("""CREATE TABLE CONTACT_NO
 #           (PATIENT_ID int(10) PRIMARY KEY,
  #           CONTACTNO int(15) not null,
   #          ALT_CONTACT int(15),
    #         FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID))
     #       """)
print("CONTACT_NO TABLE CREATED SUCCESSFULLY")
#conn.execute("Drop table if EXISTS employee")
#c = conn.cursor()
#conn.execute("""create table employee
 #           (EMP_ID varchar(10) primary key,
  #          EMP_NAME varchar(20)not null,
   #          SEX varchar(10) not null,
    #         AGE int(5) not null,
     #        DESIG varchar(20) not null,
      #       SAL int(10) not null,
       #   EXP varchar(100) not null,
        #     EMAIL varcahr(20) not null,
         #   PHONE int(12))""")

print("EMPLOYEE TABLE CREATED SUCCESSFULLY")

#conn.execute("Drop table if EXISTS TREATMENT")
#c = conn.cursor()
#conn.execute("""CREATE TABLE TREATMENT
 #           (PATIENT_ID int(10) primary key,
  #           TREATMENT varchar(100) not null,
   #          TREATMENT_CODE varchar(30) not null,
    #         T_COST int(20) not null,
     #       FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID));
      #       """)
print("TREATMENT TABLE CREATED SUCCESSFULLY")

#conn.execute("Drop table if EXISTS MEDICINE")
#c = conn.cursor()
#conn.execute("""CREATE TABLE MEDICINE
 #           (PATIENT_ID int(10) primary key,
  #           MEDICINE_NAME varchar(100) not null,
   #          M_COST int(20) not null,
    #         M_QTY int(10) not null,
     #        FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID));
      #       """)
print("MEDICINE TABLE CREATED SUCCESSFULLY")

#conn.execute("Drop table if EXISTS ROOM")
#c = conn.cursor()
#conn.execute("""Create table ROOM
         # (PATIENT_ID int(10)not NULL ,
          #  ROOM_NO varchar(20) PRIMARY KEY ,
          #ROOM_TYPE varchar(10) not null,
          #  RATE int(10) not null,
           # DATE_ADMITTED date,
            # DATE_DISCHARGED date NULL,
           # FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
            #);
           # """)
print("ROOM TABLE CREATED SUCCESSFULLY")

conn.execute("Drop table if EXISTS APPOINTMENT")
c = conn.cursor()
c.execute("""create table appointment
            (
             PATIENT_ID int(20) not null,
             EMP_ID varchar(10) not null,
             AP_NO varchar(10) primary key,
             AP_TIME time,
             AP_DATE date,
             description varchar(100),
             FOREIGN KEY(PATIENT_ID) references PATIENT(PATIENT_ID),
             FOREIGN KEY(EMP_ID) references employee(EMP_ID));""")
print("APPOINTMENT TABLE CREATED SUCCESSFULLY")
conn.commit()
conn.close()
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3


conn=sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")

#Class for EMPLOYEE REGISTRATION 
class Employee:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.emp_ID=StringVar()
        self.emp_name=StringVar()
        self.emp_sex=StringVar()
        self.emp_age=IntVar()
        self.emp_type=StringVar()
        self.emp_salary=IntVar()
        self.emp_exp=StringVar()
        self.emp_email=StringVar()
        self.emp_phno=IntVar()


        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "EMPLOYEE REGISTRATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblempid = Label(self.LoginFrame,text="EMPLOYEE ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblempid.grid(row=0,column=0)
        self.lblempid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_ID)
        self.lblempid.grid(row=0,column=1)
        
        self.lblempname = Label(self.LoginFrame,text="EMPLOYEE NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblempname.grid(row=1,column=0)
        self.lblempname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_name)
        self.lblempname.grid(row=1,column=1)

        self.lblsex = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblsex.grid(row=2,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_sex)
        self.etype1.grid(row=2,column=1)
        

        self.lblage = Label(self.LoginFrame,text="AGE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblage.grid(row=3,column=0)
        self.lblage  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_age)
        self.lblage.grid(row=3,column=1)
        
        self.etype1=Label(self.LoginFrame,text="EMPLOYEE DESIGNATION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.etype1.grid(row=4,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_type)
        self.etype1.grid(row=4,column=1)

        self.lblCon = Label(self.LoginFrame,text="SALARY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblCon.grid(row=0,column=2)
        self.lblCon  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_salary)
        self.lblCon.grid(row=0,column=3)
        
        self.lblAlt = Label(self.LoginFrame,text="EXPERIENCE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblAlt.grid(row=1,column=2)
        self.lblAlt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_exp)
        self.lblAlt.grid(row=1,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=2,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_phno)
        self.lbleid.grid(row=2,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=3,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_email)
        self.lbleid.grid(row=3,column=3)

        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_EMP)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_DISPLAY)
        self.button3.grid(row=3,column=2)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=3)
        

   #FUNCTION TO EXIT PATIENT FORM
    def Exit(self):            
        self.master.destroy()
        
    #FUNCTION TO INSERT DATA IN EMPLOYEE FORM
        
    def INSERT_EMP(self):
        global e1,e2,e3,e4,e5,e6,e7,e8,e9,var
        e1=(self.emp_ID.get())
        e2=(self.emp_name.get())
        e3=(self.emp_sex.get())
        e4=(self.emp_age.get())
        e5=(self.emp_type.get())
        e6=(self.emp_salary.get())
        e7=(self.emp_exp.get())
        e8=(self.emp_email.get())
        e9=(self.emp_phno.get())
        conn = sqlite3.connect("HospitalDB.db")     
        p = list(conn.execute("SELECT * FROM employee  WHERE EMP_ID =?",(e1,)))
        x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "EMPLOYEE ID ALREADY EXISTS")     
        else:
            conn.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA ADDED")
        conn.commit()
                
    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def DE_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = D_EMP(self.newWindow)


#CLASS FOR DISPLAY MENU FOR DELETE EMPLOYEE
class D_EMP:
    def __init__(self,master):    
        global de1_emp,de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de1_emp=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE EMPLOYEE WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER EMPLOYEE ID TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_emp)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_EMP)
        self.DeleteB.grid(row=3,column=1)
        
    #FUNCTION TO DELETE DATA IN EMPLOYEE FORM 
    def DELETE_EMP(self):        
        global inp_d
        de = str(self.de1_emp.get())
        conn = sqlite3.connect("HospitalDB.db")
        p = list(conn.execute("select * from employee where EMP_ID=?", (de,)))
        if (len(p) != 0):
            conn.execute("DELETE from employee where EMP_ID=?", (de,))
            dme = tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DELETED")
            
        else:
            error = tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DOESN'T EXIST")
        conn.commit()   
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font

from menu import Menu

def main():
    root = Tk()
    app= MainWindow(root)
#MAIN WINDOW FOR LOG IN
class MainWindow:
    # constructor
    def __init__(self,master):
        # public data mambers
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x500+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master,bg="powder blue")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame,text = "HOSPITAL MANAGEMENT SYSTEM", font="Helvetica 20 bold",bg="powder blue",fg="black")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=40)
        #======================
        self.LoginFrame1 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame1.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #======LABEL AND ENTRY=========
        self.lblUsername = Label(self.LoginFrame1,text="Username",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.lblUsername = Entry(self.LoginFrame1,font="Helvetica 14 bold",textvariable= self.Username,bd=2)
        self.lblUsername.grid(row=0,column=1)
        self.lblPassword = Label(self.LoginFrame1,text="Password ",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblPassword .grid(row=1,column=0)
        self.lblPassword  = Entry(self.LoginFrame1,font="Helvetica 14 bold",show="*",textvariable= self.Password,bd=2)
        self.lblPassword .grid(row=1,column=1)
        #===========BUTTONS====
        self.btnLogin = Button(self.LoginFrame2,text = "Login" ,font="Helvetica 10 bold", width =10 ,bg="powder blue",command = self.Login_system)
        self.btnLogin.grid(row=3,column=0)
        self.btnExit = Button(self.LoginFrame2,text = "Exit" ,font="Helvetica 10 bold", width =10 ,bg="powder blue",command = self.Exit)
        self.btnExit.grid(row=3,column=1)
    # public member function  
    #Function for LOGIN
    def Login_system(self):

        S1=(self.Username.get())
        S2=(self.Password.get())
        if(S1=='admin' and S2=='1234'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        elif(S1=='root' and S2=='4321'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        else:
            tkinter.messagebox.askretrycancel("HOSPITAL MANAGEMENT SYSTEM" , "PLEASE ENTER VALID USERNAME AND PASSWORD")
    #Function for Exit
    def Exit(self):
        self.master.destroy()




if __name__ == "__main__":
    main()
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
from patient_form import Patient
from room_form import Room
from employee_form import Employee
from appointment_form import Appointment
from billing_form import Billing

conn=sqlite3.connect("HospitalDB.db")

print("DATABASE CONNECTION SUCCESSFUL")

#Class For Menu    
class Menu:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x600+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
       
        self.lblTitle = Label(self.frame,text = "MAIN MENU", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        #===========BUTTONS============= 
        self.button1 = Button(self.LoginFrame,text = "1.PATIENT REGISTRATION", width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Patient_Reg)       
        self.button1.grid(row=1,column=0,pady=10)
        
        self.button2 = Button(self.LoginFrame, text="2.ROOM ALLOCATION",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Room_Allocation)
        self.button2.grid(row=3,column=0,pady=10)
        
        self.button3 = Button(self.LoginFrame, text="3.EMPLOYEE REGISTRATION",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Employee_Reg)
        self.button3.grid(row=5,column=0,pady=10)
        
        self.button4 = Button(self.LoginFrame, text="4.BOOK APPOINTMENT",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Appointment_Form)
        self.button4.grid(row=7,column=0,pady=10)
        
        self.button5 = Button(self.LoginFrame, text="5.PATIENT BILL",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Billing_Form)
        self.button5.grid(row=9,column=0,pady=10)
        
        self.button6 = Button(self.LoginFrame, text="6.EXIT",width =30,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=11,column=0,pady=10)
        
    #Function to Exit Menu Window
    def Exit(self):
        self.master.destroy()

    
    #Function to open Patient Registration Window   
    def Patient_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow)
        
    #Function to open Room Allocation Window   

    def Room_Allocation(self):
        self.newWindow = Toplevel(self.master)
        self.app = Room(self.newWindow)
        
    #Function to open Employee Registration Window 
    def Employee_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Employee(self.newWindow)
        
    #Function to open Appointment Window
    def Appointment_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Appointment(self.newWindow)
        
    #Function to open Billing Window
    def Billing_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Billing(self.newWindow)


from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3


conn=sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")
                      
#Class for PATIENT REGISTRATION 
class Patient:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.pat_ID=IntVar()
        self.pat_name=StringVar()
        self.pat_dob=StringVar()
        self.pat_address=StringVar()
        self.pat_sex=StringVar()
        self.pat_BG=StringVar()
        self.pat_email=StringVar()
        self.pat_contact=IntVar()
        self.pat_contactalt=IntVar()
        self.pat_CT=StringVar()


        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "PATIENT REGISTRATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_ID)
        self.lblpatid.grid(row=0,column=1)
        
        self.lblPatname = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblPatname.grid(row=1,column=0)
        self.lblPatname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_name)
        self.lblPatname.grid(row=1,column=1)

        self.lblsex = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblsex.grid(row=2,column=0)
        self.lblsex  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_sex)
        self.lblsex.grid(row=2,column=1)

        self.lblDOB = Label(self.LoginFrame,text="DOB (YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblDOB.grid(row=3,column=0)
        self.lblDOB  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_dob)
        self.lblDOB.grid(row=3,column=1)
        
        self.lblbgrp = Label(self.LoginFrame,text="BLOOD GROUP",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblbgrp.grid(row=4,column=0)
        self.lblbgrp  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_BG)
        self.lblbgrp.grid(row=4,column=1)
        
        self.lblCon = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblCon.grid(row=0,column=2)
        self.lblCon  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_contact)
        self.lblCon.grid(row=0,column=3)
        
        self.lblAlt = Label(self.LoginFrame,text="ALTERNATE CONTACT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblAlt.grid(row=1,column=2)
        self.lblAlt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_contactalt)
        self.lblAlt.grid(row=1,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=2,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_email)
        self.lbleid.grid(row=2,column=3)

        self.lbldoc = Label(self.LoginFrame,text="CONSULTING TEAM / DOCTOR",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldoc.grid(row=3,column=2)
        self.lbldoc  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_CT)
        self.lbldoc.grid(row=3,column=3)

        self.lbladd = Label(self.LoginFrame,text="ADDRESS",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbladd.grid(row=4,column=2)
        self.lbladd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_address)
        self.lbladd.grid(row=4,column=3)
        
        #===========BUTTONS============= 
        self.button2 = Button(self.LoginFrame2, text="SUBMIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_PAT)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="UPDATE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.UPDATE_PAT)
        self.button3.grid(row=3,column=2)
        
        self.button4 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.D_DISPLAY)
        self.button4.grid(row=3,column=3)
        
        self.button5 = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.S_DISPLAY)
        self.button5.grid(row=3,column=4)
        
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=5)
            

    #FUNCTION TO INSERT DATA IN PATIENT FORM
    def INSERT_PAT(self):
        global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1,conn
        conn=sqlite3.connect("HospitalDB.db")
        conn.cursor()
        p1=(self.pat_ID.get())
        p2=(self.pat_name.get())
        p3=(self.pat_sex.get())
        p4=(self.pat_BG.get())
        p5=(self.pat_dob.get())
        p6=(self.pat_contact.get())
        p7=(self.pat_contactalt.get())
        p8=(self.pat_address.get())
        p9=(self.pat_CT.get())
        p10=(self.pat_email.get())
        p = list(conn.execute("SELECT * FROM PATIENT  WHERE PATIENT_ID =?",(p1,)))
        x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","PATIENT_ID ALREADY EXISTS")
        else:
            conn.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)',(p1,p2,p3,p4,p5,p8,p9,p10,))
            conn.execute('INSERT INTO CONTACT_NO VALUES (?,?,?)',(p1,p6,p7,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM","DETAILS INSERTED INTO DATABASE")
        conn.commit()
        
    #FUNCTION TO UPDATE DATA IN PATIENT FORM

    def UPDATE_PAT(self):
        global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, conn
        conn.cursor()
        u1 = (self.pat_ID.get())
        u2 = (self.pat_name.get())
        u3 = (self.pat_sex.get())
        u4 = (self.pat_dob.get())
        u5 = (self.pat_BG.get())
        u6 = (self.pat_contact.get())
        u7 = (self.pat_contactalt.get())
        u8 = (self.pat_email.get())
        u9 = (self.pat_CT.get())
        u10 = (self.pat_address.get())
        conn = sqlite3.connect("HospitalDB.db")
        p = list(conn.execute("Select * from PATIENT where PATIENT_ID=?", (u1,)))
        if len(p) != 0:
            conn.execute('UPDATE PATIENT SET NAME=?,SEX=?,DOB=?,BLOOD_GROUP=?,ADDRESS=?,CONSULT_TEAM=?,EMAIL=? where PATIENT_ID=?', ( u2, u3, u4, u5, u10, u9, u8,u1,))
            conn.execute('UPDATE CONTACT_NO set CONTACTNO=?,ALT_CONTACT=? WHERE PATIENT_ID=?', ( u6, u7,u1,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS UPDATED INTO DATABASE")
            conn.commit()

        else:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")
            
    #FUNCTION TO EXIT PATIENT REGISTRATION WINDOW
    def Exit(self):            
        self.master.destroy()

    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def D_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DMenu(self.newWindow)
        
    #FUNCTION TO OPEN SEARCH PATIENT DISPLAY WINDOW
    def S_DISPLAY(self):
        self.newWindow= Toplevel(self.master)
        self.app = SMenu(self.newWindow)

#CLASS FOR DISPLAY MENU FOR DELETE PATIENT
class DMenu:
    def __init__(self,master):    
        global inp_d,entry1,DeleteB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.del_pid=IntVar()
        self.lblTitle = Label(self.frame,text = "DELETE WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.del_pid)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_PAT)
        self.DeleteB.grid(row=3,column=1)

    #FUNCTION TO DELETE DATA IN PATIENT FORM
    def DELETE_PAT(self):        
        global inp_d,del_pid
        c1= conn.cursor()
        inp_d = (self.del_pid.get())
        p=list(conn.execute("select * from PATIENT where PATIENT_ID=?", (inp_d,)))
        if (len(p)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","PATIENT RECORD NOT FOUND")
        else:
            conn.execute('DELETE FROM PATIENT where PATIENT_ID=?',(inp_d,))
            conn.execute('DELETE FROM CONTACT_NO WHERE PATIENT_ID=?', (inp_d,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS DELETED FROM DATABASE")
            conn.commit()

#CLASS FOR SEARCH MENU FOR SEARCH PATIENT
class SMenu:
    def __init__(self,master):    
        global inp_s,s_pid,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.s_pid=IntVar()
        self.lblTitle = Label(self.frame,text = "SEARCH WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO SEARCH",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.s_pid)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SEARCH_PAT)
        self.SearchB.grid(row=0,column=1)
        
    #FUNCTION TO SEARCH DATA IN PATIENT FORM
    def SEARCH_PAT(self):
        global inp_s,s_pid,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
        c1=conn.cursor()
        inp_s=(self.s_pid.get())                
        p=list(conn.execute('select * from PATIENT where PATIENT_ID=?',(inp_s,)))
        if (len(p)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","PATIENT RECORD NOT FOUND")
                    
        else:
            t=c1.execute('SELECT * FROM PATIENT NATURAL JOIN CONTACT_NO where PATIENT_ID=?',(inp_s,));
            for i in t:
                        self.l1 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l1.grid(row=1,column=0)
                        self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
                        self.dis1.grid(row=1,column=1)
                        
                        self.l2 = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l2.grid(row=2,column=0)
                        self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[1])
                        self.dis2.grid(row=2,column=1)

                        self.l3 = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l3.grid(row=3,column=0)
                        self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[2])
                        self.dis3.grid(row=3,column=1)

                        self.l4 = Label(self.LoginFrame,text="DOB (YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l4.grid(row=4,column=0)
                        self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[4])
                        self.dis4.grid(row=4,column=1)
                        
                        self.l5 = Label(self.LoginFrame,text="BLOOD GROUP",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l5.grid(row=5,column=0)
                        self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[3])
                        self.dis5.grid(row=5,column=1)
                        
                        self.l6 = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l6.grid(row=1,column=2)
                        self.dis6  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[8])
                        self.dis6.grid(row=1,column=3)
                        
                        self.l7 = Label(self.LoginFrame,text="ALTERNATE CONTACT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l7.grid(row=2,column=2)
                        self.dis7  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[9])
                        self.dis7.grid(row=2,column=3)
                        
                        self.l8 = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l8.grid(row=3,column=2)
                        self.dis8  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[7])
                        self.dis8.grid(row=3,column=3)

                        self.l9 = Label(self.LoginFrame,text="CONSULTING TEAM / DOCTOR",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l9.grid(row=4,column=2)
                        self.dis9  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[6])
                        self.dis9.grid(row=4,column=3)

                        self.l10 = Label(self.LoginFrame,text="ADDRESS",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l10.grid(row=5,column=2)
                        self.dis10 = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[5])
                        self.dis10.grid(row=5,column=3)
                
      
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
conn=sqlite3.connect("HospitalDB.db")

#Class for ROOM ALLOCATION    
class Room:
    
    def __init__(self,master):

        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        self.P_id=IntVar()
        self.room_t=StringVar()
        self.room_no=StringVar()
        self.rate=IntVar()
        self.da=StringVar()
        self.dd=StringVar()
      
        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "ROOM ALLOCATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.P_id)
        self.lblpatid.grid(row=0,column=1)
        self.room_t1= Label(self.LoginFrame,text="ROOM TYPE\nSINGLE ROOM: Rs 4500\nTWIN SHARING : Rs2500\nTRIPLE SHARING: Rs2000\n",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.room_t1.grid(row=1,column=0)
        self.room_t1 = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.room_t)
        self.room_t1.grid(row=1,column=1)
        
        self.room_no1=Label(self.LoginFrame,text="ROOM NUMBER ",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.room_no1.grid(row=2,column=0)

        self.room_no1 = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.room_no)
        self.room_no1.grid(row=2,column=1)
        self.lblrate=Label(self.LoginFrame,text="ROOM CHARGES",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblrate.grid(row=0,column=2)
        self.lblrate=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.rate)
        self.lblrate.grid(row=0,column=3)
        self.lblda=Label(self.LoginFrame,text="DATE ADMITTED",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblda.grid(row=1,column=2)
        self.lblda=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.da)
        self.lblda.grid(row=1,column=3)
        self.lbldd=Label(self.LoginFrame,text="DATE DISCHARGED",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldd.grid(row=2,column=2)
        self.lbldd=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.dd)
        self.lbldd.grid(row=2,column=3)
        #===========BUTTONS============= 
        self.button2 = Button(self.LoginFrame2, text="SUBMIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command=self.INSERT_ROOM)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="UPDATE",width =10,font="Helvetica 14 bold",bg="cadet blue",command=self.UPDATE_ROOM)
        self.button3.grid(row=3,column=2)
        
        self.button5 = Button(self.LoginFrame2, text="ROOM DETAILS",width =15,font="Helvetica 14 bold",bg="cadet blue",command=self.SEARCH_ROOM)
        self.button5.grid(row=3,column=4)
        
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=5)
        
    #FUNCTION TO INSERT DATA IN ROOM ALLOCATION FORM
    def INSERT_ROOM(self):
        global r1,r2,r3,r4,r5,r6,conn,p
        conn = sqlite3.connect("HospitalDB.db")
        conn.cursor()
        r1=(self.P_id.get())
        r2=(self.room_t.get())
        r3=(self.room_no.get())
        r4=(self.rate.get())
        r5=(self.da.get())
        r6=(self.dd.get())
        p = list(conn.execute("SELECT * FROM ROOM WHERE ROOM_NO=?",(r3,)))
        x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","ROOM_NO IS CURRENTLY OCCUPIED")
        else:
            conn.execute('INSERT INTO ROOM VALUES(?,?,?,?,?,?)',(r1,r3, r2, r4, r5, r6,))
            tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM", "ROOM ALLOCATED")
            conn.commit()
            
    #FUNCTION TO OPEN SEARCH MENU IN ROOM ALLOCATION FORM
    def SEARCH_ROOM(self):
        self.newWindow= Toplevel(self.master)
        self.app = S_Room(self.newWindow)
        
    #FUNCTION TO EXIT ROOM ALLOCATION FORM
    def Exit(self):            
        self.master.destroy()   

    #FUNCTION TO UPDATE DATA IN ROOM ALLOCATION FORM       
    def UPDATE_ROOM(self):
        global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
        r1=(self.P_id.get())
        r2=(self.room_t.get())
        r3=(self.room_no.get())
        r4=(self.rate.get())
        r5=(self.da.get())
        r6=(self.dd.get())
        p = list(conn.execute("Select * from ROOM where PATIENT_ID=? AND ROOM_NO=?",(r1,r3,)))
        if len(p) != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT IS NOT ALLOCATED A ROOM")

        else:
            conn.execute('UPDATE ROOM SET ROOM_NO=?,ROOM_TYPE=?,RATE=?,DATE_ADMITTED=?,DATE_DISCHARGED=? where PATIENT_ID=?',(r3, r2, r4, r5, r6,r1,))
            tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM", "ROOM DETAILS UPDATED")
            conn.commit()

#CLASS FOR DISPLAY MENU FOR SEARCH ROOM
class S_Room:
    def __init__(self,master):    
        global inp_s,entry,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.Pr_id=IntVar()
        self.lblTitle = Label(self.frame,text = "SEARCH PATIENT DETAILS", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO SEARCH",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.Pr_id)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.ROOM_DISPLAY)
        self.SearchB.grid(row=0,column=1)    

    #FUNCTION TO SEARCH DATA IN ROOM ALLOCATION FORM
    def ROOM_DISPLAY(self):
        global pat_rm,lr1,dis1,lr2,dis2,c1,i,conn,c1,Pr_id
        conn = sqlite3.connect("HospitalDB.db")
        c1=conn.cursor()        
        pat_rm=(self.Pr_id.get())
        p=list(c1.execute('select * from  ROOM  where PATIENT_ID=?',(pat_rm,)))
        if (len(p)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","PATIENT NOT ALLOCATED ROOM")
        else:
            t=c1.execute('SELECT PATIENT_ID,NAME,ROOM_NO,ROOM_TYPE FROM ROOM NATURAL JOIN PATIENT where PATIENT_ID=?',(pat_rm,));
            for i in t:
            
                self.l1 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l1.grid(row=1,column=0)
                self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
                self.dis1.grid(row=1,column=1)
                        
                self.l2 = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l2.grid(row=2,column=0)
                self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[1])
                self.dis2.grid(row=2,column=1)

                self.l3 = Label(self.LoginFrame,text="ROOM NO",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l3.grid(row=1,column=2)
                self.dis3= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[2])
                self.dis3.grid(row=1,column=3)

                self.l4 = Label(self.LoginFrame,text="ROOM TYPE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l4.grid(row=2,column=2)
                self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[3])
                self.dis4.grid(row=2,column=3)                 
                       

  
