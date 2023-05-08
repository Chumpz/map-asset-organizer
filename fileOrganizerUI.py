import customtkinter
from tkinter.filedialog import askdirectory
import fileOrganizer as fileOrg
import time

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("400x270")



def browseDir():
    entry1.delete(0, 'end')
    path = askdirectory()
    entry1.insert(0, str(path))
    label1.configure(text='')

def organize_path():
    fileOrg.organize(directory=entry1.get())
    label1.configure(text='Done!')



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame, text="Select directory to organize.", font=("Verdana", 16))
label1.pack(pady=10, padx=5)

button1 = customtkinter.CTkButton(master=frame, text="Browse directory", command=browseDir)
button1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, width=255, placeholder_text="---Directory---")
entry1.pack(pady=16, padx=5)

button2 = customtkinter.CTkButton(master=frame, text="Organize", command=organize_path)
button2.pack(pady=12, padx=10)

label1 = customtkinter.CTkLabel(master=frame, text="", font=("Verdana", 8))
label1.pack(pady=1, padx=1)

def create_window():
    root.mainloop()
