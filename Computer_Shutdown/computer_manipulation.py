import tkinter as tk
from tkinter import Text
import os
from tkinter import *
import time
import platform


root = tk.Tk()
if platform.system() == "Darwin":
    root.title("MacOS Shutdown")
else:
    root.title(platform.system() + " Shutdown")


root.iconbitmap(os.path.join("images", "computer.ico"))
root.resizable(False, False)
root.geometry('400x600')

ready_time = IntVar()


def main_function():
    try:
        ready_time = int(e1.get())
        error_label.config(text="")
        e1.config(highlightthickness=2,
                  highlightbackground="#57de54", highlightcolor="#57de54")
        return ready_time
    except ValueError:
        error_label.config(text="Enter a valid integer!")
        e1.config(highlightthickness=2,
                  highlightbackground="red", highlightcolor="red")


def sleep():
    result = main_function()
    if result:
        if platform.system() == "Windows":
            time.sleep(result)
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif platform.system() == "Darwin":
            os.system("sudo shutdown -s +" + ready_time)
        else:
            os.system(f"echo 'pm-suspend' | at now + {ready_time} seconds")


def restart():
    result = main_function()
    if result:
        if platform.system() == "Windows":
            os.system("shutdown /r /t " + str(result))
        elif platform.system() == "Darwin":
            os.system("sudo shutdown -r +" + ready_time)
        else:
            time.sleep(result)
            os.system("reboot")


def shutdown():
    result = main_function()
    if result:
        if platform.system() == "Windows":
            os.system("shutdown /s /t " + str(result))
        elif platform.system() == "Darwin":
            time.sleep(result)
            os.system("sudo shutdown -h")
        else:
            time.sleep(result)
            os.system("shutdown -h now")


main_label = tk.Label(root, text="Please Enter The Time(s):",
                      font=('poppins', 15), pady=30)
main_label.pack()


e1 = tk.Entry(root, borderwidth=0, justify=CENTER, font=('poppins', 25))
e1.pack(padx=70, pady=10)

error_label = tk.Label(root, text='', fg="red", font=('poppins', 10))
error_label.pack(pady=5)


# Add background image to sleep btn
sleep_btn = tk.PhotoImage(file=os.path.join("images", "Sleep.png"))

# Sleep btn
put_to_sleep = tk.Button(root, image=sleep_btn,
                         borderwidth=0, command=sleep)
put_to_sleep.pack()
put_to_sleep.place(relx=0.5, rely=0.57, anchor=CENTER)


# Add background image to sleep btn
shutdown_btn = tk.PhotoImage(file=os.path.join("images", "Shutdown.png"))

# Shutdown btn
shutdown_computer = tk.Button(
    root, image=shutdown_btn, padx=87, pady=5, borderwidth=0, command=shutdown)
shutdown_computer.pack()
shutdown_computer.place(relx=0.5, rely=0.7, anchor=CENTER)


# Add background image to sleep btn
restart_btn = tk.PhotoImage(file=os.path.join("images", "Restart.png"))

# Restart btn
restart_computer = tk.Button(
    root, image=restart_btn, padx=96, pady=5, borderwidth=0, command=restart)
restart_computer.pack()
restart_computer.place(relx=0.5, rely=0.83, anchor=CENTER)

root.mainloop()
