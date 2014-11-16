'''Calculate score for Smart-I examination.'''
from Tkinter import *
import tkMessageBox

class Smart(object):
    def __init__(score):
        score.root = Tk()
        score.root.title("Smart-I")
        score.label = Label(score.root, text="Enter your score.").grid(row=0)
        
        score.math = Label(score.root, text="Math").grid(row=1)
        score.textmath = IntVar()
        Entry(score.root, textvariable=score.textmath).grid(row=1, ccolumn=1)
        
        score.eng = Label(score.root, text="English").grid(row=2)
        score.texteng = IntVar()
        Entry(score.root, textvariable=score.texteng).grid(row=2, column=1)
        
        score.read = Label(score.root, text="Reading").grid(row=3)
        score.textread = IntVar()
        Entry(score.root, textvariable=score.textread).grid(row=3, column=1)
        
        score.know = Label(score.root, text="Knowledge").grid(row=4)
        score.textknow = IntVar()
        Entry(score.root, textvariable=score.textknow).grid(row=4, column=1)
        
        score.buttontext = IntVar()
        score.buttontext.set("Calculate")
        Button(score.root, textvariable=score.buttontext, command=score.calculate).grid(row=5, column=1)
        
        score.root.mainloop()
        
    def calculate(score):
         '''Input scores of subject in parameter
        then calculate score from percent of subject which
        Mathematic(math) English(eng) and Reading(read) 
        will multi with 0.3, Social multi with 0.1 
        then find all plus.'''
        input = score.textmath.get()
        input = score.texteng.get()
        input = score.textread.get()
        input = score.textknow.get()
        result = (score.textmath.get() + score.texteng.get() + score.textread.get())*0.3 + (score.textknow.get()*0.1)
        print result
        
'''
def score(math, eng, read, social):
    ''''''Input scores of subject in parameter
    then calculate score from percent of subject which
    Mathematic(math) English(eng) and Reading(read) 
    will multi with 0.3, Social multi with 0.1 
    then find all plus.''''''
    summary = ((math + eng + read) * 0.3 + (social * 0.1))
    if summary >= 63:
        print str(summary) + ' Maybe pass the exam.'
    else:
        print str(summary) + ' Maybe not pass the exam.'
score(input(), input(), input(), input())
'''
