import tkinter as tk
# tkinter is a module/container/file which contain classes and methods which help to create GUI.
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import 'random' module to generate a bill number.
# import 'os' module to create a folder
# improt 'tempfile' module to create a temporal file
# import 'smptlib' module to send mails
import random,os,tempfile,smtplib
# go to terminal and type 'pip install pillow' install
# after installed import the module. PIL = Python Image Library
from PIL import ImageTk


# -------functionality Part-------



# ------GUI Part-----

# create a window using TK() class. Assign the class to an object. 'root' is a object name/ window name
dash_window=Tk()
# to change the size of the window use 'geometry('width * height')' method
dash_window.geometry('1100x700+200+50')
# to change the title of the window use 'title()' method
dash_window.title('Dash Board')
# Stop maximize the window
dash_window.resizable(0,0)
# import the image. Image will represent by dashImage
dashImage=ImageTk.PhotoImage(file='dashboard_BG.jpg')
dashLabel = Label(dash_window, image=dashImage)
# to place image we can use following methods
dashLabel.place(x=0,y=0)

# --------buttons--------

# body section color
#Headbg = "#1E1E1E"
Headbg = "#2A2A2A"
Headfg = "#2C2723"
# button section background color
ButtonBG = "#4D4D4D"

# total button
Frame(dash_window,width=158,height=2,bg='snow').place(x=0,y=140)
totalButton = Button(dash_window,text='Total',font=('Gilroy',14,'bold'), bd=0, width=12, height=2, bg=ButtonBG, fg='snow', activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2')
totalButton.place(x=2,y=150)
# crete a frame to the total button
Frame(dash_window,width=158,height=2,bg='snow').place(x=0,y=215)

# bill button
billButton = Button(dash_window,text='Bill',font=('Gilroy',14,'bold'), bd=0, width=12, height=2, bg=ButtonBG, fg='snow', activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2')
billButton.place(x=2,y=225)
# crete a frame to the bill button
Frame(dash_window,width=158,height=2,bg='snow').place(x=0,y=290)

# email button
emailButton = Button(dash_window,text='Email',font=('Gilroy',14,'bold'), bd=0, width=12, height=2, bg=ButtonBG, fg='snow', activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2')
emailButton.place(x=2,y=300)
# crete a frame to the email button
Frame(dash_window,width=158,height=2,bg='snow').place(x=0,y=365)

# print button
printButton = Button(dash_window,text='Print',font=('Gilroy',14,'bold'), bd=0, width=12, height=2, bg=ButtonBG, fg='snow', activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2')
printButton.place(x=2,y=375)
# crete a frame to the print button
Frame(dash_window,width=158,height=2,bg='snow').place(x=0,y=440)

# clear button
clearButton = Button(dash_window,text='Clear',font=('Gilroy',14,'bold'), bd=0, width=12, height=2, bg=ButtonBG, fg='snow', activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2')
clearButton.place(x=2,y=450)
# crete a frame to the clear button
Frame(dash_window,width=158,height=2,bg='snow').place(x=0,y=515)

# logout button
logoutButton = Button(dash_window,text='Logout',font=('Gilroy',14,'bold'), bd=0, width=12, height=2, bg=ButtonBG, fg='snow', activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2')
logoutButton.place(x=2,y=525)
# crete a frame to the logout button
Frame(dash_window,width=158,height=2,bg='snow').place(x=0,y=590)

# logout button
logoutButton = Button(dash_window,text='Logout',font=('Gilroy',14,'bold'), bd=0, width=12, height=2, bg=ButtonBG, fg='snow', activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2')
logoutButton.place(x=2,y=525)
# crete a frame to the logout button
Frame(dash_window,width=158,height=2,bg='snow').place(x=0,y=590)

# ------product category buttons------

# Burger button
bunLogo = PhotoImage(file='Burger.png')
bunButton = Button(dash_window,image=bunLogo,font=('Gilroy',16,'bold'), width=100,height=100, bd=0, bg=Headbg, fg='snow', activebackground=ButtonBG, activeforeground=Headbg, cursor='hand2')
bunButton.place(x=200,y=25)
# bun label
bunLabel=Label(dash_window, text='Burger', font=('Gilroy',12,'bold'),width=10, fg='snow', bg=Headbg)
bunLabel.place(x=200,y=125)

# hotdog button
hotdogLogo = PhotoImage(file='hotdog.png')
hotdogButton = Button(dash_window,image=hotdogLogo,font=('Gilroy',16,'bold'), width=100,height=100, bd=0, bg=Headbg, fg='snow', activebackground=ButtonBG, activeforeground=Headbg, cursor='hand2')
hotdogButton.place(x=350,y=25)
# hotdog label
hotdogLabel=Label(dash_window, text='Short-eats', font=('Gilroy',12,'bold'),width=10, fg='snow', bg=Headbg)
hotdogLabel.place(x=350,y=125)

# meal button
mealLogo = PhotoImage(file='Biriyani.png')
mealButton = Button(dash_window,image=mealLogo,font=('Gilroy',16,'bold'), width=100,height=100, bd=0, bg=Headbg, fg='snow', activebackground=ButtonBG, activeforeground=Headbg, cursor='hand2')
mealButton.place(x=500,y=25)
# meal label
mealLabel=Label(dash_window, text='Meals', font=('Gilroy',12,'bold'),width=10, fg='snow', bg=Headbg)
mealLabel.place(x=500,y=125)

# icecream button
icecreamLogo = PhotoImage(file='Ice Cream.png')
icecreamButton = Button(dash_window,image=icecreamLogo,font=('Gilroy',16,'bold'), width=100,height=100, bd=0, bg=Headbg, fg='snow', activebackground=ButtonBG, activeforeground=Headbg, cursor='hand2')
icecreamButton.place(x=650,y=25)
# icecream label
icecreamLabel=Label(dash_window, text='Ice Cream', font=('Gilroy',12,'bold'),width=10, fg='snow', bg=Headbg)
icecreamLabel.place(x=650,y=125)

# drinks button
drinksLogo = PhotoImage(file='Drinks.png')
drinksButton = Button(dash_window,image=drinksLogo,font=('Gilroy',16,'bold'), width=100,height=100, bd=0, bg=Headbg, fg='snow', activebackground=ButtonBG, activeforeground=Headbg, cursor='hand2')
drinksButton.place(x=800,y=25)
# drinks label
drinksLabel=Label(dash_window, text='Drinks', font=('Gilroy',12,'bold'),width=10, fg='snow', bg=Headbg)
drinksLabel.place(x=800,y=125)

# other button
otherLogo = PhotoImage(file='Snacks.png')
otherButton = Button(dash_window,image=otherLogo,font=('Gilroy',16,'bold'), width=100,height=100, bd=0, bg=Headbg, fg='snow', activebackground=ButtonBG, activeforeground=Headbg, cursor='hand2')
otherButton.place(x=950,y=25)
# other label
otherLabel=Label(dash_window, text='Other', font=('Gilroy',12,'bold'),width=10, fg='snow', bg=Headbg)
otherLabel.place(x=950,y=125)


# -----------Products-----------

productsLabel = Label(dash_window, text='Choose Oder', font=('Gilroy',15,'bold'), bd=0, relief=GROOVE, bg=Headbg, fg='snow')
productsLabel.place(x=180,y=180)

# use Canvas() method to place the scrollbar to add items
wrapper1 = LabelFrame(dash_window)
mycanvas = Canvas(wrapper1, width=450, height=460, bg='snow')
mycanvas.pack(side=LEFT, fill="both", expand="yes")

# to add a scrollbar, use 'Scrollbar()' class. Use orient to to make vertical or horizontal scrollbar
scrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

mycanvas.configure(yscrollcommand=scrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

# canvas frames

burgerframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=burgerframe, anchor="nw")

shortsframe = Frame(mycanvas)
mycanvas.create_window((0,300), window=shortsframe, anchor="nw")

mealsframe = Frame(mycanvas)
mycanvas.create_window((0,680), window=mealsframe, anchor="nw")

normal_icecreamframe = Frame(mycanvas)
mycanvas.create_window((0,895), window=normal_icecreamframe, anchor="nw")

magic_icecreamframe = Frame(mycanvas)
mycanvas.create_window((0,1190), window=magic_icecreamframe, anchor="nw")

drinks_frame = Frame(mycanvas)
mycanvas.create_window((0,2780), window=drinks_frame, anchor="nw")

other_frame = Frame(mycanvas)
mycanvas.create_window((0,2980), window=other_frame, anchor="nw")

wrapper1.place(x=180,y=220)

# burger section
chicken_burger_title_label = Label(burgerframe, text='  BURGERS', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
chicken_burger_title_label.grid(row=0, column=0, columnspan=3, sticky=W)

chiken_burger_Logo = PhotoImage(file='Bun.png')
chiken_burger_Button = Button(burgerframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
chiken_burger_Button.grid(row=1,column=0)
chicken_burger_Button = Button(burgerframe, text='Chicken Burger', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
chicken_burger_Button.grid(row=1,column=1)
chicken_burger_Button = Button(burgerframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
chicken_burger_Button.grid(row=1,column=2)

prawn_burger_Logo = PhotoImage(file='Bun.png')
prawn_burger_Button = Button(burgerframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
prawn_burger_Button.grid(row=2,column=0)
prawn_burger_Button = Button(burgerframe, text='Prawn Burger', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
prawn_burger_Button.grid(row=2,column=1)
prawn_burger_Button = Button(burgerframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
prawn_burger_Button.grid(row=2,column=2)

cheese_burger_Logo = PhotoImage(file='Bun.png')
cheese_burger_Button = Button(burgerframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
cheese_burger_Button.grid(row=3,column=0)
cheese_burger_Button = Button(burgerframe, text='Cheese Burger', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
cheese_burger_Button.grid(row=3,column=1)
cheese_burger_Button = Button(burgerframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
cheese_burger_Button.grid(row=3,column=2)

# short-eats section

short_eats_title_label = Label(shortsframe, text='  SHORT EATS', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
short_eats_title_label.grid(row=0, column=0, columnspan=3, sticky=W)

hotdog_Logo = PhotoImage(file='hotdog.png')
hotdog_Button = Button(shortsframe,image=hotdogLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
hotdog_Button.grid(row=1,column=0)
hotdog_Button = Button(shortsframe, text='Hotdog', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
hotdog_Button.grid(row=1,column=1)
hotdog_Button = Button(shortsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
hotdog_Button.grid(row=1,column=2)

fish_bun_Logo = PhotoImage(file='fish bun.png')
fish_bun_Button = Button(shortsframe,image=fish_bun_Logo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
fish_bun_Button.grid(row=2,column=0)
fish_bun_Button = Button(shortsframe, text='Fish Bun', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
fish_bun_Button.grid(row=2,column=1)
fish_bun_Button = Button(shortsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
fish_bun_Button.grid(row=2,column=2)

pastry_Logo = PhotoImage(file='pastry.png')
pastry_Button = Button(shortsframe,image=pastry_Logo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
pastry_Button.grid(row=3,column=0)
pastry_Button = Button(shortsframe, text='Pastry', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
pastry_Button.grid(row=3,column=1)
pastry_Button = Button(shortsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
pastry_Button.grid(row=3,column=2)

egg_bun_Logo = PhotoImage(file='eggbun.png')
egg_bun_Button = Button(shortsframe,image=egg_bun_Logo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
egg_bun_Button.grid(row=4,column=0)
egg_bun_Button = Button(shortsframe, text='Egg Bun', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
egg_bun_Button.grid(row=4,column=1)
egg_bun_Button = Button(shortsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
egg_bun_Button.grid(row=4,column=2)

# meals section

meals_title_label = Label(mealsframe, text='  MEALS', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
meals_title_label.grid(row=0, column=0, columnspan=3, sticky=W)

vegi_meal_Logo = PhotoImage(file='Biriyani.png')
vegi_meal_Button = Button(mealsframe,image=vegi_meal_Logo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
vegi_meal_Button.grid(row=1,column=0)
vegi_meal_Button = Button(mealsframe, text='Vegi Meal', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
vegi_meal_Button.grid(row=1,column=1)
vegi_meal_Button = Button(mealsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
vegi_meal_Button.grid(row=1,column=2)

chicken_meal_Logo = PhotoImage(file='Biriyani.png')
chicken_meal_Button = Button(mealsframe,image=chicken_meal_Logo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
chicken_meal_Button.grid(row=2,column=0)
chicken_meal_Button = Button(mealsframe, text='Chicken Meal', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
chicken_meal_Button.grid(row=2,column=1)
chicken_meal_Button = Button(mealsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
chicken_meal_Button.grid(row=2,column=2)

# normal ice cream section

ice_cream_label = Label(normal_icecreamframe, text='  NORMAL ICE-CREAM', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
ice_cream_label.grid(row=0, column=0, columnspan=3, sticky=W)

vanila_icecream_Logo = PhotoImage(file='Bun.png')
vanila_icecream_Button = Button(normal_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
vanila_icecream_Button.grid(row=1,column=0)
vanila_icecream_Button = Button(normal_icecreamframe, text='Vanila Ice-Cream', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
vanila_icecream_Button.grid(row=1,column=1)
vanila_icecream_Button = Button(normal_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
vanila_icecream_Button.grid(row=1,column=2)

chocolate_icecream_Logo = PhotoImage(file='Bun.png')
chocolate_icecream_Button = Button(normal_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
chocolate_icecream_Button.grid(row=2,column=0)
chocolate_icecream_Button = Button(normal_icecreamframe, text='Chocolate Ice-Cream', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
chocolate_icecream_Button.grid(row=2,column=1)
chocolate_icecream_Button = Button(normal_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
chocolate_icecream_Button.grid(row=2,column=2)

strawberry_icecream_Logo = PhotoImage(file='Bun.png')
strawberry_icecream_Button = Button(normal_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
strawberry_icecream_Button.grid(row=3,column=0)
strawberry_icecream_Button = Button(normal_icecreamframe, text='Strawberry Ice-Cream', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
strawberry_icecream_Button.grid(row=3,column=1)
strawberry_icecream_Button = Button(normal_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
strawberry_icecream_Button.grid(row=3,column=2)

# magic ice cream section

magic_ice_cream_label = Label(magic_icecreamframe, text='  MAGIC ICE-CREAM', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
magic_ice_cream_label.grid(row=0, column=0, columnspan=3, sticky=W)

faluda_stick_Logo = PhotoImage(file='Bun.png')
faluda_stick_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
faluda_stick_Button.grid(row=1,column=0)
faluda_stick_Button = Button(magic_icecreamframe, text='Faluda Stick', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
faluda_stick_Button.grid(row=1,column=1)
faluda_stick_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
faluda_stick_Button.grid(row=1,column=2)

fantasticstick_chocolate_Logo = PhotoImage(file='Bun.png')
fantasticstick_chocolate_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
fantasticstick_chocolate_Button.grid(row=2,column=0)
fantasticstick_chocolate_Button = Button(magic_icecreamframe, text='Fantasticstick-Chocolate', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
fantasticstick_chocolate_Button.grid(row=2,column=1)
fantasticstick_chocolate_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
fantasticstick_chocolate_Button.grid(row=2,column=2)

cool_berry_Logo = PhotoImage(file='Bun.png')
cool_berry_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
cool_berry_Button.grid(row=3,column=0)
cool_berry_Button = Button(magic_icecreamframe, text='Cool Berry', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
cool_berry_Button.grid(row=3,column=1)
cool_berry_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
cool_berry_Button.grid(row=3,column=2)

divul_magic_stick_Logo = PhotoImage(file='Bun.png')
divul_magic_stick_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
divul_magic_stick_Button.grid(row=4,column=0)
divul_magic_stick_Button = Button(magic_icecreamframe, text='Divul Magic Stick', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
divul_magic_stick_Button.grid(row=4,column=1)
divul_magic_stick_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
divul_magic_stick_Button.grid(row=4,column=2)

magic_choc_chocolate_Logo = PhotoImage(file='Bun.png')
magic_choc_chocolate_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
magic_choc_chocolate_Button.grid(row=5,column=0)
magic_choc_chocolate_Button = Button(magic_icecreamframe, text='Magic Choc-Chocolate', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
magic_choc_chocolate_Button.grid(row=5,column=1)
magic_choc_chocolate_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
magic_choc_chocolate_Button.grid(row=5,column=2)

traffic_light_stick_Logo = PhotoImage(file='Bun.png')
traffic_light_stick_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
traffic_light_stick_Button.grid(row=6,column=0)
traffic_light_stick_Button = Button(magic_icecreamframe, text='Traffic Light Stick', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
traffic_light_stick_Button.grid(row=6,column=1)
traffic_light_stick_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
traffic_light_stick_Button.grid(row=6,column=2)

magic_caramel_bar_Logo = PhotoImage(file='Bun.png')
magic_caramel_bar_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
magic_caramel_bar_Button.grid(row=7,column=0)
magic_caramel_bar_Button = Button(magic_icecreamframe, text='Magic Caramel Bar', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
magic_caramel_bar_Button.grid(row=7,column=1)
magic_caramel_bar_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
magic_caramel_bar_Button.grid(row=7,column=2)

magic_cube_Logo = PhotoImage(file='Bun.png')
magic_cube_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
magic_cube_Button.grid(row=8,column=0)
magic_cube_Button = Button(magic_icecreamframe, text='Magic Cube', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
magic_cube_Button.grid(row=8,column=1)
magic_cube_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
magic_cube_Button.grid(row=8,column=2)

vanila_magic_Logo = PhotoImage(file='Bun.png')
vanila_magic_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
vanila_magic_Button.grid(row=9,column=0)
vanila_magic_Button = Button(magic_icecreamframe, text='Vanila Magic', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
vanila_magic_Button.grid(row=9,column=1)
vanila_magic_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
vanila_magic_Button.grid(row=9,column=2)

kithul_magic_Logo = PhotoImage(file='Bun.png')
kithul_magic_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
kithul_magic_Button.grid(row=10,column=0)
kithul_magic_Button = Button(magic_icecreamframe, text='Kithul Magic', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
kithul_magic_Button.grid(row=10,column=1)
kithul_magic_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
kithul_magic_Button.grid(row=10,column=2)

vanila_chock_mix_Logo = PhotoImage(file='Bun.png')
vanila_chock_mix_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
vanila_chock_mix_Button.grid(row=11,column=0)
vanila_chock_mix_Button = Button(magic_icecreamframe, text='Vanila Chock-Mix', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
vanila_chock_mix_Button.grid(row=11,column=1)
vanila_chock_mix_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
vanila_chock_mix_Button.grid(row=11,column=2)

fruit_and_nut_cup_Logo = PhotoImage(file='Bun.png')
fruit_and_nut_cup_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
fruit_and_nut_cup_Button.grid(row=12,column=0)
fruit_and_nut_cup_Button = Button(magic_icecreamframe, text='Fruit & Nut-Cup', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
fruit_and_nut_cup_Button.grid(row=12,column=1)
fruit_and_nut_cup_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
fruit_and_nut_cup_Button.grid(row=12,column=2)

chocolate_magic_Logo = PhotoImage(file='Bun.png')
chocolate_magic_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
chocolate_magic_Button.grid(row=13,column=0)
chocolate_magic_Button = Button(magic_icecreamframe, text='Chocolate Magic', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
chocolate_magic_Button.grid(row=13,column=1)
chocolate_magic_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
chocolate_magic_Button.grid(row=13,column=2)

magic_cone_chocolate_Logo = PhotoImage(file='Bun.png')
magic_cone_chocolate_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
magic_cone_chocolate_Button.grid(row=14,column=0)
magic_cone_chocolate_Button = Button(magic_icecreamframe, text='Magic Cone-Chocolate', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
magic_cone_chocolate_Button.grid(row=14,column=1)
magic_cone_chocolate_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
magic_cone_chocolate_Button.grid(row=14,column=2)

magic_cone_vanila_Logo = PhotoImage(file='Bun.png')
magic_cone_vanila_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
magic_cone_vanila_Button.grid(row=15,column=0)
magic_cone_vanila_Button = Button(magic_icecreamframe, text='Magic Cone-Vanila', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
magic_cone_vanila_Button.grid(row=15,column=1)
magic_cone_vanila_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
magic_cone_vanila_Button.grid(row=15,column=2)

heavenly_crunch_cone_Logo = PhotoImage(file='Bun.png')
heavenly_crunch_cone_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
heavenly_crunch_cone_Button.grid(row=16,column=0)
heavenly_crunch_cone_Button = Button(magic_icecreamframe, text='Heavenly Crunch Cone', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
heavenly_crunch_cone_Button.grid(row=16,column=1)
heavenly_crunch_cone_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
heavenly_crunch_cone_Button.grid(row=16,column=2)

fruit_and_nut_cone_Logo = PhotoImage(file='Bun.png')
fruit_and_nut_cone_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
fruit_and_nut_cone_Button.grid(row=17,column=0)
fruit_and_nut_cone_Button = Button(magic_icecreamframe, text='Fruit & Nut Cone', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
fruit_and_nut_cone_Button.grid(row=17,column=1)
fruit_and_nut_cone_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
fruit_and_nut_cone_Button.grid(row=17,column=2)

cappuccino_cone_Logo = PhotoImage(file='Bun.png')
cappuccino_cone_Button = Button(magic_icecreamframe,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
cappuccino_cone_Button.grid(row=18,column=0)
cappuccino_cone_Button = Button(magic_icecreamframe, text='Cappuccino Cone', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
cappuccino_cone_Button.grid(row=18,column=1)
cappuccino_cone_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
cappuccino_cone_Button.grid(row=18,column=2)


# drinks section

drinks_label = Label(drinks_frame, text='  Drinks', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
drinks_label.grid(row=0, column=0, columnspan=3, sticky=W)

water_Logo = PhotoImage(file='Bun.png')
water_Button = Button(drinks_frame,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
water_Button.grid(row=1,column=0)
water_Button = Button(drinks_frame, text='Water Bottle', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
water_Button.grid(row=1,column=1)
water_Button = Button(drinks_frame,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
water_Button.grid(row=1,column=2)

ginger_tea_Logo = PhotoImage(file='Bun.png')
ginger_tea_Button = Button(drinks_frame,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
ginger_tea_Button.grid(row=2,column=0)
ginger_tea_Button = Button(drinks_frame, text='Ginger Tea', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
ginger_tea_Button.grid(row=2,column=1)
ginger_tea_Button = Button(drinks_frame,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
ginger_tea_Button.grid(row=2,column=2)

# other section

other_label = Label(other_frame, text='  Other', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
other_label.grid(row=0, column=0, columnspan=3, sticky=W)

rotti_Logo = PhotoImage(file='Bun.png')
rotti_Button = Button(other_frame,image=bunLogo,font=('Gilroy',16,'bold'), width=90,height=80, bd=0, bg='gray', fg='snow', cursor='hand2')
rotti_Button.grid(row=1,column=0)
rotti_Button = Button(other_frame, text='Rotti', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray')
rotti_Button.grid(row=1,column=1)
rotti_Button = Button(other_frame,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2')
rotti_Button.grid(row=1,column=2)

# set the scrollbar comparatively to the text
scrollbar.config(command=mycanvas.yview)


# -------Bill Area-------

bill_area_Label = Label(dash_window, text='Bill Area', font=('Gilroy',15,'bold'), bd=0,relief=GROOVE, bg=Headbg, fg='snow')
bill_area_Label.place(x=680,y=180)

billFrame = Frame(dash_window, relief=GROOVE)
billFrame.place(x=680,y=220)

# to add a scrollbar, use 'Scrollbar()' class. Use orient to to make vertical or horizontal scrollbar
scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# to create a text area, use 'text()' class. To set the scrollbar with the text area, use 'yscrollcommand=scrollbar.set' command.
textarea = Text(billFrame, height=25, width=45, yscrollcommand=scrollbar.set)
textarea.pack()
#set the scrollbar comparatively to the text
scrollbar.config(command=textarea.yview)



# total price
cosmetic_price_Label = Label(dash_window, text='Total Price :', font=('Gilroy',15,'bold'), bd=0, relief=GROOVE, bg=Headbg, fg='snow')
cosmetic_price_Label.place(x=700,y=645)
cosmetic_price_Entry = Entry(dash_window, font=('arial', 15), bd=0, width=15)
cosmetic_price_Entry.place(x=850,y=645)
cosmetic_price_Label = Label(dash_window, text='Rs.', font=('Gilroy',14,'bold'), bd=0, relief=GROOVE, bg='white', fg=Headbg)
cosmetic_price_Label.place(x=980,y=645)

#scrollbar.config(command=l1.yview)

dash_window.mainloop()