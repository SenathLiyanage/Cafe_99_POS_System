from tkinter import *
# import 'messagebox' to show messages
from tkinter import messagebox
from PIL import ImageTk
# type 'pip install pymysql' in terminal
# import pymysql to connect python with the MySQL database
import pymysql


# functionality part

def clear():
    # delete all the entry fields
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    c_passwordEntry.delete(0,END)
    # uncheck the checkbox by setting value to 0
    check.set(0)


def connect_db():
    # check fields are empty or not
    if emailEntry.get()==('Email' and '') or usernameEntry.get()==('User Name' and '') or passwordEntry.get()==('Password' and '') or c_passwordEntry.get()==('Confirm Password' and ''):
        messagebox.showerror('Error','Please fill all fields to Sign Up')
    elif passwordEntry.get() != c_passwordEntry.get():
        messagebox.showerror('Error','Passwords are not matching')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept the Terms & Conditions')
    else:
        # connect with the database
        try:
            # 'con' variable will help when the commitments are done (delete, update, add)
            con=pymysql.connect(host='localhost',user='root',password='ss467')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connection issue. Please try again')
            return

        try:
        # if databases are not created execute following
            # create the database
            query = 'create database userdata'
            mycursor.execute(query)
            # use the database
            query = 'use userdata'
            mycursor.execute(query)
            # create table. Table name => data
            query = 'create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            # execute query
            mycursor.execute(query)
        except:
        # if databases are already created execute following
            mycursor.execute('use userdata')

        # check the username is existing or not. '%s' will mention saved username value
        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))

        # if there is any row match with the entered username display error msg
        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','User name is already exist!')
        else:
            # insert/save data inside the table
            # '%s' will represent the values enter to the entry fields
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            # commit the changes
            con.commit()
            # disconnect the connection
            con.close()
            # show the successful message box
            messagebox.showinfo('Seccess','Registration is Successful')
            # delete all the text in the entry field
            clear()
            # close the signup page
            signup_window.destroy()
            # open the login page
            import main

def email_enter(event):
    # if the text area has text name called 'Email' when click curser every thing will delete
    if emailEntry.get()=='Email':
        emailEntry.delete(0,END)

def email_not_enter(event):
    # if the text area is null when click another Entry the area fill with text 'Email'
    if emailEntry.get()=='':
        emailEntry.insert(0,'Email')

def un_enter(event):
    # if the text area has text name called 'User Name' when click curser every thing will delete
    if usernameEntry.get()=='User Name':
        usernameEntry.delete(0,END)

def un_not_enter(event):
    # if the text area is null when click another Entry the area fill with text 'User Name'
    if usernameEntry.get()=='':
        usernameEntry.insert(0,'User Name')

def pw_enter(event):
    # if the text area has text name called 'Password' when click curser every thing will delete
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def pw_not_enter(event):
    # if the text area is null when click another Entry the area fill with text 'Password'
    if passwordEntry.get()=='':
        passwordEntry.insert(0,'Password')

def c_pw_enter(event):
    # if the text area has text name called 'Password' when click curser every thing will delete
    if c_passwordEntry.get()=='Confirm Password':
        c_passwordEntry.delete(0,END)

def c_pw_not_enter(event):
    # if the text area is null when click another Entry the area fill with text 'Password'
    if c_passwordEntry.get()=='':
        c_passwordEntry.insert(0,'Confirm Password')

def direct_login():
    # first close sign up window
    signup_window.destroy()
    # open login window
    import main


# GUI Part

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(0,0)

# ImageTk class use for jpg files
background = ImageTk.PhotoImage(file='MainBG.jpg')
signup_window.geometry('1100x700+200+50')
bgLabel = Label(signup_window, image=background)
bgLabel.place(x=0,y=0)

# background color
Headbg = "#1E1E1E"
# font color
Headfg = "#2C2723"

heading=Label(signup_window,text='CREATE ACCOUNT',font=('Gilroy',30,'bold'),bg=Headbg, fg='snow')
heading.place(x=115,y=90)

# email entry
emailEntry = Entry(signup_window, width=25, font=('Gilroy',17,'bold'), bd=0, fg='snow', bg=Headbg)
emailEntry.place(x=130,y=180)
# add pre-instructions
emailEntry.insert(0,'Email')
# usernameEntry bind to 'on_enter' function using bind() method
emailEntry.bind('<FocusIn>',email_enter)
emailEntry.bind('<FocusOut>',email_not_enter)
# crete a frame to the user name entry
Frame(signup_window,width=350,height=2,bg='snow').place(x=125,y=215)

# user name entry
usernameEntry = Entry(signup_window, width=25, font=('Gilroy',17,'bold'), bd=0, fg='snow', bg=Headbg)
usernameEntry.place(x=130,y=255)
# add pre-instructions
usernameEntry.insert(0,'User Name')
# usernameEntry bind to 'on_enter' function using bind() method
usernameEntry.bind('<FocusIn>',un_enter)
usernameEntry.bind('<FocusOut>',un_not_enter)
# crete a frame to the user name entry
Frame(signup_window,width=350,height=2,bg='snow').place(x=125,y=285)

# password entry
passwordEntry = Entry(signup_window, width=25, font=('Gilroy',17,'bold'), bd=0, fg='snow', bg=Headbg)
passwordEntry.place(x=130,y=330)
# add pre-instructions
passwordEntry.insert(0,'Password')
# usernameEntry bind to 'on_enter' function using bind() method
passwordEntry.bind('<FocusIn>',pw_enter)
passwordEntry.bind('<FocusOut>',pw_not_enter)
# crete a frame to the password entry
Frame(signup_window,width=350,height=2,bg='snow').place(x=125,y=365)

# c_password entry
c_passwordEntry = Entry(signup_window, width=25, font=('Gilroy',17,'bold'), bd=0, fg='snow', bg=Headbg)
c_passwordEntry.place(x=130,y=405)
# add pre-instructions
c_passwordEntry.insert(0,'Confirm Password')
# usernameEntry bind to 'on_enter' function using bind() method
c_passwordEntry.bind('<FocusIn>',c_pw_enter)
c_passwordEntry.bind('<FocusOut>',c_pw_not_enter)
# crete a frame to the password entry
Frame(signup_window,width=350,height=2,bg='snow').place(x=125,y=435)

# when the box is checked, 'check' variable will get '1' otherwise get '0'
check=IntVar()
# 'checkbutton()' class will create a check button
t_c_checkButton = Checkbutton(signup_window, text="I agree to the Terms & Conditions", font=('Gilroy',10,'bold'),fg='snow', bg=Headbg, activebackground=Headbg, activeforeground='NavajoWhite4', cursor='hand2', variable=check)
# terms & conditions label
#t_c_Label=Label(signup_window, text="I agree to the Terms & Conditions", font=('Gilroy',8,'bold'), fg=Headfg, bg=Headbg)
t_c_checkButton.place(x=130,y=460)

# signup button
# when clicking signup button the data should store inside the database
signupButton = Button(signup_window,text='Sign Up',font=('Gilroy',16,'bold'), bd=0, width=18, bg='snow', fg=Headbg, activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2', command=connect_db)
signupButton.place(x=180,y=520)

# have account label
have_account_Label=Label(signup_window, text="Already have an account?", font=('Gilroy',10,'bold'), fg='snow', bg=Headbg)
have_account_Label.place(x=185,y=600)
have_account_Button = Button(signup_window,text='Log In', font=('Gilroy',10,'bold'), bd=0, bg=Headbg, fg='red', activebackground=Headbg, activeforeground='NavajoWhite4', cursor='hand2', command=direct_login)
have_account_Button.place(x=360,y=600)

signup_window.mainloop()