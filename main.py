import tkinter as tk
from tkinter import ttk
import os
from pathlib import Path


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Environment Variables")
        # self.geometry("500x500")
        
        # frame utama
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(column=0, row=0, padx=(20, 20), pady=(20, 20))
        
        # label frame
        self.label_frame1 = ttk.LabelFrame(self.main_frame, text="User Variables", padding=(10, 10, 10, 10))
        self.label_frame1.grid(column=0, row=0)

        self.tree_view = ttk.Treeview(self.label_frame1, columns=["Name"])
        self.tree_view.grid(column=0, row=0)

        # frame tombol new, edit, dan delete
        self.btn_frame = ttk.Frame(self.label_frame1)
        self.btn_frame.grid(column=0, row=1, sticky="E", pady=(10, 0))

        # tombol new
        self.btn_new = ttk.Button(self.btn_frame, text="New")
        self.btn_new.grid(column=0, row=0)

        # tombol edit
        self.btn_edit = ttk.Button(self.btn_frame, text="Edit")
        self.btn_edit.grid(column=1, row=0, padx=(5, 0))

        # tombol delete
        self.btn_del = ttk.Button(self.btn_frame, text="Delete")
        self.btn_del.grid(column=2, row=0, padx=(5, 0))

        # frame tombol konfirmasi
        self.confirm_frame = ttk.Frame(self.main_frame)
        self.confirm_frame.grid(column=0, row=1, sticky="E", pady=(20, 0))

        # tombol ok
        self.btn_ok = ttk.Button(self.confirm_frame, text="OK")
        self.btn_ok.grid(column=0, row=0)

        # tombol cancel
        self.btn_ok = ttk.Button(self.confirm_frame, text="Cancel")
        self.btn_ok.grid(column=1, row=0, padx=(5, 0))


if __name__ == "__main__":
    app = App()
    app.resizable(False, False)
    app.mainloop()
