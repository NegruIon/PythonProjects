from tkinter import filedialog
from tkinter import *
import tkinter as tk
import os


root = Tk()
root.iconbitmap(os.path.join("images", "folder.ico"))
root.title("File Showing")
root.geometry('1000x800')


def choose_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        listbox.delete(0, END)
        error_label.config(text="")
        main_label.config(text="Path: "+folder_selected)
        main_folder_name.config(text=os.path.basename(folder_selected))
        display_files(folder_selected, number_of_spaces)
    else:
        main_label.config(text="")
        main_folder_name.config(text="")
        listbox.delete(0, END)
        error_label.config(text="Choose a valid path/folder!")


number_of_spaces = 4


def display_files(folder_selected_path, number_of_spaces):
    number_of_spaces += 4
    for name in os.listdir(folder_selected_path):
        anm = " "*number_of_spaces + name
        listbox.insert('end', anm)
        if os.path.isdir(folder_selected_path+os.sep +
                         os.sep+name):
            listbox.itemconfig("end", {'fg': 'black'})
            display_files(folder_selected_path+os.sep +
                          os.sep+name, number_of_spaces)


choose_folder_img = tk.PhotoImage(
    file=os.path.join("images", "folder_select.png"))

choose_folder_btn = tk.Button(
    root, image=choose_folder_img, command=choose_folder, borderwidth=0)
choose_folder_btn.pack()

informative_label_2 = tk.Label(
    root, text="Folders(Black)", font=('poppins', 10))
informative_label_2.pack(pady=2, side=TOP, anchor="w")
informative_label_1 = tk.Label(
    root, text="Files(Gray)", fg="gray", font=('poppins', 10))
informative_label_1.pack(side=TOP, anchor="w")

error_label = tk.Label(root, text="", fg="red", font=('poppins', 13))
error_label.pack()

main_label = tk.Label(root, text="", font=('poppins', 15))
main_label.pack(pady=2, side=TOP, anchor="w")

main_folder_name = tk.Label(root, font=('poppins', 15))
main_folder_name.pack(pady=2, side=TOP, anchor="w")

listbox = Listbox(root, borderwidth=0, bg="#f0f0f0",
                  fg="gray", font=('poppins', 13))
listbox.pack(expand=tk.YES, fill=tk.BOTH)


root.mainloop()
