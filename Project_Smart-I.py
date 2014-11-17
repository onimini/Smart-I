'''Calculate score for Smart-I examination.'''
from Tkinter import *
import tkMessageBox
    
class Smart(object):
        
    def __init__(score):
        score.root = Tk()
        score.root.title('Smart-I')

        score.buttontext = IntVar()
        score.buttontext.set("New Student")
        Button(score.root, textvariable=score.buttontext, fg='red', command=calculate).grid(row=1)

        score.label = Label(score.root, text="Enter your ID Student after you added your point.", ).grid(row=2, sticky=W)

        score.id = Label(score.root, text="ID Student:").grid(row=3, sticky=W)
        score.intid = IntVar()
        Entry(score.root, textvariable=score.intid).grid(row=3)

        score.buttontext = IntVar()
        score.buttontext.set("Calculate")
        Button(score.root, textvariable=score.buttontext, fg='red', bg='black').grid(row=4)

        score.root.mainloop()
    
    def __init__(score):
        score.root = Tk()
        score.root.title('Smart-I')
        
        score.label = Label(score.root, text="Enter your score.").grid(row=0)
        
        score.math = Label(score.root, text="Math:").grid(row=1, sticky=W)
        score.textmath = IntVar()
        Entry(score.root, textvariable=score.textmath).grid(row=1, column=1)

        score.eng = Label(score.root, text="English:").grid(row=2, sticky=W)
        score.texteng = IntVar()
        Entry(score.root, textvariable=score.texteng).grid(row=2, column=1)

        score.read = Label(score.root, text="Reading:").grid(row=3, sticky=W)
        score.textread = IntVar()
        Entry(score.root, textvariable=score.textread).grid(row=3, column=1)

        score.know = Label(score.root, text="Knowledge:").grid(row=4, sticky=W)
        score.textknow = IntVar()
        Entry(score.root, textvariable=score.textknow).grid(row=4, column=1)

        score.buttontext = IntVar()
        score.buttontext.set("Calculate")
        Button(score.root, textvariable=score.buttontext, fg='red', bg='black', command=score.calculate).grid(row=5, column=1)

        score.lalabel = Label(score.root, text="").grid(row=6)

        score.root.mainloop()
        score.root.destroy()

    def calculate(score):
        root = Tk()
        '''Input scores of subject in parameter then calculate score
        from percent of subject which Mathematic(math) English(eng)
        and Reading(read) will multi with 0.3, Social multi with 0.1
        then find all plus.'''
        input = score.textmath.get()
        input = score.texteng.get()
        input = score.textread.get()
        input = score.textknow.get()
        result = (score.textmath.get() + score.texteng.get() +\
                  score.textread.get())*0.3 + (score.textknow.get()*0.1)
        print result
        

Smart()
