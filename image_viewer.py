#!/usr/bin python3
"""Przeglądarka obrazów TKinter"""
from tkinter import *
from PIL import ImageTk, Image
import os
import argparse

# Parser
# wywołanie:
# python3 image_viewer.py -f /path/to/folder
PARSER = argparse.ArgumentParser()
PARSER.add_argument("-f", "--folder", required=True,
                    help="Path to the image folder")
ARGS = PARSER.parse_args()

# przeszukiwanie katalogu w celu znalaeźienie plików kończących się na:
# .png, .jpg, .jpeg
image_list = []
for file in os.listdir(ARGS.folder):
    if (file.endswith(".jpg")) or (file.endswith(".png")) or (file.endswith(".jpeg")):
        IMAGES_LIST.append(os.path.join(ARGS.folder, file))
print("Images List: ", image_list)

root = Tk()
root.title('Przeglądarka obrazów')
root.iconbitmap("aplication_tool_based_bold-14-512.png")

# Old
# my_img1 = ImageTk.PhotoImage(Image.open("1.jpg"))
# my_img2 = ImageTk.PhotoImage(Image.open("2.jpg"))
# my_img3 = ImageTk.PhotoImage(Image.open("3.jpeg"))
# my_img4 = ImageTk.PhotoImage(Image.open("4.jpg"))

# New
# FIXME:
image_num = 0
my_img1 = ImageTk.PhotoImage(Image.open(image_list[image_num])

# FIXME:
# Tutaj mam error:
# SyntaxError: invalid syntax
my_label=Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward=Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back=Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back=Button(root, text="<<", command=back, state=DISABLED)
button_exit=Button(root, text="Wyjdź z programu", command=root.quit)
button_forward=Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
