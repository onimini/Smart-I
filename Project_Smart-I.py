'''SMART-I'''
from Tkinter import *
import tkMessageBox

'''Class First for insert scores and show first page.'''
class First(object):   
    def __init__(score):
        '''Window Command'''
        score.root = Tk()
        score.root.geometry("340x280")
        score.root.title('Smart-I')

        '''Menu Bar'''
        score.menu = Menu(score.root)
        score.root.config(menu=score.menu)
        filemenu = Menu(score.menu)
        
        score.menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Exit", command=score.root.destroy)

        helpmenu = Menu(score.menu)
        score.menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About..." , command=score.about)

        '''For insert scores.'''
        score.lalabel = Label(score.root, text=" ").grid(row=0)
        score.label = Label(score.root, text="SMART- I", font='Cordia_New 16 bold italic', fg='red').place(relx=0.5, rely=0.08, anchor=CENTER)
        score.label = Label(score.root, text="Enter your scores.", font='Cordia_New 10 bold', fg='blue').place(relx=0.3, rely=0.2, anchor=CENTER)

        score.math = Label(score.root, text="Math:", font='Cordia_New 10').place(relx=0.3, rely=0.3, anchor=CENTER)
        score.txtmath = IntVar()
        Entry(score.root, textvariable=score.txtmath, cursor='cross').place(relx=0.7, rely=0.3, anchor=CENTER)

        score.eng = Label(score.root, text="English:", font='Cordia_New 10').place(relx=0.3, rely=0.4, anchor=CENTER)
        score.txteng = IntVar()
        Entry(score.root, textvariable=score.txteng, cursor='cross').place(relx=0.7, rely=0.4, anchor=CENTER)

        score.read = Label(score.root, text="Reading:", font='Cordia_New 10').place(relx=0.3, rely=0.5, anchor=CENTER)
        score.txtread = IntVar()
        Entry(score.root, textvariable=score.txtread, cursor='cross').place(relx=0.7, rely=0.5, anchor=CENTER)
        
        score.knowledge = Label(score.root, text="Knowledge:", font='Cordia_New 10').place(relx=0.3, rely=0.6, anchor=CENTER)
        score.txtknow = IntVar()
        Entry(score.root, textvariable=score.txtknow, cursor='cross').place(relx=0.7, rely=0.6, anchor=CENTER)
        
        '''Button Calculate.'''
        score.buttontext = IntVar()
        score.buttontext.set("Calculate")
        Button(score.root, textvariable=score.buttontext ,font='Cordia_New 10 bold', command=score.calculate, bd=4, bg='orange', cursor='cross').place(relx=0.5, rely=0.74, anchor=CENTER)

        score.result = Label(score.root, text="Your result:", font='Cordia_New 10 bold').place(relx=0.5, rely=0.86, anchor=CENTER)

        score.root.mainloop()

    '''About in help menu.'''
    def about(score):
        '''Window Command'''
        score.window = Tk()
        score.window.title('Smart-I')

        '''Menu Bar'''
        score.menu = Menu(score.window)
        score.window.config(menu=score.menu)
        filemenu = Menu(score.menu)

        score.menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Exit", command=score.window.destroy)

        helpmenu = Menu(score.menu)
        score.menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About..." , command=score.about)

        '''Information in About'''
        score.window.geometry("340x280")
        score.aboutext = Label(score.window, text="This program can calculate your Smart-I score for admission", font='Cordia_New 8').place(relx=0.5, rely=0.2, anchor=CENTER)
        score.aboutext2 = Label(score.window, text=" in Accounting Faculty at Thammasat University.", font='Cordia_New 8').place(relx=0.5, rely=0.25, anchor=CENTER)
        score.abouttext3 = Label(score.window, text="---------------------------------------------------", font='Cordia_New 8').place(relx=0.5, rely=0.3, anchor=CENTER)
        score.abouttext4 = Label(score.window, text="How to use", font='Cordia_New 8').place(relx=0.5, rely=0.35, anchor=CENTER)
        score.abouttext4 = Label(score.window, text="---------------------------------------------------", font='Cordia_New 8').place(relx=0.5, rely=0.4, anchor=CENTER)
        score.abouttext5 = Label(score.window, text="entry your score smart-I according to subject article.", font='Cordia_New 8').place(relx=0.5, rely=0.45, anchor=CENTER)
        score.abouttext6 = Label(score.window, text="program will calculate by math score, reading score", font='Cordia_New 8').place(relx=0.5, rely=0.5, anchor=CENTER)
        score.abouttext7 = Label(score.window, text="english score plus together then multiply with zero point three.", font='Cordia_New 8').place(relx=0.5, rely=0.55, anchor=CENTER)
        score.abouttext8 = Label(score.window, text="knowledge score multiply with zero point one.", font='Cordia_New 8').place(relx=0.5, rely=0.65, anchor=CENTER)
        score.abouttext9 = Label(score.window, text="then all score which already process plus together.", font='Cordia_New 8').place(relx=0.5, rely=0.7, anchor=CENTER)
        score.window.mainloop()


    '''Call Class Smarti for calculate.''' 
    def calculate(score):
        result = Smarti(score.txtmath.get(), score.txteng.get(), score.txtread.get(), score.txtknow.get())
        call_result = result.print_result()
        score.knowledge = Label(score.root, text=call_result, font='Cordia_New 10').place(relx=0.5, rely=0.93, anchor=CENTER)

'''Class Smarti for calculate and print result.'''  
class Smarti():
    '''Call input.'''
    def __init__(score, math, eng, read, know):
        score.math = math
        score.eng = eng
        score.read = read
        score.know = know

    '''Print result.'''
    def print_result(score):
        point = (score.math + score.eng + score.read)*0.3 + (score.know*0.1)
        if score.math > 0 and score.eng > 0 and score.read > 0 and score.know > 0: 
            if point >= 60 and point <= 100:
                return str(point) + ' ' + 'Maybe Pass.'
            elif point < 60 and point >= 0:
                return str(point) + ' ' + 'Maybe Not Pass.'
        else:
            return "Program can not calculate because your score incorrect."
    
First()
