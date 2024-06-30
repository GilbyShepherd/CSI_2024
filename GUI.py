from tkinter import *
from tkinter import messagebox 
"""
Tkinter is a Python binding to the Tk GUI toolkit.
It is the standard Python interface to the Tk GUI toolkit, and is Python's de
facto standard GUI.
Tkinter is included with standard Linux, Microsoft Windows and macOS installs of
Python.
Tk is a cross-platform widget Toolkit that provides a library of basic elements
of
GUI widgets for building a graphical user interface (GUI).
"""
class MazeGame:
    def __init__(self):
        self.root = Tk()
        self.root.title('maze')
        self.root.iconphoto(True, PhotoImage(file = "lava.png") )
        #creats a canvas
        self.canvas = Canvas(self.root,width = 200, height=200, bg = 'blue')
        self.canvas.grid(row=0,column=0,columnspan =3)
        #self.canvas.pack()
        self.image = PhotoImage(file="rock.png")
        #Default center of image at coordinate
        self.canvas.create_image(0,0,image=self.image)
        #tk.NW top left corner of image at coordinate
        self.canvas.create_image(100,100,image=self.image,anchor=NW)
        #set up menu
        self.menubar = Menu(self.root)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help ", command=lambda :
messagebox.showinfo("Help", "This is the help message."))
        self.helpmenu.add_command(label="About...", command=lambda :
messagebox.showinfo("About", "This is an about message."))
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.root.config(menu=self.menubar)
# add buttons
        self.up_button = Button(self.root,text="Up")
        self.up_button.grid(row=1,column=1)
        #self.up_button.pack()
        self.down_button = Button(self.root,text="Down")
        self.down_button.grid(row=3,column=1,)
        #self.down_button.pack()
        self.left_button = Button(self.root,text="left")
        self.left_button.grid(row=2,column=0,)
        #self.left_button.pack()
        self.right_button = Button(self.root,text="right")
        self.right_button.grid(row=2,column=2,)
        #self.left_button.pack()


        self.root.mainloop()
if __name__ =="__main__":
    game = MazeGame()