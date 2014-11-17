'''Calculate score for Smart-I examination.'''

from Tkinter import *
root = Tk()
root.title('Smart l')

class GUI(object):
    '''Show Graphic User Interface for running program 'Smart l'.'''
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack()

        self.root.mainloop()

def score(math, eng, read, social):
    '''Input scores of subject in parameter
    then calculate score from percent of subject which
    Mathematic(math) English(eng) and Reading(read) 
    will multi with 0.3, Social multi with 0.1 
    then find all plus.'''
    summary = ((math + eng + read) * 0.3 + (social * 0.1))
    if summary >= 63:
        print str(summary) + ' Maybe pass the exam.'
    else:
        print str(summary) + ' Maybe not pass the exam.'
score(input(), input(), input(), input())

GUI()
