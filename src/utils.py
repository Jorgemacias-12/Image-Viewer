import requests
from tkinter import *
from PIL import Image, ImageTk

def initViewLabel(label):
    plcURL = "https://via.placeholder.com/600x400.jpg?text=Example"
    placeHolderImage = ImageTk.PhotoImage(Image.open(requests.get(plcURL, stream=True).raw))
    label.config(image=placeHolderImage)
    label.update_idletasks()