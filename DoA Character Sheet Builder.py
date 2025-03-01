"""

Author:  J. Clayton Graham
Date written: -/--/25
Assignment:   Module 
Short Desc:   

"""

#Imports and Constants
import tkinter as tk
from tkinter import Toplevel, StringVar, IntVar
from PIL import Image, ImageTk


#Checks if Stats are valid.
def Check_Character():
    if False:
        return Show_Error()
    else:
        return Show_Page()

#The Character Sheet
def Show_Page():
    print(name_entry.get())
    print(upskill_text.get("1.0", "end-1c"))
    
    Page_Window = tk.Toplevel()
    Page_Window.title("Character Sheet")
    Page_Window.geometry("1100x850")
    Page_Window.configure(bg='black')
    Page_Window.resizable(False, False)

    att_box = tk.Label(Page_Window, height=15, width=50, bg="white")
    att_box.grid(row = 0, column = 0, pady = 1, padx = 1)
    uti_box = tk.Label(Page_Window, height=15, width=50, bg="white")
    uti_box.grid(row = 0, column = 1, pady = 1, padx = 1)
    def_box = tk.Label(Page_Window, height=15, width=50, bg="white")
    def_box.grid(row = 0, column = 2, pady = 1, padx = 1)

    attnum_box = tk.Label(Page_Window, height=3, width=50, bg="white", text=("Attack: " + att_entry.get()))
    attnum_box.grid(row = 1, column = 0, pady = 1, padx = 1)
    utinum_box = tk.Label(Page_Window, height=3, width=50, bg="white", text=("Utility: " + uti_entry.get()))
    utinum_box.grid(row = 1, column = 1, pady = 1, padx = 1)
    defnum_box = tk.Label(Page_Window, height=3, width=50, bg="white", text=("Defense: " + def_entry.get()))
    defnum_box.grid(row = 1, column = 2, pady = 1, padx = 1)

    #Calculate the Fill Box contents
    evadestat = 0
    dicestat = 0
    vigilstat = 0
    fillstats = "Name: " + name_entry.get() +  "\nClass: " + class_entry.get() + "\nProfession: " + prof_entry.get()
    

    FillBox_box = tk.Label(Page_Window, height=5, width=50, bg="white", text=fillstats)
    FillBox_box.grid(row = 2, column = 0, pady = 1, padx = 1)
    

    try:

        main_img = Image.open("C:/Users/bxbgr/OneDrive/Documents/Final Project/Main logo.png").resize((100, 150), Image.LANCZOS)
        main_photo = ImageTk.PhotoImage(main_img)
        
        hp_img = Image.open("C:/Users/bxbgr/OneDrive/Documents/Final Project/HP Pic.png").resize((100, 150), Image.LANCZOS)
        hp_photo = ImageTk.PhotoImage(hp_img)

        bag_img = Image.open("C:/Users/bxbgr/OneDrive/Documents/Final Project/Bag pic.png").resize((100, 150), Image.LANCZOS)
        bag_photo = ImageTk.PhotoImage(bag_img)
            
        img_Label_main = tk.Label(Page_Window, image=main_photo)
        img_Label_main.image = main_photo
        img_Label_main.grid(row = 2, column = 1, pady = 2, sticky="nsew")
            
        img_Label_hp = tk.Label(Page_Window, image=hp_photo)
        img_Label_hp.image = hp_photo
        img_Label_hp.grid(row = 2, column = 2, pady = 2, sticky="nsew", rowspan=2)

        img_Label_bag = tk.Label(Page_Window, image=bag_photo)
        img_Label_bag.image = bag_photo
        img_Label_bag.grid(row = 3, column = 0, pady = 2, sticky="nsew")

    except FileNotFoundError:
        img_Label_main = tk.Label(Page_Window, text="Image not Found!", fg="red")
        img_Label_main.grid(row = 2, column = 1, pady = 2)

        img_Label_hp = tk.Label(Page_Window, text="Image not Found!", fg="red")
        img_Label_hp.grid(row = 2, column = 2, pady = 2, columnspan=2)

        img_Label_bag = tk.Label(Page_Window, text="Image not Found!", fg="red")
        img_Label_bag.grid(row = 3, column = 0, pady = 2)

    #Calculate Skills
    skilltext = ""

    skill_box = tk.Label(Page_Window, height=12, width=50, bg="white", text=skilltext)
    skill_box.grid(row = 3, column = 1, pady = 1, padx = 1)
        



#Error Page
def Show_Error():
    print ("Error")


###Main Window Starts Here
###Main Window Starts Here
###Main Window Starts Here

Char_Window = tk.Tk()
Char_Window.title("DoA Character Sheet Builder")
Char_Window.configure(bg='grey')
Char_Window.resizable(False, False)


try:
    img = Image.open("C:/Users/bxbgr/OneDrive/Documents/Final Project/MainPic.png").resize((100, 150), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    
    img_Label_one = tk.Label(Char_Window, image=photo)
    img_Label_one.image = photo
    img_Label_one.grid(row = 0, column = 0, pady = 2)

    img_Label_two = tk.Label(Char_Window, image=photo)
    img_Label_two.image = photo
    img_Label_two.grid(row = 0, column = 2, pady = 2)
except FileNotFoundError:
    img_Label_one = tk.Label(Char_Window, text="Image not Found!", fg="red")
    img_Label_one.grid(row = 0, column = 0, pady = 2)

    img_Label_two = tk.Label(Char_Window, text="Image not Found!", fg="red")
    img_Label_two.grid(row = 0, column = 2, pady = 2)


intro_label = tk.Label(Char_Window, text="Howdy Partner, What type of Adventurer are you?")
intro_label.grid(row = 0, column = 1, pady = 2)

name_label = tk.Label(Char_Window, text="Your Name:")
name_label.grid(row = 1, column = 1, pady = 2)
name_entry = tk.Entry(Char_Window)
name_entry.grid(row = 2, column = 1, pady = 2)

class_label = tk.Label(Char_Window, text="Your Class:")
class_label.grid(row = 3, column = 1, pady = 2)
class_entry = tk.Entry(Char_Window)
class_entry.grid(row = 4, column = 1, pady = 2)

prof_label = tk.Label(Char_Window, text="Profession:")
prof_label.grid(row = 5, column = 1, pady = 2)
prof_entry = tk.Entry(Char_Window)
prof_entry.grid(row = 6, column = 1, pady = 2)

att_label = tk.Label(Char_Window, text="Attack:")
att_label.grid(row = 7, column = 0, pady = 2)
att_entry = tk.Entry(Char_Window)
att_entry.grid(row = 8, column = 0, pady = 2)

uti_label = tk.Label(Char_Window, text="Utility:")
uti_label.grid(row = 7, column = 1, pady = 2)
uti_entry = tk.Entry(Char_Window)
uti_entry.grid(row = 8, column = 1, pady = 2)

def_label = tk.Label(Char_Window, text="Defence:")
def_label.grid(row = 7, column = 2, pady = 2)
def_entry = tk.Entry(Char_Window)
def_entry.grid(row = 8, column = 2, pady = 2)

bskill_label = tk.Label(Char_Window, text="Base Skill Level:")
bskill_label.grid(row = 9, column = 0, pady = 2, columnspan = 3)
bskill_text = tk.Text(Char_Window, height=5)
bskill_text.grid(row = 10, column = 0, pady = 2, columnspan = 3, sticky = 'NSEW')

upskill_label = tk.Label(Char_Window, text="Skill Upgrades:")
upskill_label.grid(row = 11, column = 0, pady = 2, columnspan = 3)
upskill_text = tk.Text(Char_Window, height=5)
upskill_text.grid(row = 12, column = 0, pady = 2, columnspan = 3, sticky = 'NSEW')

done_button = tk.Button(Char_Window, text="Build Character", command=Check_Character, bg="blue")
done_button.grid(row = 13, column = 1, pady = 5, sticky = 'NSEW')

###Main Window Ends Here
###Main Window Ends Here
###Main Window Ends Here


#Run the Main Menu
Char_Window.mainloop()
