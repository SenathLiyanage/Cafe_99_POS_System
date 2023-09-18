from tkinter import *
# import 'messagebox' to show messages
from tkinter import messagebox
# if the image is not in png formate need to install an external module to add jpg image
# go to terminal and type 'pip install pillow' install
# after installed import the module. PIL = Python Image Library
from PIL import ImageTk
# import pymysql to connect python with the MySQL database
import pymysql

# functional part

def change_pw():
    if usernameEntry.get() == '' or usernameEntry.get() == 'User Name' or new_pwEntry.get() == '' or new_pwEntry.get() == 'Password' or confirm_pwEntry.get() == '' or confirm_pwEntry.get() == 'Confirm Password':
        messagebox.showerror('Error', 'Admin data are required')
    elif new_pwEntry.get() != confirm_pwEntry.get():
        messagebox.showerror('Error','Passwords are not matching')
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
        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))
        # if there is no any row match with the entered username display error msg
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid User Name!')
        else:
            # update the password
            query='update data set password=%s where username=%s'
            mycursor.execute(query,(new_pwEntry.get(),usernameEntry.get()))
            # commit the changes
            con.commit()
            # close the connection
            con.close()
            # if the password is set successfully send msg box
            messagebox.showinfo('Success', 'Password updated successfully! Login with the new password')
            # when click ok button
            # close the Reset page
            pwreset_window.destroy()
            # open the Login page
            import main


def un_enter(event):
    # if the text area has text name called 'UserName' when click curser every thing will delete
    if usernameEntry.get()=='User Name':
        usernameEntry.delete(0,END)

def un_not_enter(event):
    # if the text area is null when click another Entry the area fill with text 'UserName'
    if usernameEntry.get()=='':
        usernameEntry.insert(0,'User Name')

def npw_enter(event):
    # if the text area has text name called 'New Password' when click curser every thing will delete
    if new_pwEntry.get()=='New Password':
        new_pwEntry.delete(0,END)

def npw_not_enter(event):
    # if the text area is null when click another Entry the area fill with text 'New Password'
    if new_pwEntry.get()=='':
        new_pwEntry.insert(0,'New Password')

def cpw_enter(event):
    # if the text area has text name called 'New Password' when click curser every thing will delete
    if confirm_pwEntry.get()=='Confirm Password':
        confirm_pwEntry.delete(0,END)

def cpw_not_enter(event):
    # if the text area is null when click another Entry the area fill with text 'New Password'
    if confirm_pwEntry.get()=='':
        confirm_pwEntry.insert(0,'Confirm Password')

# GUI Part

pwreset_window=Tk()
pwreset_window.title('Password Reset Page')
pwreset_window.resizable(0,0)

# ImageTk class use for jpg files
background = ImageTk.PhotoImage(file='BGimage.jpg')
pwreset_window.geometry('992x613+250+100')
bgLabel = Label(pwreset_window, image=background)
bgLabel.place(x=0,y=0)

# background color
Headbg = "#D3CAB3"
# font color
Headfg = "#2C2723"

heading=Label(pwreset_window,text='RESET PASSWORD',font=('Gilroy',20,'bold'),bg=Headbg, fg=Headfg)
heading.place(x=200,y=130)

# username entry
usernameEntry = Entry(pwreset_window, width=28, font=('Gilroy',11,'bold'), bd=0, fg=Headfg, bg=Headbg)
usernameEntry.place(x=210,y=215)
# add pre-instructions
usernameEntry.insert(0,'User Name')
# usernameEntry bind to 'on_enter' function using bind() method
usernameEntry.bind('<FocusIn>',un_enter)
usernameEntry.bind('<FocusOut>',un_not_enter)
# crete a frame to the user name entry
Frame(pwreset_window,width=250,height=2,bg=Headfg).place(x=210,y=237)

# new_pw entry
new_pwEntry = Entry(pwreset_window, width=28, font=('Gilroy',11,'bold'), bd=0, fg=Headfg, bg=Headbg)
new_pwEntry.place(x=210,y=275)
# add pre-instructions
new_pwEntry.insert(0,'New Password')
# new password Entry bind to 'on_enter' function using bind() method
new_pwEntry.bind('<FocusIn>',npw_enter)
new_pwEntry.bind('<FocusOut>',npw_not_enter)
# create a frame to the new password entry
Frame(pwreset_window,width=250,height=2,bg=Headfg).place(x=210,y=297)

# confirm_pw entry
confirm_pwEntry = Entry(pwreset_window, width=28, font=('Gilroy',11,'bold'), bd=0, fg=Headfg, bg=Headbg)
confirm_pwEntry.place(x=210,y=335)
# add pre-instructions
confirm_pwEntry.insert(0,'Confirm Password')
# confirm password Entry bind to 'on_enter' function using bind() method
confirm_pwEntry.bind('<FocusIn>',cpw_enter)
confirm_pwEntry.bind('<FocusOut>',cpw_not_enter)
# create a frame to the confirm password entry
Frame(pwreset_window,width=250,height=2,bg=Headfg).place(x=210,y=357)

# submit button
# when clicking submit button the data should store inside the database
submitButton = Button(pwreset_window,text='Submit',font=('Gilroy',16,'bold'), bd=0, width=18, bg=Headfg, fg=Headbg, activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2', command=change_pw)
submitButton.place(x=215,y=420)



pwreset_window.mainloop()