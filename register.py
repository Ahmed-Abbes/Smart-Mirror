from tkinter import*
from tkinter import ttk
import tkinter as tk


class Register():
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x400+200+100")
        self.root.title("Register")
        self.root.configure(bg='black')
 # variables
        self.var_name=StringVar()
        self.var_Id=StringVar()

        label = ttk.Label(root, text = "Enter Your Name").pack()       
        label.pack()
        nameEntered = ttk.Entry(root, width = 25, textvariable = self.var_name).pack()
        nameEntered.pack()

        #label1 = ttk.Label(root, text = "Enter Your Id")       
        #label1.pack(pady=10)
        #IdEntered = ttk.Entry(root, width = 25, textvariable = self.var_Id)
        #IdEntered.pack(pady=0)

        

       




    def clickMe():
        label.configure(text= 'Hello ' + name.get())



if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()