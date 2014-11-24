'''SMART-I'''
from Tkinter import *
import tkMessageBox

class First(object):   
    def __init__(score):
        score.root = Tk()
        score.root.geometry("350x250")
        score.root.title('Smart-I')

        score.lalabel = Label(score.root, text=" ").grid(row=0)
        score.label = Label(score.root, text="SMART-I", fg='red').place(relx=0.5, rely=0.08, anchor=CENTER)

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
        Button(score.root, textvariable=score.buttontext, command=score.claculate).grid(row=7, column=1)

        score.result = Label(score.root, text="Your result:").grid(row=8)
        Entry(score.root, textvariable="").grid(row=8, column=1)       

        score.root.mainloop()
        
    def claculate(score):
        result = Smarti(score.txtmath.get(), score.txteng.get(), score.txtread.get(), score.txtknow.get())
        me = result.calculate()
        score.knowledge = Label(score.root, text=me).grid(row=9, column=0)

class Smarti():
    def __init__(score, math, eng, read, know):
        score.math = math
        score.eng = eng
        score.read = read
        score.know = know

    def calculate(score):
        return (score.math + score.eng + score.read)*0.3 + (score.know*0.1)
    
First()
