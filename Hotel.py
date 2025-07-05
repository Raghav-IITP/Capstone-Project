from tkinter import*
from PIL import Image, ImageTk #Install PIL from pip install pillow
from Customer_window import customer_window #import from file that we made for customer button
from Rooms_window import Rooms_window #import from file that we made for Room button
from Details import Details
from dashboard_window import DashboardApp

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

        lbl_title=Label(self.root,text="WELCOME TO LUXURY HOTEL", font=("TIMES NEW ROMAN",40,"bold"),bg="black",fg="Beige",bd=4,relief=RIDGE)
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
        
        Dashboard_button=Button(options_frame,command=self.open_dashboard,text="DASHBOARD",width=17,font=("times new roman",15,"bold"),bg="Tan",fg="white",bd=0,cursor="hand2")
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

    def open_dashboard(self):
        self.new_window=Toplevel(self.root)
        self.app= DashboardApp(self.new_window)

    def signout(self):
        self.root.destroy()













if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

