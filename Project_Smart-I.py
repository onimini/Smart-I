'''SMART-I'''
from Tkinter import *
import tkMessageBox

class First(object):
    
    def __init__(score):
        score.root = Tk()
        score.root.geometry("340x250")
        score.root.title("Smart-I")

        '''First Step'''
        score.label = Label(score.root, text="Click Here!", fg='red')\
                      .place(relx=0.5, rely=0.1, anchor=CENTER) 

        score.buttontext = IntVar()
        score.buttontext.set("New Student")
        Button(score.root, textvariable=score.buttontext, command=score.button)\
                           .place(relx=0.5, rely=0.2, anchor=CENTER)

        score.lalabel = Label(score.root, text= "- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")\
                        .place(relx=0.5, rely=0.3, anchor=CENTER)

        '''Second Step'''
        score.id = Label(score.root, text="Enter your Student ID after you added your score.", fg='red').place(relx=0.5, \
                                                                rely=0.4, anchor=CENTER)

        score.label = Label(score.root, text="Student ID:").place(relx=0.3, rely=0.5, anchor=CENTER) 
        score.intid = IntVar()
        Entry(score.root, textvariable=score.intid).place(relx=0.6, rely=0.5, anchor=CENTER)

        score.buttontext = IntVar()
        score.buttontext.set("Calculate")
        Button(score.root, textvariable=score.buttontext, command=score.cal)\
                           .place(relx=0.5, rely=0.6, anchor=CENTER)

        score.root.mainloop()

    def button(score):
        
        global lisObject
        global lisTemp
        lisObject = []
        lisTemp = []
        
        score.root = Tk()
        score.root.geometry("510x180")
        #score.root.configure(background='black')
        score.root.title('Smart-I')

        score.lalabel = Label(score.root, text=" ").grid(row=0)
        score.label = Label(score.root, text="SMART-I", fg='red').place(relx=0.5, rely=0.08, anchor=CENTER)
        
        '''Tap for your information.'''
        score.label = Label(score.root, text="Enter your information.", fg='blue').grid(row=2)
        
        score.name = Label(score.root, text="Name:").grid(row=3)
        score.txtname = StringVar()
        Entry(score.root, textvariable=score.txtname).grid(row=3, column=1)

        score.surname = Label(score.root, text="Surname:").grid(row=4)
        score.txtsurname = StringVar()
        Entry(score.root, textvariable=score.txtsurname).grid(row=4, column=1)

        score.school = Label(score.root, text="School:").grid(row=5)
        score.txtschool = StringVar()
        Entry(score.root, textvariable=score.txtschool).grid(row=5, column=1)

        score.std_id = Label(score.root, text="Student ID:").grid(row=6)
        score.txtID = IntVar()
        Entry(score.root, textvariable=score.txtID).grid(row=6, column=1)

        score.lalabel = Label(score.root, text="    ").grid(column=2)

        '''Tap for your scores.'''
        score.label = Label(score.root, text="Enter your scores.", fg='blue').grid(row=2, column=3)

        score.math = Label(score.root, text="Math:").grid(row=3, column=3)
        score.txtmath = IntVar()
        Entry(score.root, textvariable=score.txtmath).grid(row=3, column=4)

        score.eng = Label(score.root, text="English:").grid(row=4, column=3)
        score.txteng = IntVar()
        Entry(score.root, textvariable=score.txteng).grid(row=4, column=4)

        score.read = Label(score.root, text="Reading:").grid(row=5, column=3)
        score.txtread = IntVar()
        Entry(score.root, textvariable=score.txtread).grid(row=5, column=4)

        score.knowledge = Label(score.root, text="Knowledge:").grid(row=6, column=3)
        score.txtknow = IntVar()
        Entry(score.root, textvariable=score.txtknow).grid(row=6, column=4)
        
        '''Button Save.'''
        score.buttontext = IntVar()
        Button(score.root, text="Save", textvariable=score.buttontext, command= score.new).place(relx=0.5, rely=0.9, anchor=CENTER)

        score.lalabel = Label(score.root, text="").grid(row=8)
        score.root.mainloop()

    def cal(score):
        score.root = Tk()
        
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
