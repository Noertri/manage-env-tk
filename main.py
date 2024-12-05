import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import os
from pathlib import Path


class Tabel(ttk.Treeview):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, show="headings", *args, **kwargs)
        
        self.heading(0, text="Variable", anchor="center")
        self.heading(1, text="Values", anchor="center")
        self.column(0, width=200)
        self.column(1, width=300)
        self.bind("<Motion>", "break")
        self.insert_envs()

    def insert_envs(self):
        for item in dict(os.environ).items():
            self.insert("", index=tk.END, values=item)

        
class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Environment Variables")
        # self.geometry("500x500")
        
        main_style = ttk.Style()
        main_style.configure("Treeview.Heading", font=tkfont.Font(weight="normal", size=10))

        # frame utama
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(anchor="center", padx=(20, 20), pady=(20, 20))
        
        # label frame
        self.label_frame1 = ttk.LabelFrame(self.main_frame, text="User Variables", padding=(10, 10, 10, 10))
        self.label_frame1.pack(anchor="center")

        # tabel
        self.tabel = Tabel(self.label_frame1, column=(0, 1), height=8)
        self.tabel.pack(anchor="center")

        # frame tombol new, edit, dan delete
        self.btn_frame = ttk.Frame(self.label_frame1)
        self.btn_frame.pack(after=self.tabel, pady=(10, 0), anchor="e")

        # tombol new
        self.btn_new = ttk.Button(self.btn_frame, text="New")
        self.btn_new.pack(side="left")

        # tombol edit
        self.btn_edit = ttk.Button(self.btn_frame, text="Edit")
        self.btn_edit.pack(padx=(5, 0), side="left")

        # tombol delete
        self.btn_del = ttk.Button(self.btn_frame, text="Delete")
        self.btn_del.pack(padx=(5, 0), side="left")

        # frame tombol konfirmasi
        self.confirm_frame = ttk.Frame(self.main_frame)
        self.confirm_frame.pack(anchor="e", pady=(20, 0))

        # tombol ok
        self.btn_ok = ttk.Button(self.confirm_frame, text="OK")
        self.btn_ok.pack(side="left")

        # tombol cancel
        self.btn_cancel = ttk.Button(self.confirm_frame, text="Cancel", command=self.btn_cancel_callback)
        self.btn_cancel.pack(padx=(5, 0), side="left")

    def btn_cancel_callback(self, event=None):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.resizable(False, False)
    app.mainloop()
