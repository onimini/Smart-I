from Tkinter import *
import tkMessageBox

class First(object):
    def __init__(score):
        score.root = Tk()
        score.root.geometry("340x260")
        score.root.title("Smart-I")

        score.buttontext = IntVar()
        score.buttontext.set("New Student")
        Button(score.root, textvariable=score.buttontext, command=score.button).place(relx=0.5, rely=0.2, anchor=CENTER)

        score.label = Label(score.root, text="Student ID:").place(relx=0.3, rely=0.5, anchor=CENTER)

        score.id = Label(score.root, text="Enter your Id Student after you added your score.").place(relx=0.5, rely=0.3, anchor=CENTER)
        score.intid = IntVar()
        Entry(score.root, textvariable=score.intid).place(relx=0.6, rely=0.5, anchor=CENTER)

        score.buttontext = IntVar()
        score.buttontext.set("Calculate")
        Button(score.root, textvariable=score.buttontext).place(relx=0.5, rely=0.7, anchor=CENTER)

        score.root.mainloop()

    def button(score):
        global lisObject
        global lisTemp
        lisObject = []
        lisTemp = []
        score.root = Tk()
        score.root.title('Smart-I')
        score.label = Label(score.root, text="Enter your score.").grid(row=0)
        
        score.name = Label(score.root, text="Name").grid(row=1)
        score.txtname = StringVar()
        Entry(score.root, textvariable=score.txtname).grid(row=1, column=1)

        score.surname = Label(score.root, text="Surname").grid(row=2)
        score.txtsurname = StringVar()
        Entry(score.root, textvariable=score.txtsurname).grid(row=2, column=1)

        score.school = Label(score.root, text="School").grid(row=4)
        score.txtschool = StringVar()
        Entry(score.root, textvariable=score.txtschool).grid(row=4, column=1)

        score.std_id = Label(score.root, text="Student ID").grid(row=5)
        score.txtID = IntVar()
        Entry(score.root, textvariable=score.txtID).grid(row=5, column=1)

        score.buttontext = IntVar()
        Button(score.root, text="Save", textvariable=score.buttontext, command= score.new).grid(row=6, column=1)        

        score.lalabel = Label(score.root, text="").grid(row=8)
        score.root.mainloop()

    def new(score):
        std = student(score.txtID.get(),score.txtname.get(),score.txtsurname.get(),score.txtschool.get())              
        lisObject.append(std)
        lisTemp.append(int(score.txtID.get()))
        
    def slis(score):
        xx = score.txt_in_id.get()
        print lisObject[lisTemp.index(xx)].show()
        
class student():
    def __init__(std,std_id,name,surname,age,school):
        std.id = std_id
        std.name = name
        std.surname = surname
        std.age = age
        std.school = school  

    def show(std):
        print std.name,std.surname,std.age

        

First()
