from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from mirror import Mirror
class smart_mirror():
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
        btn = Button(root, text = "Start",command = self.smart,cursor="hand2",font=("time new roman",18 , "bold"), bg="white", fg="black",border="25")
        btn.place(x=320,y=550,width=220,height=70)    

        
 
    def smart(self):
        self.new_window=Toplevel(self.root)
        self.app=Mirror(self.new_window)
    















if __name__ == "__main__":
    root=Tk()
    obj=smart_mirror(root)
    root.mainloop()
