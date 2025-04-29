from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Rooms_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1319x580+200+230")

        # Variables

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtaxes=StringVar()
        self.var_subtotal=StringVar()
        self.var_totalcost=StringVar()
        
        

       # @title

        lbl_title=Label(self.root,text="Room Booking Details", font=("TT RICKS",18,"bold"),bg="black",fg="pink",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1319,height=50)
 
        #@ logo on ROOM BOOKING 

        img1=Image.open(r"C:\Users\tryto\Desktop\Capstone Project\hms full project (1)\images\Roomsection.jpg")
        img1=img1.resize((95,48),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg= Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=95,height=48)

        # @ Label framing

        labelframeleft=LabelFrame(self.root,text="Room Booking Details",font=("TT RICKS",12,"bold"),bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2)
        labelframeleft.place(x=5,y=50,width=430,height=500)


         # label and entry
        # room contact
    
        lbl_contactroom=Label(labelframeleft,text="Customer Contact : ", font=("arial", 12, "bold"),bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_contactroom.grid(row=0, column=0,sticky=W)    

        entry_contactroom=ttk.Entry(labelframeleft,width=19,textvariable=self.var_contact,font=("arial",13))
        entry_contactroom.grid(row=0,column=1,sticky=W)

        # Find data button
        btnfind=Button(labelframeleft,command=self.Find_contact,text="Find", font=("arial",10, "bold"),bg="Tan", fg="white",width=6,cursor="hand2")
        btnfind.place(x=340,y=3)

         # check in date
        
        lbl_checkin=Label(labelframeleft,font=("arial", 12, "bold"),text="Check in Date: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_checkin.grid(row=1, column=0,sticky=W)    

        txtcheckin=ttk.Entry(labelframeleft,width=27,textvariable=self.var_checkin,font=("arial",13))
        txtcheckin.grid(row=1,column=1)

         # checkout date
        
        lbl_checkout=Label(labelframeleft,font=("arial", 12, "bold"),text="Check out Date: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_checkout.grid(row=2, column=0,sticky=W)    

        txtcheckout=ttk.Entry(labelframeleft,width=27,textvariable=self.var_checkout,font=("arial",13))
        txtcheckout.grid(row=2,column=1)

        # Room type
        
        lbl_Roomtype=Label(labelframeleft,font=("arial", 12, "bold"),text="Room Type: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_Roomtype.grid(row=3, column=0,sticky=W) 

        connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
        my_cursor=connection.cursor()
        my_cursor.execute("select RoomType from details")
        rowsss=my_cursor.fetchall() 


        Roomtype_combo=ttk.Combobox(labelframeleft,font=("arial", 12),textvariable=self.var_roomtype,width=25,state="readonly")
        Roomtype_combo["value"]=rowsss  
        Roomtype_combo.current(2)
        Roomtype_combo.grid(row=3,column=1)  

        # Available Room 
        lbl_availablerooms=Label(labelframeleft,font=("arial", 12, "bold"),text="Available Room: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_availablerooms.grid(row=4, column=0,sticky=W)    

        #txtavailablerooms=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=27,font=("arial",13))
        #txtavailablerooms.grid(row=4,column=1)
        connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
        my_cursor=connection.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        RoomNo_combo=ttk.Combobox(labelframeleft,font=("arial", 12),textvariable=self.var_roomavailable,width=25,state="readonly")
        RoomNo_combo["value"]=rows 
        RoomNo_combo.current(0)
        RoomNo_combo.grid(row=4,column=1) 

        # Meals 
        lbl_meals=Label(labelframeleft,font=("arial", 12, "bold"),text="Meal: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_meals.grid(row=5, column=0,sticky=W)    

        txtmeals=ttk.Entry(labelframeleft,width=27,textvariable=self.var_meal,font=("arial",13))
        txtmeals.grid(row=5,column=1)

        #No of days 

        lbl_Noofdays=Label(labelframeleft,font=("arial", 12, "bold"),text="No of Days: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_Noofdays.grid(row=6, column=0,sticky=W)    

        txtnoofdays=ttk.Entry(labelframeleft,width=27,textvariable=self.var_noofdays,font=("arial",13))
        txtnoofdays.grid(row=6,column=1)

        # Paid taxes

        lbl_paidtaxes=Label(labelframeleft,font=("arial", 12, "bold"),text="Paid Taxes: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_paidtaxes.grid(row=7, column=0,sticky=W)  

        txtpaidtaxes=ttk.Entry(labelframeleft,textvariable=self.var_paidtaxes,width=27,font=("arial",13))
        txtpaidtaxes.grid(row=7,column=1)
        
        # Sub Total

        lbl_subtotal=Label(labelframeleft,font=("arial", 12, "bold"),text="Sub Total: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_subtotal.grid(row=8, column=0,sticky=W)  

        txtsubtotal=ttk.Entry(labelframeleft,textvariable=self.var_subtotal,width=27,font=("arial",13))
        txtsubtotal.grid(row=8,column=1)
        
        #Total Cost

        lbl_totalcost=Label(labelframeleft,font=("arial", 12, "bold"),text="Total Cost: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_totalcost.grid(row=9, column=0,sticky=W)  

        txttotalcost=ttk.Entry(labelframeleft,width=27,textvariable=self.var_totalcost,font=("arial",13))
        txttotalcost.grid(row=9,column=1)

        # Bill BUton

        btnbill=Button(labelframeleft, text="Bill:",command=self.total,font=("arial",12, "bold"),bg="Black", fg="white",width=9,cursor="hand2")
        btnbill.grid(row=11,column=0,padx=2,sticky=W)



        # @ BUTTONS BELOW ALL OPTIONS

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=15,y=400,width=395,height=40)

        # 1st button

        btnAdd=Button(btn_frame, text="Add New",command=self.add_data,font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnAdd.grid(row=0,column=0)
        

        # @2nd button

        btnupdate=Button(btn_frame, text="Update",command=self.update,font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnupdate.grid(row=0,column=1)


        # @ 3rd button

        btndelete=Button(btn_frame, text="Delete",command=self.delete, font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btndelete.grid(row=0,column=2)

        # @ 4th button

        btnreset=Button(btn_frame, text="Reset",command=self.reset,font=("arial",12, "bold"),bg="Tan", fg="white",width=8,cursor="hand2")
        btnreset.grid(row=0,column=3)

        # Images under Room section

        img2=Image.open(r"D:\HMS project files\images\Roomsection.jpg")
        img2=img2.resize((450,240),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg= Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=860,y=55,width=450,height=240)



        # Table Frame search System

        tableframe=LabelFrame(self.root,text="View Details And Search System",font=("TT RICKS",12,"bold"),bg="Tan",fg="black",bd=2,relief=RIDGE,padx=2)
        tableframe.place(x=430,y=300,width=885,height=250)
       

        lblsearchby=Label(tableframe,font=("times new roman", 12, "bold"),text="Search By: ",bg="brown",fg="white",bd=2,relief=RIDGE,padx=2,pady=4)
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)   

        self.search_var=StringVar()
        search_combo=ttk.Combobox(tableframe,textvariable=self.search_var,font=("arial", 12),width=25,state="readonly")
        search_combo["value"]=("Contact No", "Available Room")  
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2)
        
        self.entry_search=StringVar()
        entry_search=ttk.Entry(tableframe,textvariable=self.entry_search,width=22,font=("arial",13))
        entry_search.grid(row=0,column=2,padx=2)
    

        btnsearch=Button(tableframe, text="Search",command=self.search, font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(tableframe, text="Show All",command=self.fetch_data, font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnshowall.grid(row=0,column=4,padx=1)

        # @ show data table

        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0, y=50,width=880,height=180)
         

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype", "roomavailable", "meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("contact",text="Customer Contact")
        self.room_table.heading("checkin",text="Check In Date")
        self.room_table.heading("checkout",text="Check Out Date ")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Available Room")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No of Days")
        
        

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=140)
        self.room_table.column("checkin",width=110)
        self.room_table.column("checkout",width=110)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

        # Add Data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Invalid", "All fields are required",parent=self.root)
        else:
            try:

                connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
                my_cursor=connection.cursor()
                my_cursor.execute("insert into room_window values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_contact.get(),                                                                              
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_noofdays.get()
                                                                                
                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Successful", "Room Booked Succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Something Went Wrong:{str(es)}",parent=self.root)


        # fetch data
    def fetch_data(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from room_window")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())   
            for i in rows:
                self.room_table.insert("",END,values=i)
            connection.commit()
        connection.close()
    # get_cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),                                                                              
        self.var_checkout.set(row[1]),
        self.var_checkin.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

        # Update button function
    def update(self):
        if not self.var_contact.get():
            messagebox.showerror("Error", "Please Enter Contact Details", parent=self.root)

        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            my_cursor.execute("update room_window set Check_in=%s, Check_out=%s,Roomtype=%s,Roomavailable=%s,Meal=%s,NoOfdays=%s where Contact=%s", (

                                                                                                                                                    self.var_checkin.get(),
                                                                                                                                                    self.var_checkout.get(),
                                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                                    self.var_roomavailable.get(),
                                                                                                                                                    self.var_meal.get(),
                                                                                                                                                    self.var_noofdays.get(),
                                                                                                                                                    self.var_contact.get()                                                                              

                                                                                                                                                                                                  

                                                                                                                                                    ))   
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Updated","Room Details Sucessfully Updated",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("Luxury Hotel", " Do you want to Delete this Customer",parent=self.root)
        if delete>0:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            query="delete from room_window where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return

        connection.commit()
        self.fetch_data()
        connection.close() 


    def reset(self):
        self.var_contact.set(""),                                                                              
        self.var_checkout.set(""),
        self.var_checkin.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtaxes.set("")
        self.var_subtotal.set("")
        self.var_totalcost.set("")




            # All Data fetching system

    def Find_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error", "Please Enter Contact Details",parent=self.root)
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            query=("select Customername from customer where ContactNumber=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                connection.commit()
                connection.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=445,y=55,width=400,height=240)

                lblName=Label(showDataframe,text="Customer Name:",font=("arial",12,"bold"),bg="beige",fg="black")
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=140,y=0)

                #Gender

                connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
                my_cursor=connection.cursor()
                query=("select Gender from customer where ContactNumber=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                lblgender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"),bg="beige",fg="black")
                lblgender.place(x=0,y=35)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=95,y=35)

                #Emails

                connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
                my_cursor=connection.cursor()
                query=("select Email from customer where ContactNumber=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"),bg="beige",fg="black")
                lblEmail.place(x=0,y=70)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=95,y=70)

                #Nationality
                connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
                my_cursor=connection.cursor()
                query=("select Nationality from customer where ContactNumber=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"),bg="beige",fg="black")
                lblNationality.place(x=0,y=105)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=95,y=105)

                # Address
                connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
                my_cursor=connection.cursor()
                query=("select Address from customer where ContactNumber=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"),bg="beige",fg="black")
                lbladdress.place(x=0,y=140)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=95,y=140)

                #Contact number

                connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
                my_cursor=connection.cursor()
                query=("select ContactNumber from customer where ContactNumber=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblnumber=Label(showDataframe,text="Contact number:",font=("arial",12,"bold"),bg="beige",fg="black")
                lblnumber.place(x=0,y=175)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=140,y=175)

            # Search System
    def search(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from customer where " + str(self.search_var.get())+" LIKE '% " + str(self.entry_search.get())+ "%'")

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)

            connection.commit()
        connection.close()        



    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(inDate-outDate).days)


        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(200)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)

            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(200)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
        
            q1=float(200)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
        
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)
        
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
        
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)
       
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Deluxe"):
        
            q1=float(500)
            q2=float(900)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)
        
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Deluxe"):
        
            q1=float(500)
            q2=float(900)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Deluxe"):
        
            q1=float(500)
            q2=float(900)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)
        
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Suite"):
        
            q1=float(800)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Suite"):
        
            q1=float(800)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Suite"):
        
            q1=float(800)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.09))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtaxes.set(Tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)



                

    
















if __name__=="__main__":
    root=Tk()
    obj=Rooms_window(root)
    root.mainloop()
