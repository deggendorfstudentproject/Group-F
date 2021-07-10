import tkinter
from tkinter import *
def main():
    root = tkinter.Tk()
    root.geometry('400x600') #registration form size
    root.title("Registration Form")

    root.configure(background='black') #backgroundcolor
    menubar = Menu(root)
    root.config(menu=menubar)
    # create the submenu bar
    # text = Label(root, text='leTs share some files....')
    # text.pack()


    label_0 = Label(root, text="Registration Form",width=20,font=("bold", 20),background='black',fg='yellow')
    label_0.place(x=50,y=43)


    first_name_label = Label(root, text="First Name",width=20,font=("bold", 10),background='black',fg='white')
    first_name_label.place(x=0,y=100)
    first_name_entry = Entry(root)
    first_name_entry.place(x=140,y=100)

    second_name_label = Label(root, text="Last Name",width=20,font=("bold", 10),background='black',fg='white')
    second_name_label.place(x=0,y=140)
    second_name_entry = Entry(root)
    second_name_entry.place(x=140,y=140)

    gender = Label(root, text="Gender",width=20,font=("bold", 10),background='black',fg='white')
    gender.place(x=0,y=170)
    var = IntVar()
    Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=130,y=170)
    Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=200,y=170)

    age_label = Label(root, text="Age:",width=20,font=("bold", 10),background='black',fg='white')
    age_label.place(x=0,y=200)
    age_entry = Entry(root)
    age_entry.place(x=140,y=200)

    tkvar = StringVar(root)

    # Dictionary with options
    choices = {'AstraZenca', 'BioNTech/Pfizer', 'J&J', 'Moderna'}
   # tkvar.set('Pizza')  # set the default option

    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="Prefered Vaccine").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    # on change dropdown value
    def change_dropdown(*args):
        print(tkvar.get())

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)

    OptionList = [
        "Bavaria",
        "Baden Württemberg",
        "North Rhine-Westphalia",
        "Lower Saxony"
        "Hessen"
        "Saxony"
        "Schleswig-Holstein"
        "Rhineland Palatinate"
        "Thuringia"
        "Saarland"
        "Saxony Anhalt"
        "Hamburg"
        "Bremen"
        "Bradenburg"
        "Meklenburg"
        "Berlin"
    ]

    app = tk.Tk()

    app.geometry('100x200')

    variable = tk.StringVar(app)
    variable.set(OptionList[0])

    opt = tk.OptionMenu(app, variable, *OptionList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()
    app.mainloop()

    date = input("Select date in YYYY-MM-DD format")
    year, month, day = map(int, date.split('-'))
    date = datetime.date(year, month, day)

    time = Label(root, text="Select time", width=20, font=("bold", 10), background='black', fg='white')
    gender.place(x=0, y=170)
    var = IntVar()
    Radiobutton(root, text="Forenoon", padx=5, variable=var, value=1).place(x=130, y=170)
    Radiobutton(root, text="Afternoon", padx=20, variable=var, value=2).place(x=200, y=170)






    #email_label = Label(root, text="Email",width=20,font=("bold", 10),background='black',fg='white')
    #email_label.place(x=0,y=230)
    #email_entry = Entry(root)
    #email_entry.place(x=140,y=230)

    #mobile_label = Label(root, text="Mobile no",width=20,font=("bold", 10),background='black',fg='white')
    #mobile_label.place(x=0,y=270)
    #mobile_entry = Entry(root)
    #mobile_entry.place(x=140,y=270)


   # def submit_function(): #functiontosubmit
        #new_user_data = {"first_name": first_name_entry.get(), "last_name": second_name_entry.get(),
         #                "age": age_entry.get(),

          #               "gender": 'Male' if var.get() == 1 else 'Female', "email": email_entry.get(),
           #              "mobile": mobile_entry.get()

           }
