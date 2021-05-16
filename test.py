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
        self.root.resizable(False,False)

        img=Image.open(r"CC:\Users\ASUS\Downloads\Iss\Iss\Smart.jpg")
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
    global username
    global password
    global username_entry
    global password_entry
    global register_screen
 
# The Toplevel widget work pretty much like Frame,
# but it is displayed in a separate, top-level window. 
#Such windows usually have title bars, borders, and other “window decorations”.
# And in argument we have to pass global screen variable
    
    register_screen = tk.Tk() 
    register_screen.title("Register")
    register_screen.geometry("300x400")
    register_screen.resizable(False,False)
    #register_screen.configure(bg='black')
 
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
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()    

def register_user():

# get username and password
    username_info = username.get()
    password_info = password.get()

# Open file in write mode
    file = open("username_info", "w")

# write username and password information into file
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    #print(username.get())

    

    username_entry.delete(0, END)
    password_entry.delete(0, END)

# set a label for showing success information on screen 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11))   


        
        















if __name__ == "__main__":
    root=Tk()
    obj=Mirror(root)
    root.mainloop()
