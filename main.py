import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import os
from pathlib import Path
import pickle
from popup_windows import NewBtnWindow


class Tabel(ttk.Treeview):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, show="headings", *args, **kwargs)
        
        self.parent = parent
        
        self.heading(0, text="Variable", anchor="center")
        self.heading(1, text="Values", anchor="center")
        self.column(0, width=200)
        self.column(1, width=300)
        self.bind("<Motion>", "break")

        # memuat environment variables
        self.load_env_vars()

    def load_env_vars(self):
        for item in sorted(dict(os.environ).items(), key=lambda x: x[0]):
            self.insert("", index=tk.END, values=item)


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Environment Variables")
        # self.geometry("500x500")
        self.resizable(False, False)
        
        main_style = ttk.Style()
        main_style.configure("Treeview.Heading", font=tkfont.Font(weight="normal"))

        # frame utama
        main_frame = ttk.Frame(self)
        main_frame.pack(anchor="center", padx=(20, 20), pady=(20, 20))
        
        # label frame
        label_frame1 = ttk.LabelFrame(main_frame, text="User Variables", padding=(10, 10, 10, 10))
        label_frame1.pack(anchor="center")

        # tabel
        self.tabel = Tabel(label_frame1, column=(0, 1), height=8)
        self.tabel.pack(anchor="center")

        # frame tombol new, edit, dan delete
        btn_frame = ttk.Frame(label_frame1)
        btn_frame.pack(pady=(10, 0), anchor="e", side="bottom")

        # tombol new
        btn_new = ttk.Button(btn_frame, text="New", command=self.btn_new_callback)
        btn_new.pack(side="left")

        # tombol edit
        btn_edit = ttk.Button(btn_frame, text="Edit")
        btn_edit.pack(padx=(5, 0), side="left")

        # tombol delete
        btn_del = ttk.Button(btn_frame, text="Delete")
        btn_del.pack(padx=(5, 0), side="left")

        # frame tombol konfirmasi
        confirm_frame = ttk.Frame(main_frame)
        confirm_frame.pack(anchor="e", pady=(20, 0))

        # tombol ok
        btn_ok = ttk.Button(confirm_frame, text="OK", command=self.btn_ok_callback)
        btn_ok.pack(side="left")

        # tombol cancel
        btn_cancel = ttk.Button(confirm_frame, text="Cancel", command=self.btn_cancel_callback)
        btn_cancel.pack(padx=(5, 0), side="left")

        self.new_btn_win = None

    def btn_ok_callback(self):
        print("Data has been submitted")
        self.destroy()

    def btn_cancel_callback(self):
        print("Program is closed")
        self.destroy()

    def btn_new_callback(self):
        self.new_btn_win = NewBtnWindow(self)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
