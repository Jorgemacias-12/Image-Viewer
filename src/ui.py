from tkinter import *
from PIL import Image, ImageTk
import os
import requests
import tkinter.filedialog as fd
import tkinter.messagebox as mb

def nextImage(viewLabel, infoLabel):
    return


def prevImage(viewLabel, infoLabel):
    return


def initViewLabel(label):
    plcURL = "https://via.placeholder.com/600x400.jpg?text=Example"
    placeHolderImage = ImageTk.PhotoImage(
        Image.open(requests.get(plcURL, stream=True).raw))
    label.image = placeHolderImage
    label.config(image=placeHolderImage)
    label.update_idletasks()
    
def initButtonAcitvity(prevButton, nextButton):

    prevButton.config(text="<",
                      fg="#FFF",
                      bg="#5600ff",
                      padx=10,
                      pady=10,
                      font=("Roboto", 16, "bold"),
                      state='active')

    nextButton.config(text=">",
                      fg="#FFF",
                      bg="#5600ff",
                      padx=10,
                      pady=10,
                      font=("Roboto", 16, "bold"),
                      state='active')

    prevButton.update_idletasks()
    nextButton.update_idletasks()


photosPath = []
totalImages = 0

def loadFolderAction(infoLabel, prevButton, nextButton, viewLabel):

    global totalImages

    photosDir = fd.askdirectory(
        title="Select a folder",
        initialdir="./",
    )

    global photosPath

    for file in os.listdir(photosDir):
        if file.endswith(".jpg"):
            photosPath.append(photosDir + "/" + file)
            totalImages += 1

    if (totalImages != 0):
        totalImagesCount = totalImages
        infoLabel.config(text="Image 1 of " + str(totalImagesCount))
        initButtonAcitvity(prevButton, nextButton)
    if (totalImages == 0):
        mb.showerror("Error", "No images found in the folder")


