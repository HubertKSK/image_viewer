#!/usr/bin python3
"""Przeglądarka obrazów TKinter"""
from tkinter import *
from PIL import ImageTk, Image
import os
import argparse
import numpy as np

# Parser
# wywołanie:
# python3 image_viewer.py -f /path/to/folder
PARSER = argparse.ArgumentParser()
PARSER.add_argument("-f", "--folder", required=True,
                    help="Path to the image folder")
ARGS = PARSER.parse_args()

# przeszukiwanie katalogu w celu znalaeźienie plików kończących się na:
# .png, .jpg, .jpeg
image_list_loc = []
for file in os.listdir(ARGS.folder):
    if (file.endswith(".jpg")) or (file.endswith(".png")) or (file.endswith(".jpeg")):
        image_list_loc.append(os.path.join(ARGS.folder, file))
# print("Images List: ", image_list_loc)

root = Tk()
root.title('Przeglądarka obrazów')
# root.iconbitmap("aplication_tool_based_bold-14-512.png")

image_num = 0
max_len = len(image_list_loc)
my_img = ImageTk.PhotoImage(Image.open(image_list_loc[image_num]))

image_list = []
for x, value in enumerate(image_list_loc):
    image_list.append(ImageTk.PhotoImage(Image.open(image_list_loc[x])))

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global max_len

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == max_len:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Wyjdź z programu", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
