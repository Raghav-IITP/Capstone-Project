from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk #pip install pillow 
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confirmpass=StringVar()


        # bg image
        self.bg=ImageTk.PhotoImage(file=r"D:\HMS project files\images\pexels-donaldtong94-189296.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # left image
        self.bg1=ImageTk.PhotoImage(file=r"D:\HMS project files\images\istockphoto-472899538-612x612.jpg")
        bg1_lbl=Label(self.root,image=self.bg1)
        bg1_lbl.place(x=50,y=120,width=470,height=400)

        #main framing

        frame=Frame(self.root,bg="White")
        frame.place(x=520,y=120,width=800,height=400)
        # label register

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20, "bold"),fg="Yellow", bg="Sky blue")
        register_lbl.place(x=20,y=10)

        # labels and entries
        fname=Label(frame,text="First Name", font=("times new roman",18,"bold"),bg="white")
        fname.place(x=40,y=50)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=40,y=80,width=240)

        l_name=Label(frame,text="Last Name", font=("times new roman",18,"bold"),bg="white")
        l_name.place(x=370,y=50)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=80,width=240)

        #row 2
        contact=Label(frame,text="Contact No",font=("times new roman",18,"bold"),bg="white")
        contact.place(x=40,y=110)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=40,y=140,width=240)

        email=Label(frame,text="Email",font=("times new roman",18,"bold"),bg="white")
        email.place(x=370,y=110)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=140,width=240)

        secuirityques=Label(frame,text="Security Question",font=("times new roman",18,"bold"),bg="white")
        secuirityques.place(x=40,y=170)

        self.combosecuirity=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="readonly")
        self.combosecuirity["values"]=("select", "Your Birth place", "Your Secondary School", "Your Pet Name")
        self.combosecuirity.place(x=40,y=200,width=240)
        self.combosecuirity.current(0)


        Secuirityanswer=Label(frame,text="Security Answer",font=("times new roman",18,"bold"),bg="white")
        Secuirityanswer.place(x=370,y=170)

        self.txt_secuirityanswer=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_secuirityanswer.place(x=370,y=200,width=240)

        # row 4

        password=Label(frame,text="Password",font=("times new roman",18,"bold"),bg="white")
        password.place(x=40,y=230)
        
        self.txt_password=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_password.place(x=40,y=260,width=240)

        confirmpassword=Label(frame,text="Confirm Password",font=("times new roman",18,"bold"),bg="white")
        confirmpassword.place(x=370,y=230)
        
        self.txt_cpassword=ttk.Entry(frame,textvariable=self.var_confirmpass,font=("times new roman",15))
        self.txt_cpassword.place(x=370,y=260,width=240)

        #checkbutton
        self.var_checkbutton=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_checkbutton,text="I Agree with The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=40,y=310)

        # buttons
        
        
        img=Image.open(r"D:\HMS project files\images\224-2244451_fall-always-forever-now-png-download-red-transparent.png")
        img=img.resize((170,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=40,y=350,width=170)

        img1=Image.open(r"D:\HMS project files\images\login-button-png-1.png")
        img1=img1.resize((200,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b2.place(x=400,y=300,width=200)

        # function declaration

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All Fields are required!")
        elif self.var_pass.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error", " Password and Confirm Password must be same")
        elif self.var_checkbutton.get()==0:
            messagebox.showerror("Error"," Please agree to our terms and condition")
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                                        ))
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "User Registered Successfully")
        







if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()


