from tkinter import *
# import 'messagebox' to show messages
from tkinter import messagebox
# if the image is not in png formate need to install an external module to add jpg image
# go to terminal and type 'pip install pillow' install
# after installed import the module. PIL = Python Image Library
from PIL import ImageTk
# import pymysql to connect python with the MySQL database
import pymysql

# functionality part

def clear():
    # delete all the entry fields
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)

def login_db():
    # check fields are empty or not
    if usernameEntry.get() == '' or usernameEntry.get() == 'User Name' or passwordEntry.get() == '' or passwordEntry.get() == 'Password':
        messagebox.showerror('Error', 'Please fill all fields to Sign Up')
    else:
        # connect with the database
        try:
            # 'con' variable will help when the commitments are done (delete, update, add)
            con=pymysql.connect(host='localhost',user='root',password='ss467')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connection issue. Please try again')
            return

        # use the database. Database is already created in signup page
        query = 'use userdata'
        mycursor.execute(query)

        # check the username is existing or not. '%s' will mention saved username value
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(),passwordEntry.get()))

        # if there is no any row match with the entered username and pw display error msg
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid User Name or Password!')
        else:
            # if there is matching username and password show message box
            messagebox.showinfo('Welcome', 'Login is Successful')
            # delete all the text in the entry field
            clear()
            # close the signup page
            #login_window.destroy()
            # open the login page
            # import signup


def forget_pass():
    # creating a window
    window = Toplevel()
    window.title('Reset Password')

    bgImg = ImageTk.PhotoImage(file='BGimage.jpg')
    bgLabel = Label(window,image=bgImg)
    bgLabel.grid()

    Headbg = "#D3CAB3"
    Headfg = "#2C2723"

    heading_Label = Label(window, text='RESET PASSWORD', font=('Gilroy', 20, 'bold'), bg=Headbg, fg=Headfg)
    heading_Label.place(x=200, y=130)

    # user name entry
    usernameEntry = Entry(window, width=28, font=('Gilroy', 11, 'bold'), bd=0, fg=Headfg, bg=Headbg)
    usernameEntry.place(x=210, y=205)
    # add pre-instructions
    usernameEntry.insert(0, 'User Name')
    # usernameEntry bind to 'on_enter' function using bind() method
    usernameEntry.bind('<FocusIn>', un_enter)
    usernameEntry.bind('<FocusOut>', un_not_enter)
    # crete a frame to the user name entry
    Frame(login_window, width=258, height=2, bg=Headfg).place(x=210, y=227)

    # password entry
    passwordEntry = Entry(window, width=28, font=('Gilroy', 11, 'bold'), bd=0, fg=Headfg, bg=Headbg)
    passwordEntry.place(x=210, y=265)
    # add pre-instructions
    passwordEntry.insert(0, 'Password')
    # passwordEntry bind to 'pw_enter' function using bind() method
    passwordEntry.bind('<FocusIn>', pw_enter)
    # passwordEntry bind to 'pw_not_enter' function using bind() method
    passwordEntry.bind('<FocusOut>', pw_not_enter)
    # crete a frame to the user name entry
    Frame(login_window, width=258, height=2, bg=Headfg).place(x=210, y=287)


    window.mainloop()


def show():
    # 'config()' method use to change the icon into 'icon eye.png' when click
    closeeye.config(file='icon eye.png')
    # show the password by clicking
    passwordEntry.config(show='')
    # when clicking the button again hide the characters
    eyeButton.config(command=hide)

def hide():
    # 'config()' method use to change the icon into 'eye slash.png' when click
    closeeye.config(file='eye slash.png')
    # hide the password using '*' by clicking
    passwordEntry.config(show='*')
    # when clicking the button again show the characters
    eyeButton.config(command=show)

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
        # type the password in * mark
        passwordEntry.config(show='*')

def pw_not_enter(event):
    # if the text area is null when click another Entry the area fill with text 'Password'
    if passwordEntry.get()=='':
        passwordEntry.insert(0,'Password')

def direct_signup():
    # first close login window
    login_window.destroy()
    # open sign up window
    import signup


# GUI part

login_window = Tk()
# if use place(width*height + space from X + space from Y) method must mention the geometrics
login_window.geometry('992x613+250+100')
# Stop maximize the window
login_window.resizable(0,0)
# set title
login_window.title('Login Page')
# import the image. Image will represent by bgImage
bgImage=ImageTk.PhotoImage(file='BGimage.jpg')
bgLabel = Label(login_window, image=bgImage)
# to place image we can use following methods
# bgLabel.pack()
# bgLabel.grid(row=0,column=0)
bgLabel.place(x=0,y=0)

# Login Labels Part

# Heading

# call a string variable to use hex color codes
Headbg = "#D3CAB3"
Headfg = "#2C2723"

heading=Label(login_window,text='USER LOGIN',font=('Gilroy',20,'bold'),bg=Headbg, fg=Headfg)
# use 'place()' method if you want to place label on a particular position
heading.place(x=245,y=130)

# user name entry
usernameEntry = Entry(login_window, width=28, font=('Gilroy',11,'bold'), bd=0, fg=Headfg, bg=Headbg)
usernameEntry.place(x=210,y=205)
# add pre-instructions
usernameEntry.insert(0,'User Name')
# usernameEntry bind to 'on_enter' function using bind() method
usernameEntry.bind('<FocusIn>',un_enter)
usernameEntry.bind('<FocusOut>',un_not_enter)
# crete a frame to the user name entry
Frame(login_window,width=258,height=2,bg=Headfg).place(x=210,y=227)

# password entry
passwordEntry = Entry(login_window, width=28, font=('Gilroy',11,'bold'), bd=0, fg=Headfg, bg=Headbg)
passwordEntry.place(x=210,y=265)
# add pre-instructions
passwordEntry.insert(0,'Password')
# passwordEntry bind to 'pw_enter' function using bind() method
passwordEntry.bind('<FocusIn>',pw_enter)
# passwordEntry bind to 'pw_not_enter' function using bind() method
passwordEntry.bind('<FocusOut>',pw_not_enter)
# crete a frame to the user name entry
Frame(login_window,width=258,height=2,bg=Headfg).place(x=210,y=287)
# eye button
closeeye = PhotoImage(file='eye slash.png')
eyeButton = Button(login_window,image=closeeye, bd=0, bg=Headbg, activebackground=Headbg, cursor='hand2', command=show)
eyeButton.place(x=445,y=260)

# forget button
forgetButton = Button(login_window,text='forgot Password?', bd=0, bg=Headbg, fg=Headfg, activebackground=Headbg, activeforeground='NavajoWhite4', cursor='hand2', command=forget_pass)
forgetButton.place(x=370,y=300)

# login button
loginButton = Button(login_window,text='Login',font=('Gilroy',16,'bold'), bd=0, width=18, bg=Headfg, fg=Headbg, activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2', command=login_db)
loginButton.place(x=220,y=340)

# OR label
orLabel=Label(login_window, text='- OR -', font=('Gilroy',8,'bold'), fg=Headfg, bg=Headbg)
orLabel.place(x=320,y=395)

# logos
fbLogo = PhotoImage(file='facebook.png')
fbButton = Button(login_window,image=fbLogo,font=('Gilroy',16,'bold'), bd=0, bg=Headbg, fg=Headfg, activebackground=Headbg, activeforeground=Headbg, cursor='hand2')
fbButton.place(x=260,y=430)

googleLogo = PhotoImage(file='google.png')
googleButton = Button(login_window,image=googleLogo,font=('Gilroy',16,'bold'), bd=0, bg=Headbg, fg=Headfg, activebackground=Headbg, activeforeground=Headbg, cursor='hand2')
googleButton.place(x=320,y=430)

twitterLogo = PhotoImage(file='twitter.png')
twitterButton = Button(login_window,image=twitterLogo,font=('Gilroy',16,'bold'), bd=0, bg=Headbg, fg=Headfg, activebackground=Headbg, activeforeground=Headbg, cursor='hand2')
twitterButton.place(x=380,y=430)

# create account label
createLabel=Label(login_window, text="Don't have an account?", font=('Gilroy',8,'bold'), fg=Headfg, bg=Headbg)
createLabel.place(x=215,y=485)
createButton = Button(login_window,text='Create new account', font=('Gilroy',8,'bold'), bd=0, bg=Headbg, fg='red', activebackground=Headbg, activeforeground='NavajoWhite4', cursor='hand2', command=direct_signup)
createButton.place(x=345,y=485)


login_window.mainloop()