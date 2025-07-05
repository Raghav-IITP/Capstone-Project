from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk #pip install pillow 
from tkinter import messagebox
import mysql.connector
from Customer_window import customer_window #import from file that we made for customer button
from Rooms_window import Rooms_window #import from file that we made for Room button
from Details import Details


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()



class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"D:\HMS project files\images\HOTEL ENTRANCE.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

    # Frame of login system
        frame=Frame(self.root,bg="Tan")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"D:\HMS project files\images\295128.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="Tan",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_started=Label(frame,text="WELCOME", font=("Open Sans",20,"bold"),fg="white",bg="Tan")
        get_started.place(x=95,y=100)

        #labels
        username_lbl=Label(frame,text="Username:",font=("Open Sans",15,"bold"),fg="white",bg="Tan")
        username_lbl.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("Open Sans",12))
        self.txtuser.place(x=30,y=185,width=270)

        password_lbl=Label(frame,text="Password:",font=("Open Sans",15,"bold"),fg="white",bg="Tan")
        password_lbl.place(x=70,y=220)
        
        self.txtpass=ttk.Entry(frame,font=("Open Sans",12))
        self.txtpass.place(x=30,y=250,width=270)


        # Icon

        img2=Image.open(r"D:\HMS project files\images\1077114.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="Tan",borderwidth=0)
        lblimg2.place(x=650,y=325,width=25,height=25)

        img3=Image.open(r"D:\HMS project files\images\images (2).png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="Tan",borderwidth=0)
        lblimg3.place(x=650,y=390,width=25,height=25)

        # Buttons 
        #login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("Open Sans",15,"bold"),bd=3,relief=RIDGE,fg="White",bg="Tan",activeforeground="white",activebackground="Tan",cursor="hand2")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # new user button

        registerbtn=Button(frame,text="Register New User ",command=self.register_window,font=("Open Sans",12,"bold"),borderwidth=0,fg="White",bg="Tan",activeforeground="white",activebackground="Tan",cursor="hand2")
        registerbtn.place(x=5,y=375,width=160,height=35)

        # forgot password button
        forgotbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("Open Sans",12,"bold"),borderwidth=0,fg="White",bg="Tan",activeforeground="white",activebackground="Tan",cursor="hand2")
        forgotbtn.place(x=5,y=410,width=150,height=35)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get()=="Aastha@luxuryhotel" and self.txtpass.get()=="aashu":
            messagebox.showinfo("Success","Welcome to Luxury Hotel")
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(

                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("Yes/No", "Only Accessible to Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            connection.commit()
            connection.close()

            # reset password
    def reset_password(self):
        if self.combosecuirity.get()=="Select":
            messagebox.showerror("Error", "Select the Security Question",parent=self.root2)
        elif self.txt_secuirityanswer.get()=="":
            messagebox.showerror("Error","Please Enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error", " Please enter the new Password",parent=self.root2)
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combosecuirity.get(),self.txt_secuirityanswer.get(),)
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error"," Please Enter Correct Answer",parent=self.root2)

            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                connection.commit()
                connection.close()
                messagebox.showinfo("Info"," Password reset successful",parent=self.root2)
                self.root2.destroy()



#forgot passqword window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Mysql@3115",database="sys")
            my_cursor=connection.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error", " Please Enter the Valid user Name")
            else:
                connection.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")            
                
                l=Label(self.root2,text="Forget Password", font=("times new roman",15),fg="Yellow",bg="Tan")
                l.place(x=0, y=10, relwidth=1)

                secuirityques=Label(self.root2,text="Security Question",font=("times new roman",18,"bold"),bg="white")
                secuirityques.place(x=40,y=80)

                self.combosecuirity=ttk.Combobox(self.root2,font=("times new roman",15),state="readonly")
                self.combosecuirity["values"]=("select", "Your Birth place", "Your Secondary School", "Your Pet Name")
                self.combosecuirity.place(x=40,y=110,width=240)
                self.combosecuirity.current(0)


                Secuirityanswer=Label(self.root2,text="Security Answer",font=("times new roman",18,"bold"),bg="white")
                Secuirityanswer.place(x=40,y=150)

                self.txt_secuirityanswer=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_secuirityanswer.place(x=40,y=180,width=240)


                newpass=Label(self.root2,text="New Password",font=("times new roman",18,"bold"),bg="white")
                newpass.place(x=40,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=40,y=250,width=240)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15),fg="white", bg="Tan", cursor="hand2")
                btn.place(x=140,y=290)





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

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20, "bold"),fg="Yellow", bg="Tan")
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
        b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
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

    #Login button

    def return_login(self):
        self.root.destroy()

        

        

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        
        # @ 1st Image 
        
        img1=Image.open(r"D:\HMS project files\images\pexels-pixabay-260922.jpg")
        img1=img1.resize((1550,150),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg= Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=150)

        # @ LOGO
        img2=Image.open(r"D:\HMS project files\images\LOGO.png")
        img2=img2.resize((220,150),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg= Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=220,height=140)

        # @title

        lbl_title=Label(self.root,text="LUXURY HOTEL", font=("Futura",40,"bold"),bg="black",fg="Beige",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=150,width=1550,height=50)

        # @MAIN FRAME
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=200,width=1550,height=620)

        #@Menu

        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="Tan", fg="white",bd=4,relief=RIDGE)
        lbl_menu.place(x=5,y=5,width=190) 

        # @ options
        options_frame=Frame(main_frame,bd=4,relief=RIDGE)
        options_frame.place(x=5,y=40,width=190,height=192)

        cutm_button=Button(options_frame,text="CUSTOMER",command=self.customer_details,width=17,font=("times new roman",15,"bold"),bg="Tan",fg="white",bd=0,cursor="hand2")
        cutm_button.grid(row=0,column=0,pady=1)
        
        Room_button=Button(options_frame,text="ROOMS",command=self.Rooms_window,width=17,font=("times new roman",15,"bold"),bg="Tan",fg="white",bd=0,cursor="hand2")
        Room_button.grid(row=1,column=0,pady=1)
        
        Details_button=Button(options_frame,text="DETAILS",command=self.Details,width=17,font=("times new roman",15,"bold"),bg="Tan",fg="white",bd=0,cursor="hand2")
        Details_button.grid(row=2,column=0,pady=1)
        
        Dashboard_button=Button(options_frame,text="DASHBOARD",width=17,font=("times new roman",15,"bold"),bg="Tan",fg="white",bd=0,cursor="hand2")
        Dashboard_button.grid(row=3,column=0,pady=1)

        signout_button=Button(options_frame,text="SIGN OUT",command=self.signout,width=17,font=("times new roman",15,"bold"),bg="Tan",fg="white",bd=0,cursor="hand2")
        signout_button.grid(row=4,column=0,pady=1)
        
        # @image next to all options
        img3=Image.open(r"D:\HMS project files\images\pexels-osho-1001965.jpg")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3= Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg3.place(x=200,y=0,width=1317,height=580)
         
        # images below options section
        img4=Image.open(r"D:\HMS project files\images\downimage1.jpg")
        img4=img4.resize((200,190),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4= Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=233,width=200,height=190)
        
        img5=Image.open(r"D:\HMS project files\images\downimage2.jpg")
        img5=img5.resize((200,175),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5= Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=400,width=200,height=175)


    def customer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=customer_window(self.new_window)

    def Rooms_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Rooms_window(self.new_window)  

    def Details(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)

    def signout(self):
        self.root.destroy()


    
        



if __name__=="__main__":
    main()