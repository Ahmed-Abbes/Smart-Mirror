from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
class Mirror():
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x700+0+0")
        self.root.title("Smart Mirror")
        self.root.configure(bg='black')

        img=Image.open(r"C:\Users\ASUS\Desktop\python3\Iss\Smart.jpg")
        img=img.resize((700,900), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=150,y=30,width=500,height=500)
        # Mirror button
        btn = Button(root, text = "Login",command = root.destroy,cursor="hand2",font=("time new roman",18 , "bold"), bg="white", fg="black",border="20")
        btn.place(x=150,y=550,width=220,height=70)    

        btn1 = Button(root, text = "Register",command = register,cursor="hand2",font=("time new roman",18 , "bold"), bg="white", fg="black",border="20")
        btn1.place(x=430,y=550,width=220,height=70) 


def register():
 
# The Toplevel widget work pretty much like Frame,
# but it is displayed in a separate, top-level window. 
#Such windows usually have title bars, borders, and other “window decorations”.
# And in argument we have to pass global screen variable
    
    register_screen = tk.Tk() 
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
# Set text variables
    username = StringVar()
    password = StringVar()
 
# Set label for user's instruction
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    
# Set username label
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
   
# Set password label
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    
# Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(register_screen, text="").pack()
    
# Set register button
    Button(register_screen, text="Register", width=10, height=1, bg="blue").pack()    

 
    
    















if __name__ == "__main__":
    root=Tk()
    obj=Mirror(root)
    root.mainloop()
