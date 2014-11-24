'''SMART-I'''
from Tkinter import *
import tkMessageBox

class First(object):
    
    def __init__(score):
        global book
        book = {}
        score.root = Tk()
##        score.root.geometry("340x250")
##        score.root.title("Smart-I")
##
##        '''First Step'''
##        score.label = Label(score.root, text="Click Here!", fg='red')\
##                      .place(relx=0.5, rely=0.1, anchor=CENTER) 
##
##        score.buttontext = IntVar()
##        score.buttontext.set("New Student")
##        Button(score.root, textvariable=score.buttontext, command=score.button)\
##                           .place(relx=0.5, rely=0.2, anchor=CENTER)
##
##        score.lalabel = Label(score.root, text= "- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")\
##                        .place(relx=0.5, rely=0.3, anchor=CENTER)

##        '''Second Step'''
##        score.id = Label(score.root, text="Enter your Student ID after you added your score.", fg='red').place(relx=0.5, \
##                                                                rely=0.4, anchor=CENTER)
##
##        score.label = Label(score.root, text="Student ID:").place(relx=0.3, rely=0.5, anchor=CENTER) 
##        score.intid = IntVar()
##        Entry(score.root, textvariable=score.intid).place(relx=0.6, rely=0.5, anchor=CENTER)
##
##        score.buttontext = IntVar()
##        score.buttontext.set("Calculate")
##        Button(score.root, textvariable=score.buttontext)\
##                           .place(relx=0.5, rely=0.6, anchor=CENTER)

##        score.root.mainloop()
##
##    def button(score):
##        
##        score.root = Tk()
        score.root.geometry("250x180")
        #score.root.configure(background='black')
        score.root.title('Smart-I')

        score.lalabel = Label(score.root, text=" ").grid(row=0)
        score.label = Label(score.root, text="SMART-I", fg='red').place(relx=0.5, rely=0.08, anchor=CENTER)
        
##        '''Tap for your information.'''
##        score1.label = Label(score1.root, text="Enter your information.", fg='blue').grid(row=2)
##        
##        score1.name = Label(score1.root, text="Name:").grid(row=3)
##        score1.txtname = StringVar()
##        Entry(score1.root, textvariable=score1.txtname).grid(row=3, column=1)
##
##        score1.surname = Label(score1.root, text="Surname:").grid(row=4)
##        score1.txtsurname = StringVar()
##        Entry(score1.root, textvariable=score1.txtsurname).grid(row=4, column=1)
##
##        score1.school = Label(score1.root, text="School:").grid(row=5)
##        score1.txtschool = StringVar()
##        Entry(score1.root, textvariable=score1.txtschool).grid(row=5, column=1)
##
##        score1.std_id = Label(score1.root, text="Student ID:").grid(row=6)
##        score1.txtID = IntVar()
##        Entry(score1.root, textvariable=score1.txtID).grid(row=6, column=1)
##
##        score1.lalabel = Label(score1.root, text="    ").grid(column=2)

        '''Tap for your scores.'''
        score.label = Label(score.root, text="Enter your scores.", fg='blue').grid(row=2)

        score.math = Label(score.root, text="Math:").grid(row=3, column=0)
        score.txtmath = IntVar()
        Entry(score.root, textvariable=score.txtmath).grid(row=3, column=1)

        score.eng = Label(score.root, text="English:").grid(row=4, column=0)
        score.txteng = IntVar()
        Entry(score.root, textvariable=score.txteng).grid(row=4, column=1)

        score.read = Label(score.root, text="Reading:").grid(row=5, column=0)
        score.txtread = IntVar()
        Entry(score.root, textvariable=score.txtread).grid(row=5, column=1)

        score.knowledge = Label(score.root, text="Knowledge:").grid(row=6, column=0)
        score.txtknow = IntVar()
        Entry(score.root, textvariable=score.txtknow).grid(row=6, column=1)
        
        '''Button Calculate.'''
        score.buttontext = IntVar()
        score.buttontext.set("Calculate")
        Button(score.root, textvariable=score.buttontext, command=score.calculate).grid(row=7, column=1)

        score.result = Label(score.root, text="Your result:").grid(row=8)
        Entry(score.root, textvariable=score.calculate).grid(row=8, column=1)

        score.lalabel = Label(score.root, text="").grid(row=9)

        score.root.mainloop()

    def calculate(score):
        input = score.txtmath.get()
        input = score.txteng.get()
        input = score.txtread.get()
        input = score.txtknow.get()
        result = (score.txtmath.get() + score.txteng.get() +\
                  score.txtread.get())*0.3 + (score.txtknow.get())*0.1
        print result

First()
