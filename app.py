import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()


# color = {"nero": "#25226", "orange": "#FF8870", "darkorange": "#FE6101"}

root.title("Vaccination Buddy")
# root.config(bg="gray17")
root.geometry("800x600")
sideFrame = tk.Frame(root, bg="#00ADB5", height=600, width=40)

homeButton = tk.Button(
    sideFrame, text="HM", width=40, command=lambda: print("Hello World")
)
# homeButton.pack()
homeButton.place(x=0, y=0)
sideFrame.pack(side="left")


# root.state("zoomed")
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)


# frame1 = tk.Frame(root, bg="red")
# frame1.grid(row=0, column=0, sticky="nsew")

# canvas = tk.Canvas(root, width=600, height=300)
# canvas.grid(columnspan=3, rowspan=3)

# # logo
# instructions = tk.Label(root, text="select a pdf file on your computer", font="Raleway")
# instructions.grid(columnspan=3, column=0, row=0)


root.mainloop()
