import customtkinter
from tkinter import *
from tkinter import messagebox
from needleman import *


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x600")


def button_nw():
    print(initializare(sec1, sec2, main, nw_zeros_check))
def button_sw():
    pass
def button_b():
    pass


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

button = customtkinter.CTkButton(master=frame,
                                 text="Needleman Wunsch",
                                 bg_color="#badee2",
                                 fg_color="blue",
                                 cursor="hand2",
                                 command= button_nw)
button.place(relx=0.2, rely=0.5, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=frame,
                                 text="Smith-Waterman",
                                 bg_color="#badee2",
                                 fg_color="blue",
                                 cursor="hand2")

button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=frame, text="Beteringhe")
button.place(relx=0.8, rely=0.5, anchor=customtkinter.CENTER)

root.mainloop()