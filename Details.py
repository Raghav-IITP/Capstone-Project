from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1319x580+200+230")


# @title

        lbl_title=Label(self.root,text="DETAILS", font=("TT RICKS",18,"bold"),bg="black",fg="pink",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1319,height=50)
 
        #@ logo on ROOM BOOKING 

        img1=Image.open(r"D:\HMS project files\images\LOGO.png")
        img1=img1.resize((95,48),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg= Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=95,height=48)

        # @ Label framing

        labelframeleft=LabelFrame(self.root,text="Add New Room",font=("TT RICKS",12,"bold"),bg="Tan", fg="white",bd=2,relief=RIDGE,padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=300)

        labelframe=LabelFrame(self.root,padx=2)
        labelframe.place(x=5,y=360,width=1310,height=188)

        # Images below details section

        img2=Image.open(r"D:\HMS project files\images\pexels-kamenczak-775219.jpg")
        img2=img2.resize((1310,188),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg= Label(self.root,image=self.photoimg2,bd=2,relief=RIDGE)
        lblimg.place(x=5,y=360,width=1310,height=188)
        

        # Floor no
    
        lbl_floor=Label(labelframeleft,text="Floor : ", font=("arial", 12, "bold"),bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_floor.grid(row=0, column=1,sticky=W)    
        
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=19,font=("arial",13))
        entry_floor.grid(row=0,column=2,sticky=W)

        # Room Number
    
        lbl_roomno=Label(labelframeleft,text="Room No : ", font=("arial", 12, "bold"),bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_roomno.grid(row=1, column=1,sticky=W)    

        self.var_roomno=StringVar()
        entry_roomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=19,font=("arial",13))
        entry_roomno.grid(row=1,column=2,sticky=W)

        # Room Type
    
        lbl_roomtype=Label(labelframeleft,text="Room Type : ", font=("arial", 12, "bold"),bg="Tan",fg="white",bd=2,relief=RIDGE,padx=2,pady=6)
        lbl_roomtype.grid(row=2, column=1,sticky=W)    

        self.var_roomtype=StringVar()
        entry_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=19,font=("arial",13))
        entry_roomtype.grid(row=2,column=2,sticky=W)


         # @ BUTTONS BELOW ALL OPTIONS

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=135,width=105,height=135)

        # 1st button

        btnAdd=Button(btn_frame, text="Add New",command=self.add_data,font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnAdd.grid(row=0,column=0)
        

        # @2nd button

        btnupdate=Button(btn_frame, text="Update",command=self.update,font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnupdate.grid(row=1,column=0)


        # @ 3rd button

        btndelete=Button(btn_frame, text="Delete",command=self.delete, font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btndelete.grid(row=2,column=0)

        # @ 4th button

        btnreset=Button(btn_frame,command=self.reset, text="Reset",font=("arial",12, "bold"),bg="Tan", fg="white",width=9,cursor="hand2")
        btnreset.grid(row=3,column=0)


        # Table Frame search System

        tableframe=LabelFrame(self.root,text="Show Room Details",font=("TT RICKS",12,"bold"),bd=2,relief=RIDGE,padx=2)
        tableframe.place(x=550,y=55,width=760,height=298)

        # Scroll bar
        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.room_table=ttk.Treeview(tableframe,column=("floor", "roomno", "roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room Number")
        self.room_table.heading("roomtype",text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=70)
        self.room_table.column("roomno",width=70)
        self.room_table.column("roomtype",width=130)
        
        

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()




        # Add Data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Invalid", "All fields are required",parent=self.root)
        else:
            try:

                connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
                my_cursor=connection.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                self.var_floor.get(),                                                                              
                                                                                self.var_roomno.get(),
                                                                                self.var_roomtype.get()
                                                                                
                                                                                
                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Successful","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Something Went Wrong:{str(es)}",parent=self.root)


    # fetch data
    def fetch_data(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),                                                                              
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])
        
    # Update button

    def update(self):
        if not self.var_floor.get():
            messagebox.showerror("Error", "Please Enter Details", parent=self.root)

        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            my_cursor.execute("update details set Floor=%s, RoomType=%s where RoomNo=%s",(

                                                                                                                                                    self.var_floor.get(),
                                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                                    self.var_roomno.get()
                                                                                                                                                                                                                               

                                                                                                                                                                                                  

                                                                                                                                                    ))   
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Updated","New Room Details Sucessfully Updated",parent=self.root)

    #DElete button
    def delete(self):
        delete=messagebox.askyesno("Luxury Hotel", " Do you want to Delete this Room Details",parent=self.root)
        if delete>0:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return

        connection.commit()
        self.fetch_data()
        connection.close()
        messagebox.showinfo("Deleted","Details Succesfully Deleted",parent=self.root)
    
    # Reset Button
    def reset(self):
        self.var_floor.set(""),                                                                              
        self.var_roomno.set(""),
        self.var_roomtype.set("")
        




if __name__=="__main__":
    root=Tk()
    obj=Details(root)
    root.mainloop()