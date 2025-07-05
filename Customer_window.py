from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class customer_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1319x580+200+230")

        #@Variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_pincode=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()
        
        # @title

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS", font=("TT RICKS",18,"bold"),bg="black",fg="pink",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1319,height=50)
 
        #@ logo on add customer 

        img1=Image.open(r"D:\HMS project files\images\LOGO.png")
        img1=img1.resize((95,48),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg= Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=95,height=48)

        # @ Label framing

        labelframeleft=LabelFrame(self.root,text="Customer Details",font=("TT RICKS",12,"bold"),bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2)
        labelframeleft.place(x=5,y=50,width=430,height=500)
       
        # label and entry
        # customer 
    
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref : ", font=("arial", 12, "bold"),bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_cust_ref.grid(row=0, column=0,sticky=W)    

        entry_cust_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=27,font=("arial",13),state="readonly")
        entry_cust_ref.grid(row=0,column=1)

        # customer name
        
        cust_name=Label(labelframeleft,font=("arial", 12, "bold"),text="Customer Name: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        cust_name.grid(row=1, column=0,sticky=W)    

        entry_cust_name=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=27,font=("arial",13))
        entry_cust_name.grid(row=1,column=1)
        
        # mother's name
        lblmnames=Label(labelframeleft,font=("arial", 12, "bold"),text="Mother's Name: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lblmnames.grid(row=2, column=0,sticky=W)    

        txtmnames=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=27,font=("arial",13))
        txtmnames.grid(row=2,column=1)
        
        # Gender
        label_gender=Label(labelframeleft,font=("arial", 12, "bold"),text="Gender:",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        label_gender.grid(row=3, column=0,sticky=W)  

        Gender_combo=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial", 12),width=25,state="readonly")
        Gender_combo["value"]=("Male", "Female", "Other")  
        Gender_combo.current(0)
        Gender_combo.grid(row=3,column=1)
        
        # pincode

        lblPincode=Label(labelframeleft,font=("arial", 12, "bold"),text="Pincode: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lblPincode.grid(row=4, column=0,sticky=W)    

        txtPincode=ttk.Entry(labelframeleft,textvariable=self.var_pincode,width=27,font=("arial",13))
        txtPincode.grid(row=4,column=1)
        

        # Contact number

        lblContact=Label(labelframeleft,font=("arial", 12, "bold"),text="Contact number: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lblContact.grid(row=5, column=0,sticky=W)    

        txtContactNumber=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=27,font=("arial",13))
        txtContactNumber.grid(row=5,column=1)
        
        #email address
        
        lblEmail=Label(labelframeleft,font=("arial", 12, "bold"),text="Email: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)    
         

        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=27,font=("arial",13))
        txtEmail.grid(row=6,column=1)

        #Nationality

        lblNationality=Label(labelframeleft,font=("arial", 12, "bold"),text="Nationality: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lblNationality.grid(row=7, column=0,sticky=W) 


        nation_combo=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial", 12),width=25,state="readonly")
        nation_combo["value"]=("Indian", "French", "German", "Italian", "Mexican","Japanese", "Spanish","English", "Other")  
        nation_combo.current(0)
        nation_combo.grid(row=7,column=1)




        # Id proof type combobox

        lblIdProof=Label(labelframeleft,font=("arial", 12, "bold"),text="Id Proof Type: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lblIdProof.grid(row=8, column=0,sticky=W) 

        search_combo=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial", 12),width=25,state="readonly")
        search_combo["value"]=("Aadhar card", "Voter Id Card", "Driving license", "Passport", "Other")  
        search_combo.current(0)
        search_combo.grid(row=8,column=1)




        # id number
        lblIdNumber=Label(labelframeleft,font=("arial", 12, "bold"),text="Id Number: ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lblIdNumber.grid(row=9, column=0,sticky=W)    
         

        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=27,font=("arial",13))
        txtIdNumber.grid(row=9,column=1)

        # @ address
        lbladdress=Label(labelframeleft,font=("arial", 12, "bold"),text="Address ",bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbladdress.grid(row=10, column=0,sticky=W)    
         

        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=27,font=("arial",13))
        txtaddress.grid(row=10,column=1)


        # @ BUTTONS BELOW ALL OPTIONS

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=15,y=400,width=395,height=40)

        # 1st button

        btnAdd=Button(btn_frame, text="Add New",command=self.add_data, font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnAdd.grid(row=0,column=0)
        

        # @2nd button

        btnupdate=Button(btn_frame, text="Update",command=self.update,font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnupdate.grid(row=0,column=1)


        # @ 3rd button

        btndelete=Button(btn_frame, text="Delete",command=self.delete, font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btndelete.grid(row=0,column=2)

        # @ 4th button

        btnreset=Button(btn_frame, text="Reset",command=self.reset, font=("arial",12, "bold"),bg="Tan", fg="white",width=8,cursor="hand2")
        btnreset.grid(row=0,column=3)
        
        # @ table frame next to all details and search system

        tableframe=LabelFrame(self.root,text="View Details And Search System",font=("TT RICKS",12,"bold"),bg="Tan",fg="black",bd=2,relief=RIDGE,padx=2)
        tableframe.place(x=430,y=50,width=885,height=500)
       

        lblsearchby=Label(tableframe,font=("times new roman", 12, "bold"),text="Search By: ",bg="brown",fg="white",bd=2,relief=RIDGE,padx=2,pady=4)
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)   

        self.search_var=StringVar()
        search_combo=ttk.Combobox(tableframe,font=("arial", 12),textvariable=self.search_var,width=25,state="readonly")
        search_combo["value"]=("Contact No", "Reference No")  
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2)

        self.entry_search=StringVar()
        entry_search=ttk.Entry(tableframe,width=22,textvariable=self.entry_search,font=("arial",13))
        entry_search.grid(row=0,column=2,padx=2)
    

        btnsearch=Button(tableframe, text="Search",command=self.search, font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(tableframe, text="Show All",command=self.fetch_data, font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnshowall.grid(row=0,column=4,padx=1)
        
       
        # @ show data table

        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0, y=50,width=880,height=320)
         

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother's name","gender", "pincode", "contact number","email","nationality","id proof","id number","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)


        self.cust_Details_Table.heading("ref",text="Reference No ")
        self.cust_Details_Table.heading("name",text="Customer Name ")
        self.cust_Details_Table.heading("mother's name",text="Mother's Name ")
        self.cust_Details_Table.heading("gender",text="Gender")
        self.cust_Details_Table.heading("pincode",text="Pincode")
        self.cust_Details_Table.heading("contact number",text="Contact No")
        self.cust_Details_Table.heading("email",text="Email")
        self.cust_Details_Table.heading("nationality",text="Nationality")
        self.cust_Details_Table.heading("id proof",text="Id proof")
        self.cust_Details_Table.heading("id number",text="Id Number")
        self.cust_Details_Table.heading("address",text="Address")

        self.cust_Details_Table["show"]="headings"

        self.cust_Details_Table.column("ref",width=100)
        self.cust_Details_Table.column("name",width=110)
        self.cust_Details_Table.column("mother's name",width=110)
        self.cust_Details_Table.column("gender",width=100)
        self.cust_Details_Table.column("pincode",width=100)
        self.cust_Details_Table.column("contact number",width=100)
        self.cust_Details_Table.column("email",width=100)
        self.cust_Details_Table.column("nationality",width=100)
        self.cust_Details_Table.column("id proof",width=100)
        self.cust_Details_Table.column("id number",width=100)
        self.cust_Details_Table.column("address",width=100)


        self.cust_Details_Table.pack(fill=BOTH,expand=1)
        self.cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def add_data(self):
        if self.var_contact.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Invalid", "All fields are required",parent=self.root)
        else:
            try:

                connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
                my_cursor=connection.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_ref.get(),
                                                                                self.var_cust_name.get(),
                                                                                self.var_mother.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_pincode.get(),
                                                                                self.var_contact.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_idproof.get(),
                                                                                self.var_idnumber.get(),
                                                                                self.var_address.get()
                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Successful", "Customer has been Added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Something Went Wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())   
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
            connection.commit()
        connection.close()

    def get_cursor(self,event=""):
        cursor_row=self.cust_Details_Table.focus()
        content=self.cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_pincode.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_idnumber.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if not self.var_contact.get():
            messagebox.showerror("Error", "Please Enter Contact Details", parent=self.root)

        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            my_cursor.execute("update customer set Customername=%s, MotherName=%s,Gender=%s,Pincode=%s,ContactNumber=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where ReferenceNo=%s",(

                                                                                                                                                                                                  self.var_cust_name.get(),
                                                                                                                                                                                                  self.var_mother.get(),
                                                                                                                                                                                                  self.var_gender.get(),
                                                                                                                                                                                                  self.var_pincode.get(),
                                                                                                                                                                                                  self.var_contact.get(),
                                                                                                                                                                                                  self.var_email.get(),
                                                                                                                                                                                                  self.var_nationality.get(),
                                                                                                                                                                                                  self.var_idproof.get(),
                                                                                                                                                                                                  self.var_idnumber.get(),
                                                                                                                                                                                                  self.var_address.get(),
                                                                                                                                                                                                  self.var_ref.get()

                                                                                                                                                                                              ))   
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Updated","Customer Details Sucessfully Updated",parent=self.root)  


            
    def delete(self):
        delete=messagebox.askyesno("Luxury Hotel", " Do you want to Delete this Customer",parent=self.root)
        if delete>0:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            query="delete from customer where ReferenceNo=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return

        connection.commit()
        self.fetch_data()
        connection.close()    

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_pincode.set(""),
        self.var_contact.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_idproof.set(""),
        self.var_idnumber.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


        # Search button 

    def search(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from customer where " + str(self.search_var.get())+" LIKE '% " + str(self.entry_search.get())+ "%'")

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("", END, values=i)

            connection.commit()
        connection.close()
    

    
    
          








    

                                                                                                                                                                                                       


                                                                                                                                                                                                                                                                                                                                   


if __name__=="__main__":
    root=Tk()
    obj=customer_window(root)
    root.mainloop()
