import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pathlib import Path


class NewBtnWindow(tk.Toplevel):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.new_var_data = tk.StringVar()
        self.new_values_data = tk.StringVar()

        self.title("New Variable")
        self.resizable(False, False)

        frame0 = ttk.Frame(self, relief="sunken", padding=(10, 10, 10, 10))
        frame0.pack(padx=(20, 20), pady=(20, 20))

        frame1 = ttk.Frame(frame0)
        frame1.pack(anchor="center")

        frame2 = ttk.Frame(frame0)
        frame2.pack(anchor="center", pady=(10, 0))

        btn_frame = ttk.Frame(frame0)
        btn_frame.pack(anchor="se", pady=(25, 0), side="right")

        btn_frame2 = ttk.Frame(frame0)
        btn_frame2.pack(anchor="sw", pady=(25, 0))

        label1 = ttk.Label(frame1, text="Variable", width=10)
        label1.grid(column=0, row=0, sticky=tk.W)

        label2 = ttk.Label(frame2, text="Value(s)", width=10)
        label2.grid(column=0, row=1, sticky=tk.W)

        # entry box untuk variabel baru
        new_var = ttk.Entry(frame1, width=52, textvariable=self.new_var_data)
        new_var.grid(column=1, row=0, sticky=tk.W)

        # entry box untuk nilai variabel baru
        new_values = ttk.Entry(frame2, width=52, textvariable=self.new_values_data)
        new_values.grid(column=1, row=1, sticky=tk.W)

        # tombol browse
        btn_browse = ttk.Button(btn_frame2, text="Browse", command=self.btn_browse_callback)
        btn_browse.pack()

        # tombol add
        btn_add = ttk.Button(btn_frame, text="Add", command=self.btn_add_callback)
        btn_add.pack(side="left")

        # tombol cancel
        btn_cancel = ttk.Button(btn_frame, text="Cancel", command=self.btn_cancel_callback)
        btn_cancel.pack(padx=(10, 0))

    def btn_add_callback(self):
        self.parent.tabel.insert("", index=0, values=(self.new_var_data.get(), self.new_values_data.get()))
    
        if (k := self.new_var_data.get()) and (v := self.new_values_data.get()):
            self.parent.data["env_file"][k] = v

        self.destroy()

    def btn_cancel_callback(self):
        print("Task is aborted")
        self.destroy()

    def btn_browse_callback(self):
        pass


class EditBtnWindow(tk.Toplevel):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

        self.title("Edit Variable")
        # self.resizable(False, False)

        frame = ttk.Frame(self)
        frame.pack(anchor="nw", padx=(20, 20), pady=(20, 20))

        entry_frame = ttk.Frame(frame)
        entry_frame.pack(side="left")

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side="left", padx=(10, 0))

        label1 = ttk.Label(entry_frame, text="Variable", width=10)
        label1.grid(column=0, row=0)

        entry1 = ttk.Entry(entry_frame, width=32, state="disable")
        entry1.grid(column=1, row=0)

        btn1 = ttk.Button(btn_frame, text="OK")
        btn1.pack()
