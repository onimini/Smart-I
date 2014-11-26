'''SMART-I'''
from Tkinter import *
import tkMessageBox

class First(object):   
    def __init__(score):            
        score.root = Tk()
        score.root.geometry("340x280")
        score.root.title('Smart-I')
        score.menu = Menu(score.root)
        score.root.config(menu=score.menu)
        
        filemenu = Menu(score.menu)
        score.menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=score.root.quit)

        helpmenu = Menu(score.menu)
        score.menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About..." ,command=score.about)

        score.lalabel = Label(score.root, text=" ").grid(row=0)
        score.label = Label(score.root, text="SMART-I", fg='red').place(relx=0.5, rely=0.08, anchor=CENTER)

        '''Tap for your scores.'''
        score.label = Label(score.root, text="Enter your scores.", fg='blue').place(relx=0.3, rely=0.2, anchor=CENTER)

        score.math = Label(score.root, text="Math:").place(relx=0.3, rely=0.3, anchor=CENTER)
        score.txtmath = IntVar()
        Entry(score.root, textvariable=score.txtmath).place(relx=0.7, rely=0.3, anchor=CENTER)

        score.eng = Label(score.root, text="English:").place(relx=0.3, rely=0.4, anchor=CENTER)
        score.txteng = IntVar()
        Entry(score.root, textvariable=score.txteng).place(relx=0.7, rely=0.4, anchor=CENTER)

        score.read = Label(score.root, text="Reading:").place(relx=0.3, rely=0.5, anchor=CENTER)
        score.txtread = IntVar()
        Entry(score.root, textvariable=score.txtread).place(relx=0.7, rely=0.5, anchor=CENTER)

        score.knowledge = Label(score.root, text="Knowledge:").place(relx=0.3, rely=0.6, anchor=CENTER)
        score.txtknow = IntVar()
        Entry(score.root, textvariable=score.txtknow).place(relx=0.7, rely=0.6, anchor=CENTER)
        
        '''Button Calculate.'''
        score.buttontext = IntVar()
        score.buttontext.set("Calculate")
        Button(score.root, textvariable=score.buttontext, command=score.claculate).place(relx=0.5, rely=0.74, anchor=CENTER)
        score.result = Label(score.root, text="Your result:").place(relx=0.5, rely=0.84, anchor=CENTER)    

        score.root.mainloop()
        score.root.destroy()
        
    def about(score):
        score.root = Tk()
        score.label = Label(score.root, text="This program can calculate your Smart-I score for admission in Accounting Faculty at Thammasat University.")
        score.root.mainloop()
        
    def claculate(score):
        result = Smarti(score.txtmath.get(), score.txteng.get(), score.txtread.get(), score.txtknow.get())
        me = result.calculate()
        score.knowledge = Label(score.root, text=me).place(relx=0.5, rely=0.9, anchor=CENTER)
        
class Smarti():
    def __init__(score, math, eng, read, know):
        score.math = math
        score.eng = eng
        score.read = read
        score.know = know

    def calculate(score):
        point = (score.math + score.eng + score.read)*0.3 + (score.know*0.1)
        con = [' Maybe Pass', 'Maybe Not Pass'][point <=60]
        return str(point) + ' ' + con
    
First()
