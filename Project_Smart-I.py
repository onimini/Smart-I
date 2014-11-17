'''Calculate score for Smart-I examination.'''
from Tkinter import *
import tkMessageBox
    
class First(object):
    def __init__(score):
        score.root = Tk()
        score.root.title('Smart-I')

        score.buttontext = IntVar()
        score.buttontext.set("New Student")
        Button(score.root, textvariable=score.buttontext).grid(row=1)

        score.label = Label(score.root, text="Enter your ID Student after you added your point.", ).grid(row=2, sticky=W)

        score.id = Label(score.root, text="Student ID:").grid(row=3, sticky=W)
        score.intid = IntVar()
        Entry(score.root, textvariable=score.intid).grid(row=3)

        score.buttontext = IntVar()
        score.buttontext.set("Calculate")
        Button(score.root, textvariable=score.buttontext).grid(row=4)

        score.root.mainloop()

        def id_student(click):
                  input = click.intid.get()

First()

##class Smart(object):
##    def __init__(score):
##        score.root = Tk()
##        score.root.title('Smart-I')
##        
##        score.label = Label(score.root, text="Enter your score.").grid(row=0)
##
##        score.name = Label(score.root, text="Name:".grid(row=1, sticky=W)
##        score.textname = StringVar()
##        Entry(score.root, textvariable=score.textname).grid(row=1, column=1)
##
##        score.name = Label(score.root, text="Surname:".grid(row=2, sticky=W)
##        score.textsurname = StringVar()
##        Entry(score.root, textvariable=score.textsurname).grid(row=2, column=1)
##
##        score.name = Label(score.root, text="Age:".grid(row=3, sticky=W)
##        score.textage = IntVar()
##        Entry(score.root, textvariable=score.textage).grid(row=3, column=1)
##
##        score.name = Label(score.root, text="ID:".grid(row=4, sticky=W)
##        score.textID = IntVar()
##        Entry(score.root, textvariable=score.textID).grid(row=4, column=1)
##        
##        score.math = Label(score.root, text="Math:").grid(row=5, sticky=W)
##        score.textmath = IntVar()
##        Entry(score.root, textvariable=score.textmath).grid(row=5, column=1)
##
##        score.eng = Label(score.root, text="English:").grid(row=6, sticky=W)
##        score.texteng = IntVar()
##        Entry(score.root, textvariable=score.texteng).grid(row=6, column=1)
##
##        score.read = Label(score.root, text="Reading:").grid(row=7, sticky=W)
##        score.textread = IntVar()
##        Entry(score.root, textvariable=score.textread).grid(row=7, column=1)
##
##        score.know = Label(score.root, text="Knowledge:").grid(row=8, sticky=W)
##        score.textknow = IntVar()
##        Entry(score.root, textvariable=score.textknow).grid(row=8, column=1)
##
##        score.buttontext = IntVar()
##        score.buttontext.set("Calculate")
##        Button(score.root, textvariable=score.buttontext, fg='red', bg='black', command=score.calculate).grid(row=9, column=1)
##
##        score.lalabel = Label(score.root, text="").grid(row=10)
##
##        score.root.mainloop()
##        score.root.destroy()
##                           
##    def calculate(score):
##        root = Tk()
##        '''Input scores of subject in parameter then calculate score
##        from percent of subject which Mathematic(math) English(eng)
##        and Reading(read) will multi with 0.3, Social multi with 0.1
##        then find all plus.'''
##        input = score.textage.get()
##        input = score.textID.get()
##        input = score.textmath.get()
##        input = score.texteng.get()
##        input = score.textread.get()
##        input = score.textknow.get()
##        result = (score.textmath.get() + score.texteng.get() +\
##                  score.textread.get())*0.3 + (score.textknow.get()*0.1)
##        print result
##        mainloop()
        
Smart()



