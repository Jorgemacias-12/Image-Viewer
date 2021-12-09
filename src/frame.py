from tkinter import *

import utils

def main():
    root = Tk()
    root.title("Image Viewer - JAMZ")
    root.resizable(False, False)
    
    
    menubar = Menu(root)
   
    folderMenu = Menu(menubar, tearoff=0)
    folderMenu.add_command(label="Open Folder", 
                           command=lambda: utils.loadFolderAction(infoView, prevButton, nextButton,))
    
    menubar.add_cascade(label="File", menu=folderMenu)
    
    root.config(menu=menubar)
    
    imageView = Label(root,
                      image=None,)
    
    infoView = Label(root, 
                     text="Image None of None",
                     fg="#fff",
                     bg="#303030",
                     font=("Roboto", 16, "bold"),
                     bd=1,
                     relief=SUNKEN,)
    
    prevButton = Button(root,
                        text="<",
                        fg="#fff",
                        bg="#5600ff",
                        padx=10,
                        pady=10,
                        font=("Roboto", 16, "bold"),
                        command= lambda: utils.prevImage(imageView, infoView),
                        state=DISABLED,)
    
    nextButton = Button(root,
                        text=">",
                        fg="#fff",
                        bg="#5600ff",
                        padx=10,
                        pady=10,
                        font=("Roboto", 16, "bold"),
                        command= lambda: utils.nextImage(imageView, infoView),
                        state=DISABLED,)
    
    prevButton.grid(column=0, row=0)
    imageView.grid(column=1, row=0)
    nextButton.grid(column=2, row=0)
    infoView.grid(column=1, row=1, sticky=W+E)
    
    root.after(0, lambda: utils.initViewLabel(imageView))

    root.mainloop()