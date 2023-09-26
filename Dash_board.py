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

def total():
    global chicken_burger_price, prawn_burger_price, cheese_burger_price
    global hotdog_price, fish_bun_price, pastry_price, egg_bun_price
    global vegi_meal_price, chicken_meal_price
    global vanila_icecream_price, chocolate_icecream_price, strawberry_icecream_price
    global faluda_stick_price,fantasticstick_chocolate_price,cool_berry_price,divul_magic_stick_price,choc_chocolate_price,traffic_light_stick_price,caramel_bar_price,cone_vanila_price,fruit_and_nut_cone_price
    global Magic_Cube_price,vanila_magic_price,kithul_magic_price,vanila_chock_mix_price,vanila_chock_mix_price,fruit_and_nut_cup_price,cocolate_magic_price,cone_chocolate_price,heavenly_crunch_price,cappuccino_price
    global water_price, ginger_tea_price
    global rotti_price

    # burger
    chicken_burger_price = chkb_count * 400
    prawn_burger_price = prw_count * 500
    cheese_burger_price = che_count * 300
    # shot eats
    hotdog_price = hod_count * 100
    fish_bun_price = fib_count * 100
    pastry_price = pas_count * 100
    egg_bun_price = eggb_count * 100
    # meals
    vegi_meal_price = vegi_count * 100
    chicken_meal_price = chkm_count * 100
    # normal ice cream
    vanila_icecream_price = vaice_count * 100
    chocolate_icecream_price = chocice_count * 100
    strawberry_icecream_price = strice_count * 100
    # magic ice cream
    faluda_stick_price = fluda_stick_count * 100
    fantasticstick_chocolate_price = fantastick_chocolate_count * 100
    cool_berry_price = cool_berry_count * 100
    divul_magic_stick_price = divul_magic_count * 100
    choc_chocolate_price = choc_chocolate_count * 100
    traffic_light_stick_price = traffic_light_stick_count * 100
    caramel_bar_price = caramel_bar_count * 100
    Magic_Cube_price = Magic_Cube_count * 100
    vanila_magic_price = vanila_magic_count * 100
    kithul_magic_price = kithul_magic_count * 100
    vanila_chock_mix_price = vanila_choc_mix_count * 100
    fruit_and_nut_cup_price = fruit_n_nut_cup_count * 100
    cocolate_magic_price = cocolate_magic_count * 100
    cone_chocolate_price = cone_chocolate_count * 100
    cone_vanila_price = cone_vanila_count * 100
    heavenly_crunch_price = heavenly_crunch_count * 100
    fruit_and_nut_cone_price =  fruit_n_nut_cone_count * 100
    cappuccino_price = cappuccino_count * 100
    # drinks cream
    water_price = water_count * 100
    ginger_tea_price = ginger_tea_count * 100
    # other
    rotti_price = rotti_count * 100

    # calculate each section prices
    total_burger_price = chicken_burger_price + prawn_burger_price + cheese_burger_price
    total_shorts_price = hotdog_price + fish_bun_price + pastry_price + egg_bun_price
    total_meal_price = vegi_meal_price + chicken_meal_price
    total_normalice_price = vanila_icecream_price + chocolate_icecream_price + strawberry_icecream_price
    total_magic1_price = faluda_stick_price+fantasticstick_chocolate_price+cool_berry_price+divul_magic_stick_price+choc_chocolate_price+traffic_light_stick_price+caramel_bar_price+cone_vanila_price+fruit_and_nut_cone_price
    total_magic2_price = Magic_Cube_price+vanila_magic_price+kithul_magic_price+vanila_chock_mix_price+vanila_chock_mix_price+fruit_and_nut_cup_price+cocolate_magic_price+cone_chocolate_price+heavenly_crunch_price+cappuccino_price
    total_drinks_price = water_price + ginger_tea_price
    total_other_price = rotti_price

    # calculate grand total price
    total_price = total_burger_price+total_shorts_price+total_meal_price+total_normalice_price+total_magic1_price+total_magic2_price+total_drinks_price+total_other_price

    # before enter total value, delete the values inside the entry field using 'delete()' method. 'delete(0,END)' ---> delete from start to end
    total_price_Entry.delete(0, END)

    # convert 'total_price' into string using 'str()' or f'{total_price} Rs'
    total_price_Entry.insert(0, 'Rs. ' + str(total_price))

# -----------Burger functions----------

chkb_count = 0
prw_count=0
che_count=0

def chicken_burger():
    global chkb_count
    chkb_count = chkb_count + 1
    data_list = ['Chicken Burger',f'{chkb_count}']

    for item in data_list:
        index_to_delete = 1
        if index_to_delete < len(data_list):
            remove data_list[index_to_delete]
        textarea.insert(tk.END, item + "\t\t\t\t\n")
def remove_chicken_burger():
    global chkb_count
    if chkb_count>0:
        chkb_count = chkb_count - 1
        textarea.insert(END, 'Chicken Burger\t\t\t\t')
        textarea.insert(END, f'{chkb_count}\n')

def prawn_burger():
    global prw_count
    prw_count = prw_count + 1
    textarea.delete("1.0","1.1")
    prawn_burger_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    prawn_burger_Entry.grid(row=1, column=0, padx=8)
    prawn_burger_Entry.insert(END, 'Prawn Burger')
    prawn_burger_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    prawn_burger_qEntry.grid(row=1, column=1, padx=8)
    prawn_burger_qEntry.insert(END, f'{prw_count}')
def remove_prawn_burger():
    global prw_count
    if prw_count>0:
        prw_count = prw_count - 1
        prawn_burger_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        prawn_burger_qEntry.grid(row=1, column=1, padx=8)
        prawn_burger_qEntry.insert(END, f'{prw_count}')

def cheese_burger():
    global che_count
    che_count = che_count + 1
    cheese_burger_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    cheese_burger_Entry.grid(row=2, column=0, padx=8)
    cheese_burger_Entry.insert(END, 'Cheese Burger')
    cheese_burger_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    cheese_burger_qEntry.grid(row=2, column=1, padx=8)
    cheese_burger_qEntry.insert(END, f'{che_count}')
def remove_cheese_burger():
    global che_count
    if che_count>0:
        che_count = che_count - 1
        cheese_burger_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        cheese_burger_qEntry.grid(row=2, column=1, padx=8)
        cheese_burger_qEntry.insert(END, f'{che_count}')

# -----------short eats functions----------

hod_count=0
fib_count=0
pas_count=0
eggb_count=0

def hotdog():
    global hod_count
    hod_count = hod_count + 1
    hotdog_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    hotdog_Entry.grid(row=3, column=0, padx=8)
    hotdog_Entry.insert(END, 'Hotdog')
    hotdog_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    hotdog_qEntry.grid(row=3, column=1, padx=8)
    hotdog_qEntry.insert(END, f'{hod_count}')
def remove_hotdog():
    global hod_count
    if hod_count>0:
        hod_count = hod_count - 1
        hotdog_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        hotdog_qEntry.grid(row=3, column=1, padx=8)
        hotdog_qEntry.insert(END, f'{hod_count}')

def fishbun():
    global fib_count
    fib_count = fib_count + 1
    fishbun_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    fishbun_Entry.grid(row=4, column=0, padx=8)
    fishbun_Entry.insert(END, 'Fish Bun')
    fishbun_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    fishbun_qEntry.grid(row=4, column=1, padx=8)
    fishbun_qEntry.insert(END, f'{fib_count}')
def remove_fishbun():
    global fib_count
    if fib_count>0:
        fib_count = fib_count - 1
        fishbun_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        fishbun_qEntry.grid(row=4, column=1, padx=8)
        fishbun_qEntry.insert(END, f'{fib_count}')

def pastry():
    global pas_count
    pas_count = pas_count + 1
    pastry_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    pastry_Entry.grid(row=5, column=0, padx=8)
    pastry_Entry.insert(END, 'Pastry')
    pastry_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    pastry_qEntry.grid(row=5, column=1, padx=8)
    pastry_qEntry.insert(END, f'{pas_count}')
def remove_pastry():
    global pas_count
    if pas_count>0:
        pas_count = pas_count - 1
        pastry_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        pastry_qEntry.grid(row=5, column=1, padx=8)
        pastry_qEntry.insert(END, f'{pas_count}')

def egg_bun():
    global eggb_count
    eggb_count = eggb_count + 1
    egg_bun_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    egg_bun_Entry.grid(row=6, column=0, padx=8)
    egg_bun_Entry.insert(END, 'Egg Bun')
    egg_bun_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    egg_bun_qEntry.grid(row=6, column=1, padx=8)
    egg_bun_qEntry.insert(END, f'{eggb_count}')
def remove_egg_bun():
    global eggb_count
    if eggb_count>0:
        eggb_count = eggb_count - 1
        egg_bun_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        egg_bun_qEntry.grid(row=6, column=1, padx=8)
        egg_bun_qEntry.insert(END, f'{eggb_count}')

# -----------meals functions----------

vegi_count = 0
chkm_count = 0

def vegi_meal():
    global vegi_count
    vegi_count = vegi_count + 1
    vegi_meal_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    vegi_meal_Entry.grid(row=7, column=0, padx=8)
    vegi_meal_Entry.insert(END, 'Vegi Meal')
    vegi_meal_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    vegi_meal_qEntry.grid(row=7, column=1, padx=8)
    vegi_meal_qEntry.insert(END, f'{vegi_count}')
def remove_vegi_meal():
    global vegi_count
    if vegi_count>0:
        vegi_count = vegi_count - 1
        vegi_meal_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        vegi_meal_qEntry.grid(row=7, column=1, padx=8)
        vegi_meal_qEntry.insert(END, f'{vegi_count}')

def chicken_meal():
    global chkm_count
    chkm_count = chkm_count + 1
    chicken_meal_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    chicken_meal_Entry.grid(row=8, column=0, padx=8)
    chicken_meal_Entry.insert(END, 'Chicken Meal')
    chicken_meal_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    chicken_meal_qEntry.grid(row=8, column=1, padx=8)
    chicken_meal_qEntry.insert(END, f'{chkm_count}')
def remove_chicken_meal():
    global chkm_count
    if chkm_count>0:
        chkm_count = chkm_count - 1
        chicken_meal_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        chicken_meal_qEntry.grid(row=8, column=1, padx=8)
        chicken_meal_qEntry.insert(END, f'{chkm_count}')

# -----------normal icecream functions----------

vaice_count = 0
chocice_count = 0
strice_count = 0

def vanila_icecream():
    global vaice_count
    vaice_count = vaice_count + 1
    vanila_icecream_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    vanila_icecream_Entry.grid(row=9, column=0, padx=8)
    vanila_icecream_Entry.insert(END, 'Vanila ice-Cream')
    vanila_icecream_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    vanila_icecream_qEntry.grid(row=9, column=1, padx=8)
    vanila_icecream_qEntry.insert(END, f'{vaice_count}')
def remove_vanila_icecream():
    global vaice_count
    if vaice_count>0:
        vaice_count = vaice_count - 1
        vanila_icecream_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        vanila_icecream_qEntry.grid(row=9, column=1, padx=8)
        vanila_icecream_qEntry.insert(END, f'{vaice_count}')

def chocolate_icecream():
    global chocice_count
    chocice_count = chocice_count + 1
    chocolate_icecream_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    chocolate_icecream_Entry.grid(row=10, column=0, padx=8)
    chocolate_icecream_Entry.insert(END, 'Chocolate Ice-Cream')
    chocolate_icecream_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    chocolate_icecream_qEntry.grid(row=10, column=1, padx=8)
    chocolate_icecream_qEntry.insert(END, f'{chocice_count}')
def remove_chocolate_icecream():
    global chocice_count
    if chocice_count>0:
        chocice_count = chocice_count - 1
        chocolate_icecream_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        chocolate_icecream_qEntry.grid(row=10, column=1, padx=8)
        chocolate_icecream_qEntry.insert(END, f'{chocice_count}')

def strawberry_icecream():
    global strice_count
    strice_count = strice_count + 1
    strawberry_icecream_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    strawberry_icecream_Entry.grid(row=11, column=0, padx=8)
    strawberry_icecream_Entry.insert(END, 'Strawberry Ice-Cream')
    strawberry_icecream_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    strawberry_icecream_qEntry.grid(row=11, column=1, padx=8)
    strawberry_icecream_qEntry.insert(END, f'{strice_count}')
def remove_strawberry_icecream():
    global strice_count
    if strice_count>0:
        strice_count = strice_count - 1
        strawberry_icecream_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        strawberry_icecream_qEntry.grid(row=11, column=1, padx=8)
        strawberry_icecream_qEntry.insert(END, f'{strice_count}')

# -----------magic icecream functions----------

fluda_stick_count=0
fantastick_chocolate_count=0
cool_berry_count=0
divul_magic_count=0
choc_chocolate_count=0
traffic_light_stick_count=0
caramel_bar_count=0
Magic_Cube_count=0
vanila_magic_count=0
kithul_magic_count=0
vanila_choc_mix_count=0
fruit_n_nut_cup_count=0
cocolate_magic_count=0
cone_chocolate_count=0
cone_vanila_count=0
heavenly_crunch_count=0
fruit_n_nut_cone_count=0
cappuccino_count=0

def faluda_stick():
    global fluda_stick_count
    fluda_stick_count = fluda_stick_count + 1
    fal_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    fal_Entry.grid(row=12, column=0, padx=8)
    fal_Entry.insert(END, 'Faluda Stick')
    fal_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    fal_qEntry.grid(row=12, column=1, padx=8)
    fal_qEntry.insert(END, f'{fluda_stick_count}')
def remove_faluda_stick():
    global fluda_stick_count
    if fluda_stick_count>0:
        fluda_stick_count = fluda_stick_count - 1
        fal_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        fal_qEntry.grid(row=12, column=1, padx=8)
        fal_qEntry.insert(END, f'{fluda_stick_count}')

def fantastic_stick():
    global fantastick_chocolate_count
    fantastick_chocolate_count = fantastick_chocolate_count + 1
    fantastic_stick_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    fantastic_stick_Entry.grid(row=13, column=0, padx=8)
    fantastic_stick_Entry.insert(END, 'Fantastic Stick')
    fantastic_stick_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    fantastic_stick_qEntry.grid(row=13, column=1, padx=8)
    fantastic_stick_qEntry.insert(END, f'{fantastick_chocolate_count}')
def remove_fantastic_stick():
    global fantastick_chocolate_count
    if fantastick_chocolate_count>0:
        fantastick_chocolate_count = fantastick_chocolate_count - 1
        fantastic_stick_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        fantastic_stick_qEntry.grid(row=13, column=1, padx=8)
        fantastic_stick_qEntry.insert(END, f'{fantastick_chocolate_count}')

def cool_berry():
    global cool_berry_count
    cool_berry_count = cool_berry_count + 1
    cool_berry_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    cool_berry_Entry.grid(row=14, column=0, padx=8)
    cool_berry_Entry.insert(END, 'Cool Berry')
    cool_berry_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    cool_berry_qEntry.grid(row=14, column=1, padx=8)
    cool_berry_qEntry.insert(END, f'{cool_berry_count}')
def remove_cool_berry():
    global cool_berry_count
    if cool_berry_count>0:
        cool_berry_count = cool_berry_count - 1
        cool_berry_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        cool_berry_qEntry.grid(row=14, column=1, padx=8)
        cool_berry_qEntry.insert(END, f'{cool_berry_count}')

def divul():
    global divul_magic_count
    divul_magic_count = divul_magic_count + 1
    divul_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    divul_Entry.grid(row=15, column=0, padx=8)
    divul_Entry.insert(END, 'Divul Magic Stick')
    divul_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    divul_qEntry.grid(row=15, column=1, padx=8)
    divul_qEntry.insert(END, f'{divul_magic_count}')
def remove_divul():
    global divul_magic_count
    if divul_magic_count>0:
        divul_magic_count = divul_magic_count - 1
        divul_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        divul_qEntry.grid(row=15, column=1, padx=8)
        divul_qEntry.insert(END, f'{divul_magic_count}')

def cho_chocolate():
    global choc_chocolate_count
    choc_chocolate_count = choc_chocolate_count + 1
    cho_chocolate_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    cho_chocolate_Entry.grid(row=16, column=0, padx=8)
    cho_chocolate_Entry.insert(END, 'Magic Choc-Chocolate')
    cho_chocolate_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    cho_chocolate_qEntry.grid(row=16, column=1, padx=8)
    cho_chocolate_qEntry.insert(END, f'{choc_chocolate_count}')
def remove_cho_chocolate():
    global choc_chocolate_count
    if choc_chocolate_count>0:
        choc_chocolate_count = choc_chocolate_count - 1
        cho_chocolate_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        cho_chocolate_qEntry.grid(row=16, column=1, padx=8)
        cho_chocolate_qEntry.insert(END, f'{choc_chocolate_count}')

def traffic_light_stick():
    global traffic_light_stick_count
    traffic_light_stick_count = traffic_light_stick_count + 1
    traffic_light_stick_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    traffic_light_stick_Entry.grid(row=17, column=0, padx=8)
    traffic_light_stick_Entry.insert(END, 'Traffic Light Stick')
    traffic_light_stick_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    traffic_light_stick_qEntry.grid(row=17, column=1, padx=8)
    traffic_light_stick_qEntry.insert(END, f'{traffic_light_stick_count}')
def remove_traffic_light_stick():
    global traffic_light_stick_count
    if traffic_light_stick_count>0:
        traffic_light_stick_count = traffic_light_stick_count - 1
        traffic_light_stick_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        traffic_light_stick_qEntry.grid(row=17, column=1, padx=8)
        traffic_light_stick_qEntry.insert(END, f'{traffic_light_stick_count}')

def caramel_bar():
    global caramel_bar_count
    caramel_bar_count = caramel_bar_count + 1
    caramel_bar_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    caramel_bar_Entry.grid(row=18, column=0, padx=8)
    caramel_bar_Entry.insert(END, 'Magic Caramel Bar')
    caramel_bar_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    caramel_bar_qEntry.grid(row=18, column=1, padx=8)
    caramel_bar_qEntry.insert(END, f'{caramel_bar_count}')
def remove_caramel_bar():
    global caramel_bar_count
    if caramel_bar_count>0:
        caramel_bar_count = caramel_bar_count - 1
        caramel_bar_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        caramel_bar_qEntry.grid(row=18, column=1, padx=8)
        caramel_bar_qEntry.insert(END, f'{caramel_bar_count}')

def cube():
    global Magic_Cube_count
    Magic_Cube_count = Magic_Cube_count + 1
    cube_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    cube_Entry.grid(row=19, column=0, padx=8)
    cube_Entry.insert(END, 'Magic Cube')
    cube_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    cube_qEntry.grid(row=19, column=1, padx=8)
    cube_qEntry.insert(END, f'{Magic_Cube_count}')
def remove_cube():
    global Magic_Cube_count
    if Magic_Cube_count>0:
        Magic_Cube_count = Magic_Cube_count - 1
        cube_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        cube_qEntry.grid(row=19, column=1, padx=8)
        cube_qEntry.insert(END, f'{Magic_Cube_count}')

def vanila_magic():
    global vanila_magic_count
    vanila_magic_count = vanila_magic_count + 1
    vanila_magic_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    vanila_magic_Entry.grid(row=20, column=0, padx=8)
    vanila_magic_Entry.insert(END, 'Vanila Magic')
    vanila_magic_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    vanila_magic_qEntry.grid(row=20, column=1, padx=8)
    vanila_magic_qEntry.insert(END, f'{vanila_magic_count}')
def remove_vanila_magic():
    global vanila_magic_count
    if vanila_magic_count>0:
        vanila_magic_count = vanila_magic_count - 1
        vanila_magic_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        vanila_magic_qEntry.grid(row=20, column=1, padx=8)
        vanila_magic_qEntry.insert(END, f'{vanila_magic_count}')

def kithul_magic():
    global kithul_magic_count
    kithul_magic_count = kithul_magic_count + 1
    kithul_magic_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    kithul_magic_Entry.grid(row=21, column=0, padx=8)
    kithul_magic_Entry.insert(END, 'Kithul Magic')
    kithul_magic_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    kithul_magic_qEntry.grid(row=21, column=1, padx=8)
    kithul_magic_qEntry.insert(END, f'{kithul_magic_count}')
def remove_kithul_magic():
    global kithul_magic_count
    if kithul_magic_count>0:
        kithul_magic_count = kithul_magic_count - 1
        kithul_magic_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        kithul_magic_qEntry.grid(row=21, column=1, padx=8)
        kithul_magic_qEntry.insert(END, f'{kithul_magic_count}')

def vanila_choc_mix():
    global vanila_choc_mix_count
    vanila_choc_mix_count = vanila_choc_mix_count + 1
    vanila_choc_mix_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    vanila_choc_mix_Entry.grid(row=22, column=0, padx=8)
    vanila_choc_mix_Entry.insert(END, 'Vanuila Choc-Mix')
    vanila_choc_mix_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    vanila_choc_mix_qEntry.grid(row=22, column=1, padx=8)
    vanila_choc_mix_qEntry.insert(END, f'{vanila_choc_mix_count}')
def remove_vanila_choc_mix():
    global vanila_choc_mix_count
    if vanila_choc_mix_count>0:
        vanila_choc_mix_count = vanila_choc_mix_count - 1
        vanila_choc_mix_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        vanila_choc_mix_qEntry.grid(row=22, column=1, padx=8)
        vanila_choc_mix_qEntry.insert(END, f'{vanila_choc_mix_count}')

def fruit_n_nut_cup():
    global fruit_n_nut_cup_count
    fruit_n_nut_cup_count = fruit_n_nut_cup_count + 1
    fruit_n_nut_cup_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    fruit_n_nut_cup_Entry.grid(row=23, column=0, padx=8)
    fruit_n_nut_cup_Entry.insert(END, 'Fruit & Nut Cup')
    fruit_n_nut_cup_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    fruit_n_nut_cup_qEntry.grid(row=23, column=1, padx=8)
    fruit_n_nut_cup_qEntry.insert(END, f'{fruit_n_nut_cup_count}')
def remove_fruit_n_nut_cup():
    global fruit_n_nut_cup_count
    if fruit_n_nut_cup_count>0:
        fruit_n_nut_cup_count = fruit_n_nut_cup_count - 1
        fruit_n_nut_cup_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        fruit_n_nut_cup_qEntry.grid(row=23, column=1, padx=8)
        fruit_n_nut_cup_qEntry.insert(END, f'{fruit_n_nut_cup_count}')

def chocolate_magic():
    global cocolate_magic_count
    cocolate_magic_count = cocolate_magic_count + 1
    cocolate_magic_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    cocolate_magic_Entry.grid(row=24, column=0, padx=8)
    cocolate_magic_Entry.insert(END, 'Chocolate Magic')
    cocolate_magic_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    cocolate_magic_qEntry.grid(row=24, column=1, padx=8)
    cocolate_magic_qEntry.insert(END, f'{cocolate_magic_count}')
def remove_chocolate_magic():
    global cocolate_magic_count
    if cocolate_magic_count>0:
        cocolate_magic_count = cocolate_magic_count - 1
        cocolate_magic_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        cocolate_magic_qEntry.grid(row=24, column=1, padx=8)
        cocolate_magic_qEntry.insert(END, f'{cocolate_magic_count}')

def cone_chocolate():
    global cone_chocolate_count
    cone_chocolate_count = cone_chocolate_count + 1
    cone_chocolate_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    cone_chocolate_Entry.grid(row=25, column=0, padx=8)
    cone_chocolate_Entry.insert(END, 'Magic Cone Chocolate')
    cone_chocolate_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    cone_chocolate_qEntry.grid(row=25, column=1, padx=8)
    cone_chocolate_qEntry.insert(END, f'{cone_chocolate_count}')
def remove_cone_chocolate():
    global cone_chocolate_count
    if cone_chocolate_count>0:
        cone_chocolate_count = cone_chocolate_count - 1
        cone_chocolate_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        cone_chocolate_qEntry.grid(row=25, column=1, padx=8)
        cone_chocolate_qEntry.insert(END, f'{cone_chocolate_count}')

def cone_vanila():
    global cone_vanila_count
    cone_vanila_count = cone_vanila_count + 1
    cone_vanila_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    cone_vanila_Entry.grid(row=26, column=0, padx=8)
    cone_vanila_Entry.insert(END, 'Magic Cone Vanila')
    cone_vanila_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    cone_vanila_qEntry.grid(row=26, column=1, padx=8)
    cone_vanila_qEntry.insert(END, f'{cone_vanila_count}')
def remove_cone_vanila():
    global cone_vanila_count
    if cone_vanila_count>0:
        cone_vanila_count = cone_vanila_count - 1
        cone_vanila_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        cone_vanila_qEntry.grid(row=26, column=1, padx=8)
        cone_vanila_qEntry.insert(END, f'{cone_vanila_count}')

def heavenly_crunch():
    global heavenly_crunch_count
    heavenly_crunch_count = heavenly_crunch_count + 1
    heavenly_crunch_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    heavenly_crunch_Entry.grid(row=27, column=0, padx=8)
    heavenly_crunch_Entry.insert(END, 'Heavenly Crunch Cone')
    heavenly_crunch_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    heavenly_crunch_qEntry.grid(row=27, column=1, padx=8)
    heavenly_crunch_qEntry.insert(END, f'{heavenly_crunch_count}')
def remove_heavenly_crunch():
    global heavenly_crunch_count
    if heavenly_crunch_count>0:
        heavenly_crunch_count = heavenly_crunch_count - 1
        heavenly_crunch_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        heavenly_crunch_qEntry.grid(row=27, column=1, padx=8)
        heavenly_crunch_qEntry.insert(END, f'{heavenly_crunch_count}')

def fruit_n_nut_cone():
    global fruit_n_nut_cone_count
    fruit_n_nut_cone_count = fruit_n_nut_cone_count + 1
    fruit_n_nut_cone_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    fruit_n_nut_cone_Entry.grid(row=28, column=0, padx=8)
    fruit_n_nut_cone_Entry.insert(END, 'Fruit and Nut Cone')
    fruit_n_nut_cone_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    fruit_n_nut_cone_qEntry.grid(row=28, column=1, padx=8)
    fruit_n_nut_cone_qEntry.insert(END, f'{fruit_n_nut_cone_count}')
def remove_fruit_n_nut_cone():
    global fruit_n_nut_cone_count
    if fruit_n_nut_cone_count>0:
        fruit_n_nut_cone_count = fruit_n_nut_cone_count - 1
        fruit_n_nut_cone_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        fruit_n_nut_cone_qEntry.grid(row=28, column=1, padx=8)
        fruit_n_nut_cone_qEntry.insert(END, f'{fruit_n_nut_cone_count}')

def cappuccino():
    global cappuccino_count
    cappuccino_count = cappuccino_count + 1
    cappuccino_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    cappuccino_Entry.grid(row=29, column=0, padx=8)
    cappuccino_Entry.insert(END, 'Cappuccino Cone')
    cappuccino_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    cappuccino_qEntry.grid(row=29, column=1, padx=8)
    cappuccino_qEntry.insert(END, f'{cappuccino_count}')
def remove_cappuccino():
    global cappuccino_count
    if cappuccino_count>0:
        cappuccino_count = cappuccino_count - 1
        cappuccino_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        cappuccino_qEntry.grid(row=29, column=1, padx=8)
        cappuccino_qEntry.insert(END, f'{cappuccino_count}')

# -----------drinks functions----------

water_count=0
ginger_tea_count=0

def water():
    global water_count
    water_count = water_count + 1
    water_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    water_Entry.grid(row=30, column=0, padx=8)
    water_Entry.insert(END, 'Water Bottle')
    water_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    water_qEntry.grid(row=30, column=1, padx=8)
    water_qEntry.insert(END, f'{water_count}')
def remove_water():
    global water_count
    if water_count>0:
        water_count = water_count - 1
        water_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        water_qEntry.grid(row=30, column=1, padx=8)
        water_qEntry.insert(END, f'{water_count}')

def ginger_tea():
    global ginger_tea_count
    ginger_tea_count = ginger_tea_count + 1
    ginger_tea_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    ginger_tea_Entry.grid(row=31, column=0, padx=8)
    ginger_tea_Entry.insert(END, 'Ginger Tea')
    ginger_tea_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    ginger_tea_qEntry.grid(row=31, column=1, padx=8)
    ginger_tea_qEntry.insert(END, f'{ginger_tea_count}')
def remove_ginger_tea():
    global ginger_tea_count
    if ginger_tea_count>0:
        ginger_tea_count = ginger_tea_count - 1
        ginger_tea_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        ginger_tea_qEntry.grid(row=31, column=1, padx=8)
        ginger_tea_qEntry.insert(END, f'{ginger_tea_count}')

# -----------other functions----------

rotti_count=0

def rotti():
    global rotti_count
    rotti_count = rotti_count + 1
    rotti_Entry = Entry(textarea, font=('arial', 15), bd=0, width=25)
    rotti_Entry.grid(row=32, column=0, padx=8)
    rotti_Entry.insert(END, 'Rotti')
    rotti_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
    rotti_qEntry.grid(row=32, column=1, padx=8)
    rotti_qEntry.insert(END, f'{rotti_count}')
def remove_rotti():
    global rotti_count
    if rotti_count>0:
        rotti_count = rotti_count - 1
        rotti_qEntry = Entry(textarea, font=('arial', 15), bd=0, width=6)
        rotti_qEntry.grid(row=32, column=1, padx=8)
        rotti_qEntry.insert(END, f'{rotti_count}')

def clear():
    textarea.delete("0.0","32.0")


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
dashImage=ImageTk.PhotoImage(file='dashboard_bg.jpg')
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
totalButton = Button(dash_window,text='Total',font=('Gilroy',14,'bold'), bd=0, width=12, height=2, bg=ButtonBG, fg='snow', activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2', command=total)
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
clearButton = Button(dash_window,text='Clear',font=('Gilroy',14,'bold'), bd=0, width=12, height=2, bg=ButtonBG, fg='snow', activebackground='NavajoWhite4', activeforeground=Headbg, cursor='hand2', command=clear)
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
mycanvas.create_window((0,298), window=shortsframe, anchor="nw")

mealsframe = Frame(mycanvas)
mycanvas.create_window((0,682), window=mealsframe, anchor="nw")

normal_icecreamframe = Frame(mycanvas)
mycanvas.create_window((0,895), window=normal_icecreamframe, anchor="nw")

magic_icecreamframe = Frame(mycanvas)
mycanvas.create_window((0,1195), window=magic_icecreamframe, anchor="nw")

drinks_frame = Frame(mycanvas)
mycanvas.create_window((0,2785), window=drinks_frame, anchor="nw")

other_frame = Frame(mycanvas)
mycanvas.create_window((0,3000), window=other_frame, anchor="nw")

wrapper1.place(x=180,y=220)

# burger section
chicken_burger_title_label = Label(burgerframe, text='  BURGERS', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
chicken_burger_title_label.grid(row=0, column=0, columnspan=3, sticky=W)

chiken_burger_Logo = PhotoImage(file='Burger.png')
chiken_burger_label = Label(burgerframe,image=chiken_burger_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow')
chiken_burger_label.grid(row=1,column=0)
chicken_burger_Button = Button(burgerframe, text='Chicken Burger', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command = chicken_burger)
chicken_burger_Button.grid(row=1,column=1)
chicken_burger_Button = Button(burgerframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command = remove_chicken_burger)
chicken_burger_Button.grid(row=1,column=2)

prawn_burger_Logo = PhotoImage(file='Burger.png')
prawn_burger_label = Label(burgerframe,image=prawn_burger_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow')
prawn_burger_label.grid(row=2,column=0)
prawn_burger_Button = Button(burgerframe, text='Prawn Burger', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command = prawn_burger)
prawn_burger_Button.grid(row=2,column=1)
prawn_burger_Button = Button(burgerframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command = remove_prawn_burger)
prawn_burger_Button.grid(row=2,column=2)

cheese_burger_Logo = PhotoImage(file='Burger.png')
cheese_burger_label = Label(burgerframe,image=cheese_burger_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow')
cheese_burger_label.grid(row=3,column=0)
cheese_burger_Button = Button(burgerframe, text='Cheese Burger', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command = cheese_burger)
cheese_burger_Button.grid(row=3,column=1)
cheese_burger_Button = Button(burgerframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command = remove_cheese_burger)
cheese_burger_Button.grid(row=3,column=2)

# short-eats section

short_eats_title_label = Label(shortsframe, text='  SHORT EATS', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
short_eats_title_label.grid(row=0, column=0, columnspan=3, sticky=W)

hotdog_Logo = PhotoImage(file='hotdog.png')
hotdog_label = Label(shortsframe,image=hotdogLogo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow', cursor='hand2')
hotdog_label.grid(row=1,column=0)
hotdog_Button = Button(shortsframe, text='Hotdog', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', command = hotdog)
hotdog_Button.grid(row=1,column=1)
hotdog_Button = Button(shortsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command = remove_hotdog)
hotdog_Button.grid(row=1,column=2)

fish_bun_Logo = PhotoImage(file='fish bun.png')
fish_bun_label = Label(shortsframe,image=fish_bun_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow', cursor='hand2')
fish_bun_label.grid(row=2,column=0)
fish_bun_Button = Button(shortsframe, text='Fish Bun', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', command = fishbun)
fish_bun_Button.grid(row=2,column=1)
fish_bun_Button = Button(shortsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command = remove_fishbun)
fish_bun_Button.grid(row=2,column=2)

pastry_Logo = PhotoImage(file='pastry.png')
pastry_label = Label(shortsframe,image=pastry_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow', cursor='hand2')
pastry_label.grid(row=3,column=0)
pastry_Button = Button(shortsframe, text='Pastry', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', command = pastry)
pastry_Button.grid(row=3,column=1)
pastry_Button = Button(shortsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command = remove_pastry)
pastry_Button.grid(row=3,column=2)

egg_bun_Logo = PhotoImage(file='eggbun.png')
egg_bun_label = Label(shortsframe,image=egg_bun_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow', cursor='hand2')
egg_bun_label.grid(row=4,column=0)
egg_bun_Button = Button(shortsframe, text='Egg Bun', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', command = egg_bun)
egg_bun_Button.grid(row=4,column=1)
egg_bun_Button = Button(shortsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command = remove_egg_bun)
egg_bun_Button.grid(row=4,column=2)

# meals section

meals_title_label = Label(mealsframe, text='  MEALS', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
meals_title_label.grid(row=0, column=0, columnspan=3, sticky=W)

vegi_meal_Logo = PhotoImage(file='Biriyani.png')
vegi_meal_label = Label(mealsframe,image=vegi_meal_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow', cursor='hand2')
vegi_meal_label.grid(row=1,column=0)
vegi_meal_Button = Button(mealsframe, text='Vegi Meal', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', command = vegi_meal)
vegi_meal_Button.grid(row=1,column=1)
vegi_meal_Button = Button(mealsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command = remove_vegi_meal)
vegi_meal_Button.grid(row=1,column=2)

chicken_meal_Logo = PhotoImage(file='Biriyani.png')
chicken_meal_label = Label(mealsframe,image=chicken_meal_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow', cursor='hand2')
chicken_meal_label.grid(row=2,column=0)
chicken_meal_Button = Button(mealsframe, text='Chicken Meal', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', command = chicken_meal)
chicken_meal_Button.grid(row=2,column=1)
chicken_meal_Button = Button(mealsframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command = remove_chicken_meal)
chicken_meal_Button.grid(row=2,column=2)

# normal ice cream section

ice_cream_label = Label(normal_icecreamframe, text='  NORMAL ICE-CREAM', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
ice_cream_label.grid(row=0, column=0, columnspan=3, sticky=W)

vanila_icecream_Logo = PhotoImage(file='Ice Cream.png')
vanila_icecream_label = Label(normal_icecreamframe,image=vanila_icecream_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow', cursor='hand2')
vanila_icecream_label.grid(row=1,column=0)
vanila_icecream_Button = Button(normal_icecreamframe, text='Vanila Ice-Cream', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', command=vanila_icecream)
vanila_icecream_Button.grid(row=1,column=1)
vanila_icecream_Button = Button(normal_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_vanila_icecream)
vanila_icecream_Button.grid(row=1,column=2)

chocolate_icecream_Logo = PhotoImage(file='Cohocolate Icecream.png')
chocolate_icecream_label = Label(normal_icecreamframe,image=chocolate_icecream_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow', cursor='hand2')
chocolate_icecream_label.grid(row=2,column=0)
chocolate_icecream_Button = Button(normal_icecreamframe, text='Chocolate Ice-Cream', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', command=chocolate_icecream)
chocolate_icecream_Button.grid(row=2,column=1)
chocolate_icecream_Button = Button(normal_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_chocolate_icecream)
chocolate_icecream_Button.grid(row=2,column=2)

strawberry_icecream_Logo = PhotoImage(file='strawberry icecream.png')
strawberry_icecream_label = Label(normal_icecreamframe,image=strawberry_icecream_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow', fg='snow', cursor='hand2')
strawberry_icecream_label.grid(row=3,column=0)
strawberry_icecream_Button = Button(normal_icecreamframe, text='Strawberry Ice-Cream', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', command=strawberry_icecream)
strawberry_icecream_Button.grid(row=3,column=1)
strawberry_icecream_Button = Button(normal_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_strawberry_icecream)
strawberry_icecream_Button.grid(row=3,column=2)

# magic ice cream section

magic_ice_cream_label = Label(magic_icecreamframe, text='  MAGIC ICE-CREAM', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
magic_ice_cream_label.grid(row=0, column=0, columnspan=3, sticky=W)

faluda_stick_Logo = PhotoImage(file='Cargils_magic.png')
faluda_stick_label = Label(magic_icecreamframe,image=faluda_stick_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
faluda_stick_label.grid(row=1,column=0)
faluda_stick_Button = Button(magic_icecreamframe, text='Faluda Stick', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=faluda_stick)
faluda_stick_Button.grid(row=1,column=1)
faluda_stick_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_faluda_stick)
faluda_stick_Button.grid(row=1,column=2)

fantasticstick_chocolate_Logo = PhotoImage(file='Cargils_magic.png')
fantasticstick_chocolate_label = Label(magic_icecreamframe,image=fantasticstick_chocolate_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
fantasticstick_chocolate_label.grid(row=2,column=0)
fantasticstick_chocolate_Button = Button(magic_icecreamframe, text='Fantasticstick-Chocolate', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=fantastic_stick)
fantasticstick_chocolate_Button.grid(row=2,column=1)
fantasticstick_chocolate_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_fantastic_stick)
fantasticstick_chocolate_Button.grid(row=2,column=2)

cool_berry_Logo = PhotoImage(file='Cargils_magic.png')
cool_berry_label = Label(magic_icecreamframe,image=cool_berry_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
cool_berry_label.grid(row=3,column=0)
cool_berry_Button = Button(magic_icecreamframe, text='Cool Berry', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=cool_berry)
cool_berry_Button.grid(row=3,column=1)
cool_berry_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_cool_berry)
cool_berry_Button.grid(row=3,column=2)

divul_magic_stick_Logo = PhotoImage(file='Cargils_magic.png')
divul_magic_stick_label = Label(magic_icecreamframe,image=divul_magic_stick_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
divul_magic_stick_label.grid(row=4,column=0)
divul_magic_stick_Button = Button(magic_icecreamframe, text='Divul Magic Stick', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=divul)
divul_magic_stick_Button.grid(row=4,column=1)
divul_magic_stick_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_divul)
divul_magic_stick_Button.grid(row=4,column=2)

magic_choc_chocolate_Logo = PhotoImage(file='Cargils_magic.png')
magic_choc_chocolate_label = Label(magic_icecreamframe,image=magic_choc_chocolate_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
magic_choc_chocolate_label.grid(row=5,column=0)
magic_choc_chocolate_Button = Button(magic_icecreamframe, text='Magic Choc-Chocolate', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=cho_chocolate)
magic_choc_chocolate_Button.grid(row=5,column=1)
magic_choc_chocolate_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_cho_chocolate)
magic_choc_chocolate_Button.grid(row=5,column=2)

traffic_light_stick_Logo = PhotoImage(file='Cargils_magic.png')
traffic_light_stick_label = Label(magic_icecreamframe,image=traffic_light_stick_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
traffic_light_stick_label.grid(row=6,column=0)
traffic_light_stick_Button = Button(magic_icecreamframe, text='Traffic Light Stick', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=traffic_light_stick)
traffic_light_stick_Button.grid(row=6,column=1)
traffic_light_stick_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_traffic_light_stick)
traffic_light_stick_Button.grid(row=6,column=2)

magic_caramel_bar_Logo = PhotoImage(file='Cargils_magic.png')
magic_caramel_bar_label = Label(magic_icecreamframe,image=magic_caramel_bar_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
magic_caramel_bar_label.grid(row=7,column=0)
magic_caramel_bar_Button = Button(magic_icecreamframe, text='Magic Caramel Bar', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=caramel_bar)
magic_caramel_bar_Button.grid(row=7,column=1)
magic_caramel_bar_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_caramel_bar)
magic_caramel_bar_Button.grid(row=7,column=2)

magic_cube_Logo = PhotoImage(file='Cargils_magic.png')
magic_cube_label = Label(magic_icecreamframe,image=magic_cube_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
magic_cube_label.grid(row=8,column=0)
magic_cube_Button = Button(magic_icecreamframe, text='Magic Cube', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=cube)
magic_cube_Button.grid(row=8,column=1)
magic_cube_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_cube)
magic_cube_Button.grid(row=8,column=2)

vanila_magic_Logo = PhotoImage(file='Cargils_magic.png')
vanila_magic_label = Label(magic_icecreamframe,image=vanila_magic_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
vanila_magic_label.grid(row=9,column=0)
vanila_magic_Button = Button(magic_icecreamframe, text='Vanila Magic', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=vanila_magic)
vanila_magic_Button.grid(row=9,column=1)
vanila_magic_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_vanila_magic)
vanila_magic_Button.grid(row=9,column=2)

kithul_magic_Logo = PhotoImage(file='Cargils_magic.png')
kithul_magic_label = Label(magic_icecreamframe,image=kithul_magic_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
kithul_magic_label.grid(row=10,column=0)
kithul_magic_Button = Button(magic_icecreamframe, text='Kithul Magic', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=kithul_magic)
kithul_magic_Button.grid(row=10,column=1)
kithul_magic_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_kithul_magic)
kithul_magic_Button.grid(row=10,column=2)

vanila_chock_mix_Logo = PhotoImage(file='Cargils_magic.png')
vanila_chock_mix_label = Label(magic_icecreamframe,image=vanila_chock_mix_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
vanila_chock_mix_label.grid(row=11,column=0)
vanila_chock_mix_Button = Button(magic_icecreamframe, text='Vanila Chock-Mix', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=vanila_choc_mix)
vanila_chock_mix_Button.grid(row=11,column=1)
vanila_chock_mix_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_vanila_choc_mix)
vanila_chock_mix_Button.grid(row=11,column=2)

fruit_and_nut_cup_Logo = PhotoImage(file='Cargils_magic.png')
fruit_and_nut_cup_label = Label(magic_icecreamframe,image=fruit_and_nut_cup_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
fruit_and_nut_cup_label.grid(row=12,column=0)
fruit_and_nut_cup_Button = Button(magic_icecreamframe, text='Fruit & Nut-Cup', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=fruit_n_nut_cup)
fruit_and_nut_cup_Button.grid(row=12,column=1)
fruit_and_nut_cup_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_fruit_n_nut_cup)
fruit_and_nut_cup_Button.grid(row=12,column=2)

chocolate_magic_Logo = PhotoImage(file='Cargils_magic.png')
chocolate_magic_label = Label(magic_icecreamframe,image=chocolate_magic_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
chocolate_magic_label.grid(row=13,column=0)
chocolate_magic_Button = Button(magic_icecreamframe, text='Chocolate Magic', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=chocolate_magic)
chocolate_magic_Button.grid(row=13,column=1)
chocolate_magic_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_chocolate_magic)
chocolate_magic_Button.grid(row=13,column=2)

magic_cone_chocolate_Logo = PhotoImage(file='Cargils_magic.png')
magic_cone_chocolate_label = Label(magic_icecreamframe,image=magic_cone_chocolate_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
magic_cone_chocolate_label.grid(row=14,column=0)
magic_cone_chocolate_Button = Button(magic_icecreamframe, text='Magic Cone-Chocolate', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=cone_chocolate)
magic_cone_chocolate_Button.grid(row=14,column=1)
magic_cone_chocolate_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_cone_chocolate)
magic_cone_chocolate_Button.grid(row=14,column=2)

magic_cone_vanila_Logo = PhotoImage(file='Cargils_magic.png')
magic_cone_vanila_label = Label(magic_icecreamframe,image=magic_cone_vanila_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
magic_cone_vanila_label.grid(row=15,column=0)
magic_cone_vanila_Button = Button(magic_icecreamframe, text='Magic Cone-Vanila', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=cone_vanila)
magic_cone_vanila_Button.grid(row=15,column=1)
magic_cone_vanila_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_cone_vanila)
magic_cone_vanila_Button.grid(row=15,column=2)

heavenly_crunch_cone_Logo = PhotoImage(file='Cargils_magic.png')
heavenly_crunch_cone_label = Label(magic_icecreamframe,image=heavenly_crunch_cone_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
heavenly_crunch_cone_label.grid(row=16,column=0)
heavenly_crunch_cone_Button = Button(magic_icecreamframe, text='Heavenly Crunch Cone', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=heavenly_crunch)
heavenly_crunch_cone_Button.grid(row=16,column=1)
heavenly_crunch_cone_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_heavenly_crunch)
heavenly_crunch_cone_Button.grid(row=16,column=2)

fruit_and_nut_cone_Logo = PhotoImage(file='Cargils_magic.png')
fruit_and_nut_cone_label = Label(magic_icecreamframe,image=fruit_and_nut_cone_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
fruit_and_nut_cone_label.grid(row=17,column=0)
fruit_and_nut_cone_Button = Button(magic_icecreamframe, text='Fruit & Nut Cone', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=fruit_n_nut_cone)
fruit_and_nut_cone_Button.grid(row=17,column=1)
fruit_and_nut_cone_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_fruit_n_nut_cone)
fruit_and_nut_cone_Button.grid(row=17,column=2)

cappuccino_cone_Logo = PhotoImage(file='Cargils_magic.png')
cappuccino_cone_label = Label(magic_icecreamframe,image=cappuccino_cone_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
cappuccino_cone_label.grid(row=18,column=0)
cappuccino_cone_Button = Button(magic_icecreamframe, text='Cappuccino Cone', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=cappuccino)
cappuccino_cone_Button.grid(row=18,column=1)
cappuccino_cone_Button = Button(magic_icecreamframe,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_cappuccino)
cappuccino_cone_Button.grid(row=18,column=2)


# drinks section

drinks_label = Label(drinks_frame, text='  Drinks', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
drinks_label.grid(row=0, column=0, columnspan=3, sticky=W)

water_Logo = PhotoImage(file='Water.png')
water_label = Label(drinks_frame,image=water_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
water_label.grid(row=1,column=0)
water_Button = Button(drinks_frame, text='Water Bottle', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=water)
water_Button.grid(row=1,column=1)
water_Button = Button(drinks_frame,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_water)
water_Button.grid(row=1,column=2)

ginger_tea_Logo = PhotoImage(file='Tea.png')
ginger_tea_label = Label(drinks_frame,image=ginger_tea_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
ginger_tea_label.grid(row=2,column=0)
ginger_tea_Button = Button(drinks_frame, text='Ginger Tea', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=ginger_tea)
ginger_tea_Button.grid(row=2,column=1)
ginger_tea_Button = Button(drinks_frame,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_ginger_tea)
ginger_tea_Button.grid(row=2,column=2)

# other section

other_label = Label(other_frame, text='  Other', font=('Gilroy',13,'bold'), justify="left", anchor="w", width=45, height=2, bd=0, relief=GROOVE, bg='snow', fg='gray')
other_label.grid(row=0, column=0, columnspan=3, sticky=W)

rotti_Logo = PhotoImage(file='Rotti.png')
rotti_label = Label(other_frame,image=rotti_Logo,font=('Gilroy',16,'bold'), width=95,height=85, bd=0, bg='snow')
rotti_label.grid(row=1,column=0)
rotti_Button = Button(other_frame, text='Rotti', font=('Gilroy',15,'bold'), width=22, height=3, bd=0, relief=GROOVE, bg='snow', fg=Headfg, activeforeground='gray', cursor='hand2', command=rotti)
rotti_Button.grid(row=1,column=1)
rotti_Button = Button(other_frame,text='Remove',font=('Gilroy',12,'bold'), width=8,height=3, bd=0, bg='red', fg='snow', cursor='hand2', command=remove_rotti)
rotti_Button.grid(row=1,column=2)

# set the scrollbar comparatively to the text
scrollbar.config(command=mycanvas.yview)


# --------Bill Area--------


bill_area_Label = Label(dash_window, text='Bill Area', font=('Gilroy',15,'bold'), bd=0,relief=GROOVE, bg=Headbg, fg='snow')
bill_area_Label.place(x=680,y=180)

billFrame = Frame(dash_window, relief=GROOVE)
billFrame.place(x=680,y=220)

# to add a scrollbar, use 'Scrollbar()' class. Use orient to to make vertical or horizontal scrollbar
scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# to create a text area, use 'text()' class. To set the scrollbar with the text area, use 'yscrollcommand=scrollbar.set' command.
textarea = Text(billFrame, height=10, width=45, yscrollcommand=scrollbar.set)
textarea.pack()

#set the scrollbar comparatively to the text
scrollbar.config(command=textarea.yview)



# total price
total_price_Label = Label(dash_window, text='Total Price :', font=('Gilroy',15,'bold'), bd=0, relief=GROOVE, bg=Headbg, fg='snow')
total_price_Label.place(x=700,y=645)
total_price_Entry = Entry(dash_window, font=('arial', 15), bd=0, width=15)
total_price_Entry.place(x=850,y=645)
#unit_Label = Label(dash_window, text='Rs.', font=('Gilroy',14,'bold'), bd=0, relief=GROOVE, bg='white', fg=Headbg)
#unit_Label.place(x=980,y=645)

#scrollbar.config(command=l1.yview)

dash_window.mainloop()