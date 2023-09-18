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
            # close the login page
            login_window.destroy()
            # open the Dash_board page
            import Dash_board

# admin conformation
def forget_pass():
    def admin_con():
        if usernameEntry.get() == '' or usernameEntry.get() == 'User Name' or passwordEntry.get() == '' or passwordEntry.get() == 'Password':
            messagebox.showerror('Error', 'Admin data are required',parent=window)
        else:
            # connect with the database
            try:
                # 'con' variable will help when the commitments are done (delete, update, add)
                con = pymysql.connect(host='localhost', user='root', password='ss467')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error', 'Database connection issue. Please try again')
                return

            # use the database. Database is already created in signup page
            query = 'use userdata'
            mycursor.execute(query)

            # check the username is existing or not. '%s' will mention saved username value
            query = 'select * from admin where username=%s and password=%s'
            mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))

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
                window.destroy()
                login_window.destroy()
                # open the Password Reset page
                import Reset_pw

    def un_enter(event):
        # if the text area has text name called 'User Name' when click curser every thing will delete
        if usernameEntry.get() == 'User Name':
            usernameEntry.delete(0, END)

    def un_not_enter(event):
        # if the text area is null when click another Entry the area fill with text 'User Name'
        if usernameEntry.get() == '':
            usernameEntry.insert(0, 'User Name')

    def pw_enter(event):
        # if the text area has text name called 'Password' when click curser every thing will delete
        if passwordEntry.get() == 'Password':
            passwordEntry.delete(0, END)
            # type the password in * mark
            passwordEntry.config(show='*')

    def pw_not_enter(event):
        # if the text area is null when click another Entry the area fill with text 'Password'
        if passwordEntry.get() == '':
            passwordEntry.insert(0, 'Password')

    # GUI part
    # creating a window
    window = Toplevel()
    # if use place(width*height + space from X + space from Y) method must mention the geometrics
    window.geometry('323x329+575+250')
    # Stop maximize the window
    login_window.resizable(0, 0)
    # set window title
    window.title('Reset Password')

    bgImg = ImageTk.PhotoImage(file='con_bg.jpg')
    bgLabel = Label(window,image=bgImg)
    bgLabel.grid()

    heading_Label = Label(window, text='ADMIN CONFORMATION', font=('Gilroy', 18, 'bold'), bg='gray8', fg='snow')
    heading_Label.place(x=20, y=50)

    # user name entry
    usernameEntry = Entry(window, width=25, font=('Gilroy', 11, 'bold'), bd=0, bg='gray8', fg='snow')
    usernameEntry.place(x=60, y=130)
    # add pre-instructions
    usernameEntry.insert(0, 'User Name')
    # usernameEntry bind to 'on_enter' function using bind() method
    usernameEntry.bind('<FocusIn>', un_enter)
    usernameEntry.bind('<FocusOut>', un_not_enter)

    # password entry
    passwordEntry = Entry(window, width=25, font=('Gilroy', 11, 'bold'), bd=0, fg='snow', bg='gray8')
    passwordEntry.place(x=60, y=180)
    # add pre-instructions
    passwordEntry.insert(0, 'Password')
    # passwordEntry bind to 'pw_enter' function using bind() method
    passwordEntry.bind('<FocusIn>', pw_enter)
    # passwordEntry bind to 'pw_not_enter' function using bind() method
    passwordEntry.bind('<FocusOut>', pw_not_enter)

    # confirm button
    confirmButton = Button(window, text='Confirm', font=('Gilroy', 16, 'bold'), bd=0, width=15, bg=Headfg, fg='snow',
                         activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2', command=admin_con)
    confirmButton.place(x=60, y=250)


    window.mainloop()


def show():
    # 'config()' method use to change the icon into 'openeye.png' when click
    closeeye.config(file='openeye.png')
    # show the password by clicking
    passwordEntry.config(show='')
    # when clicking the button again hide the characters
    eyeButton.config(command=hide)

def hide():
    # 'config()' method use to change the icon into 'eye slash.png' when click
    closeeye.config(file='close_eye.png')
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
login_window.geometry('1100x700+200+50')
# Stop maximize the window
login_window.resizable(0,0)
# set title
login_window.title('Login Page')
# import the image. Image will represent by bgImage
bgImage=ImageTk.PhotoImage(file='MainBG.jpg')
bgLabel = Label(login_window, image=bgImage)
# to place image we can use following methods
# bgLabel.pack()
# bgLabel.grid(row=0,column=0)
bgLabel.place(x=0,y=0)

# Login Labels Part

# Heading

# call a string variable to use hex color codes
Headbg = "#1E1E1E"
Headfg = "#2C2723"

heading=Label(login_window,text='USER LOGIN',font=('Gilroy',30,'bold'),bg=Headbg, fg='snow')
# use 'place()' method if you want to place label on a particular position
heading.place(x=180,y=110)

# user name entry
usernameEntry = Entry(login_window, width=25, font=('Gilroy',17,'bold'), bd=0, fg='snow', bg=Headbg)
usernameEntry.place(x=130,y=225)
# add pre-instructions
usernameEntry.insert(0,'User Name')
# usernameEntry bind to 'on_enter' function using bind() method
usernameEntry.bind('<FocusIn>',un_enter)
usernameEntry.bind('<FocusOut>',un_not_enter)
# crete a frame to the user name entry
Frame(login_window,width=350,height=2,bg='snow').place(x=125,y=260)

# password entry
passwordEntry = Entry(login_window, width=25, font=('Gilroy',17,'bold'), bd=0, fg='snow', bg=Headbg)
passwordEntry.place(x=130,y=300)
# add pre-instructions
passwordEntry.insert(0,'Password')
# passwordEntry bind to 'pw_enter' function using bind() method
passwordEntry.bind('<FocusIn>',pw_enter)
# passwordEntry bind to 'pw_not_enter' function using bind() method
passwordEntry.bind('<FocusOut>',pw_not_enter)
# crete a frame to the user name entry
Frame(login_window,width=350,height=2,bg='snow').place(x=125,y=335)
# eye button
closeeye = PhotoImage(file='close_eye.png')
eyeButton = Button(login_window, image=closeeye, bd=0, bg=Headbg, activebackground=Headbg, cursor='hand2', command=show)
eyeButton.place(x=450,y=300)

# forget button
forgetButton = Button(login_window,text='forgot Password?', bd=0, bg=Headbg, fg='snow', activebackground=Headbg, activeforeground='NavajoWhite4', cursor='hand2', command=forget_pass)
forgetButton.place(x=390,y=360)

# login button
loginButton = Button(login_window,text='Login',font=('Gilroy',16,'bold'), bd=0, width=18, bg='snow', fg=Headbg, activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2', command=login_db)
loginButton.place(x=180,y=420)

# OR label
orLabel=Label(login_window, text='-  OR  -', font=('Gilroy',8,'bold'), fg='snow', bg=Headbg)
orLabel.place(x=280,y=485)

# logos
fbLogo = PhotoImage(file='facebook.png')
fbButton = Button(login_window,image=fbLogo,font=('Gilroy',16,'bold'), bd=0, bg=Headbg, fg='snow', activebackground=Headbg, activeforeground=Headbg, cursor='hand2')
fbButton.place(x=223,y=530)

googleLogo = PhotoImage(file='google.png')
googleButton = Button(login_window,image=googleLogo,font=('Gilroy',16,'bold'), bd=0, bg=Headbg, fg='snow', activebackground=Headbg, activeforeground=Headbg, cursor='hand2')
googleButton.place(x=283,y=530)

twitterLogo = PhotoImage(file='twitter.png')
twitterButton = Button(login_window,image=twitterLogo,font=('Gilroy',16,'bold'), bd=0, bg=Headbg, fg='snow', activebackground=Headbg, activeforeground=Headbg, cursor='hand2')
twitterButton.place(x=343,y=530)

# create account label
createLabel=Label(login_window, text="Don't have an account?", font=('Gilroy',8,'bold'), fg='snow', bg=Headbg)
createLabel.place(x=177,y=600)
createButton = Button(login_window,text='Create new account', font=('Gilroy',8,'bold'), bd=0, bg=Headbg, fg='red', activebackground=Headbg, activeforeground='NavajoWhite4', cursor='hand2', command=direct_signup)
createButton.place(x=307,y=600)


login_window.mainloop()