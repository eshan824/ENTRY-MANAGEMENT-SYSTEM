from tkinter import *
import datetime

root = Tk()
root.title("GYM ENTRY & CHECKING SYSTEM")
root.geometry("350x200")
#root.minsize(350,200)
#root.maxsize(350,200)
first_name_ = StringVar()
last_name_ = StringVar()
fees_ = StringVar()

def saving_entry ():
    datetimenow = datetime.datetime.now()
    first_name_str = first_name_.get()
    last_name_str = last_name_.get()
    fees_str = fees_.get()
    make_file = open("D:/CODE WITH HARRY/PYTHON           GUI/PYTHON FILES/CODE_WITH_HARRY_PY_DATA/GYM ENTRIES.txt", "a")
    make_file.write(f"\nNAME: {first_name_str} {last_name_str}\nFEES: {fees_str}\-\nDATE & TIME: {datetimenow}\n,")



def make_entry ():    
    b1.destroy()
    b2.destroy()
    b3.destroy()
    
    welcome_screen = Label(root, text = "*** WELCOME TO GYM ENTRY SYSTEM ***", 
                           font = ("comicsans",12,"bold","underline"), background = "black", foreground = "white")
    welcome_screen.grid(row = 0, columnspan = 5,padx = 10)
    first_name = Label(root, text = "FIRST NAME: ")
    first_name.grid(row = 3, column = 0, pady = 10)

    first_name_entry = Entry(root, textvariable = first_name_, background = "white", foreground = "black"
                        ,font = ("comicsans", 8, "bold"))
    first_name_entry.grid(row = 3, column = 1, pady = 10)
    
    last_name = Label(root, text = "LAST NAME: ")
    last_name.grid(row = 4, column = 0)

    last_name_entry = Entry(root, textvariable = last_name_, background = "white", foreground = "black"
                        ,font = ("comicsans", 8, "bold"))
    last_name_entry.grid(row = 4, column = 1)
    
    fees = Label(root, text = "FEES: ")
    fees.grid(row = 5, column = 0, pady = 10)

    fees_entry = Entry(root, textvariable = fees_, background = "white", foreground = "black"
                        ,font = ("comicsans", 8, "bold"))
    fees_entry.grid(row = 5, column = 1, pady = 10)
    
    submit_button = Button (root, text = "SUBMIT",background = "black", foreground = "white",
                            font = ("Times New Roman", 10, "italic"), border = 4, relief = RAISED, command = saving_entry)
    submit_button.grid(row = 6, column = 1)
    
def check_entries ():
    b1.destroy()
    b2.destroy()
    b3.destroy()
    check_file = open("D:/CODE WITH HARRY/PYTHON           GUI/PYTHON FILES/CODE_WITH_HARRY_PY_DATA/GYM ENTRIES.txt", "r")
    reading_entry_file = check_file.read()
    showing_data = Label(root, text = reading_entry_file, justify = LEFT).grid(padx = 10)
    
def find_entry ():
    b1.destroy()
    b2.destroy()
    b3.destroy()
    name_find = StringVar()
    def finding_name ():
        name_find_str = name_find.get()
        check_file = open("D:/CODE WITH HARRY/PYTHON           GUI/PYTHON FILES/CODE_WITH_HARRY_PY_DATA/GYM ENTRIES.txt", "r")
        reading_entry_file = check_file.read()
        reading_entry_file_ = reading_entry_file.split(",")
        i = 0
        for x in reading_entry_file_:
            writing_details = reading_entry_file_[i].find(name_find_str)
            if writing_details != -1:
                display_details_label = Label(root, text = reading_entry_file_[i], background = "black"
                                             , foreground = "white", padx = 3).grid()
                i += 1
        
    name_label = Label (root, text = "ENTER NAME: ").grid(row = 0, column = 0, pady = 10)
    name_label_entry = Entry(root, textvariable = name_find, border = 2
                             , relief = RAISED).grid(row = 0, column = 1,padx = 5, pady = 10)
    name_label_entry_button = Button(root, text = "SUBMIT", background = "black", foreground = "white"
                                    , border = 2, relief = RAISED, command = finding_name).grid(row = 1, column = 1)
    
b1 = Button(root, text = "MAKE ENTRY", font = ("symbolic", 8,"italic","underline"), border = 3, 
            relief = RAISED, command = make_entry)
b1.grid(row = 0, column = 0, padx = 4)

b2 = Button(root, text = "FIND ENTRY", font = ("symbolic", 8,"italic","underline"), border = 3, 
            relief = RAISED, command = find_entry)
b2.grid(row = 4, column = 0, pady = 20)

b3 = Button(root, text = "CHECK ALL PREVIOUS ENTRIES", font = ("symbolic", 8,"italic","underline"), 
            border = 3, relief = RAISED, command = check_entries)
b3.grid(row = 5, columnspan = 19, padx = 5)

root.mainloop()