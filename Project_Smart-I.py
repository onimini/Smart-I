'''SMART-I'''
from Tkinter import *
import tkMessageBox

class First(object):
    
    def __init__(score):
        global book
        book = {}
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
        Button(score.root, textvariable=score.buttontext)\
                           .place(relx=0.5, rely=0.6, anchor=CENTER)

        score.root.mainloop()

    def button(score1):
        
        score1.root = Tk()
        score1.root.geometry("510x180")
        #score.root.configure(background='black')
        score1.root.title('Smart-I')

        score1.lalabel = Label(score1.root, text=" ").grid(row=0)
        score1.label = Label(score1.root, text="SMART-I", fg='red').place(relx=0.5, rely=0.08, anchor=CENTER)
        
        '''Tap for your information.'''
        score1.label = Label(score1.root, text="Enter your information.", fg='blue').grid(row=2)
        
        score1.name = Label(score1.root, text="Name:").grid(row=3)
        score1.txtname = StringVar()
        Entry(score1.root, textvariable=score1.txtname).grid(row=3, column=1)

        score1.surname = Label(score1.root, text="Surname:").grid(row=4)
        score1.txtsurname = StringVar()
        Entry(score1.root, textvariable=score1.txtsurname).grid(row=4, column=1)

        score1.school = Label(score1.root, text="School:").grid(row=5)
        score1.txtschool = StringVar()
        Entry(score1.root, textvariable=score1.txtschool).grid(row=5, column=1)

        score1.std_id = Label(score1.root, text="Student ID:").grid(row=6)
        score1.txtID = IntVar()
        Entry(score1.root, textvariable=score1.txtID).grid(row=6, column=1)

        score1.lalabel = Label(score1.root, text="    ").grid(column=2)

        '''Tap for your scores.'''
        score1.label = Label(score1.root, text="Enter your scores.", fg='blue').grid(row=2, column=3)

        score1.math = Label(score1.root, text="Math:").grid(row=3, column=3)
        score1.txtmath = IntVar()
        Entry(score1.root, textvariable=score1.txtmath).grid(row=3, column=4)

        score1.eng = Label(score1.root, text="English:").grid(row=4, column=3)
        score1.txteng = IntVar()
        Entry(score1.root, textvariable=score1.txteng).grid(row=4, column=4)

        score1.read = Label(score1.root, text="Reading:").grid(row=5, column=3)
        score1.txtread = IntVar()
        Entry(score1.root, textvariable=score1.txtread).grid(row=5, column=4)

        score1.knowledge = Label(score1.root, text="Knowledge:").grid(row=6, column=3)
        score1.txtknow = IntVar()
        Entry(score1.root, textvariable=score1.txtknow).grid(row=6, column=4)
        
        '''Button Save.'''
        score1.buttontext = Button(score1.root, text="Save", textvariable=score1.buttontext).place(relx=0.5, rely=0.9, anchor=CENTER)

        score1.lalabel = Label(score1.root, text="").grid(row=8)
##        def new(score):
##            cally = stdent.calcu(score1.txtmath.get(), score1.txteng.get(), score1.txtread.get(), score1.txtknow.get())
##            print cally
##        
##class student():
##    def __init__(std, math, eng, read, know):
##        std.math = math
##        std.eng = eng
##        std.read = read
##        std.know = know
##
##    def calcu(std):
##        result = ((std.math + std.eng + std.read)*0.3) + (std.know*0.1)
##        print result
        
First()

