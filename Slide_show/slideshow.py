from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk


root = tk.Tk()
root.title("Image Slideshow Viewer : ")

image_paths = [
    r"C:\Users\91836\Pictures\Camera Roll\Bff\B612_20230802_113518_795.jpg",
    r"C:\Users\91836\Pictures\Camera Roll\Bff\B612_20230802_113810_421.jpg",
    r"C:\Users\91836\Pictures\Camera Roll\Bff\B612_20230802_114443_321.jpg",
    r"C:\Users\91836\Pictures\Camera Roll\Bff\B612_20230802_114743_140.jpg",
]

image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()


def update_image():
    for photo_image in cycle(photo_images):
        label.config(image=photo_image)
        root.update()
        time.sleep(5)


slideshow = cycle(photo_images)


def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()


play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()


root.mainloop()
