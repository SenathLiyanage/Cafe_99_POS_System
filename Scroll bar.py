from tkinter import *
from tkinter import ttk

win =Tk()

wrapper1 = LabelFrame(win)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical",command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor="nw")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)

#for i in range(50):
    #Button(myframe, text="Button"+str(i)).pack()

bunLogo = PhotoImage(file='Bun.png')
bunButton = Button(myframe,image=bunLogo,font=('Gilroy',16,'bold'), width=180,height=96, bd=0, bg='gray', fg='snow', cursor='hand2')
bunButton.grid(row=0,column=0)
chicken_burger_Label = Label(myframe, text='Burger', font=('Gilroy',15,'bold'), width=10, height=4, bd=0, relief=GROOVE, bg='gray', fg='snow')
chicken_burger_Label.grid(row=0,column=1)
icecreamButton = Button(myframe,text='-',font=('Gilroy',16,'bold'), width=10,height=3, bd=0, bg='navy', fg='snow', cursor='hand2')
icecreamButton.grid(row=0,column=2, padx=2)


yscrollbar.config(command=mycanvas.yview)

win.geometry("500x500")
win.resizable(False,False)
win.title("MyScroller")

yscrollbar.config(command=mycanvas.yview)
win.mainloop()