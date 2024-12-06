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


class ListBoxPanel(ttk.Frame):

    def __init__(self, parent, data, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.data = data

        list_box = tk.Listbox(self, width=30)
        list_box.pack(side="left")

        btn_frame = ttk.Frame(self)
        btn_frame.pack(anchor="n", padx=(10, 0))

        btn_new = ttk.Button(btn_frame, text="New")
        btn_new.pack()


class EditBtnWindow(tk.Toplevel):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

        self.title("Edit Variable")
        # self.resizable(False, False)

        frame0 = ttk.Frame(self)
        frame0.pack(anchor="nw", padx=(20, 20), pady=(20, 20))
        
        list_box_panel = ListBoxPanel(frame0, self.parent.tabel)
        list_box_panel.pack()

        btn_frame = ttk.Frame(frame0)
        btn_frame.pack(side="bottom", anchor="se", pady=(25, 0))

        btn_ok = ttk.Button(btn_frame, text="OK")
        btn_ok.pack(side="left")

        btn_cancel = ttk.Button(btn_frame, text="Cancel")
        btn_cancel.pack(padx=(10, 0))
