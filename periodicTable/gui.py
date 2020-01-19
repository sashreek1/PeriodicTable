from period_lib import main
from tkinter import *
from mendeleev import element
from tkinter import messagebox
import random


class app:
    def __init__(self):
        self.wrong_ans = 0
        self.status = None
        self.hint_no = 5
        self.chances = 5
        
    def get_elem(self,num):
        ele = element(num)
        ans = ele.symbol
        return ans

    def hint_func(self,atno):
        print("The hint number is", self.hint_no)
        if self.hint_no == 5:
            prev_elem = element(atno-1)
            name = prev_elem.name
            symbol = prev_elem.symbol
            message = "The previous element in the periodic table is "+str(name)+"\n"+"its symbol is "+str(symbol)
            messagebox.showinfo("Hint", message)
            self.hint_no-=1

        elif self.hint_no == 4:
            next_elem = element(atno+1)
            name = next_elem.name
            symbol = next_elem.symbol
            message = "The next element in the periodic table is "+str(name)+"\n"+"its symbol is "+str(symbol)
            messagebox.showinfo("Hint", message)
            self.hint_no-=1
        
        elif self.hint_no == 3:
            elem = element(atno)
            mass_no = elem.mass_number
            message = "The mass number of the most stable isotope of this element is {}".format(mass_no)
            messagebox.showinfo("Hint", message)
            self.hint_no-=1

        elif self.hint_no == 2:
            elem = element(atno)
            uses = elem.uses
            message = "The uses of the element are : \n"+str(uses)
            messagebox.showinfo("Hint", message)
            self.hint_no-=1

        elif self.hint_no == 1:
            elem = element(atno)
            name = elem.name
            sources = elem.sources
            message = "The elemnet starts with the letter {} \n It can be obtained from the following sources : \n {}".format(str(name)[0],sources)
            messagebox.showinfo("Hint", message)
            self.hint_no-=1

        elif self.hint_no <= 0:
            messagebox.showwarning("Warning","You have run out of hints")
            self.hint_no-=1

            
    def submit_func(self,root,submission,atno,box):
        sym = self.get_elem(int(atno.get()))
        if submission == sym:
            messagebox.showinfo("Information","Correct!!")
            self.hint_no = 5
            atno.set(str(random.randrange(1,118)))
            print(atno.get())
            box.delete(0, 'end')
        else:
            if self.chances <= 1:
                messagebox.showwarning("game", "GAME OVER")
                root.destroy()
                
            else:
                self.chances -= 1
                messagebox.showerror("Information", "Wrong :( \n please take a hint and try again \n You have {} chances left".format(self.chances))
                box.delete(0, 'end')
        
    
    def run_gui (self):
        root = Tk()
        root.title('Periodic Table guessing game')
        root.geometry("700x550+900+300")
        root.resizable(False, False)
        root.configure(background='#00CED1')

        rule_text ="""

GAME RULES :
* You have a total of 5 chances to
    guess the answers
    
* For each question you get 5 hints

* The answer nust be the scientific
    symbol of an element with
    proper casing
    correct answer : Ag
    wrong answers : ag, AG,A g, etc
"""
        messagebox.showinfo("Rules", rule_text)
        atno = StringVar()
        atno.set(str(random.randrange(1,118)))
        atno_p = Label(root, textvariable=atno)
        atno_p.place(x=250,y=50)
        atno_p.config(font=("Courier", 88),background='#00CED1')

        b = Button(root,text='Hint',command=lambda : self.hint_func(int(atno.get())))
        b.config(font=("Courier", 22))
        b.place(x=150,y=400)

        ans = Entry(root)
        ans.config(font=("Courier", 88),width=3)
        ans.place(x=250,y=175)

        b1 = Button(root,text='Submit', command=lambda : self.submit_func(root,ans.get(),atno,ans))
        b1.config(font=("Courier", 22))
        b1.place(x=450,y=400)
        
        root.mainloop()



app = app()
app.run_gui()
