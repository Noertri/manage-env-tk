import tkinter as tk
from tkinter import ttk


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

        frame3 = ttk.Frame(frame0)
        frame3.pack(anchor=tk.E, pady=(10, 0))

        label1 = ttk.Label(frame1, text="Variable", width=10)
        label1.grid(column=0, row=0, sticky=tk.W)

        label2 = ttk.Label(frame2, text="Value(s)", width=10)
        label2.grid(column=0, row=1, sticky=tk.W)

        # entry box untuk variabel baru
        self.new_var = ttk.Entry(frame1, width=32, textvariable=self.new_var_data)
        self.new_var.grid(column=1, row=0, sticky=tk.W)

        # entry box untuk nilai variabel baru
        self.new_values = ttk.Entry(frame2, width=32, textvariable=self.new_values_data)
        self.new_values.grid(column=1, row=1, sticky=tk.W)

        # tombol add
        self.btn_add = ttk.Button(frame3, text="Add", command=self.btn_add_callback)
        self.btn_add.pack(side="left")

        # tombol cancel
        self.btn_cancel = ttk.Button(frame3, text="Cancel", command=self.btn_cancel_callback)
        self.btn_cancel.pack(padx=(5, 0), side="left")

    def btn_add_callback(self):
        self.parent.tabel.insert("", index=0, values=(self.new_var_data.get(), self.new_values_data.get()))
        self.parent.data["env_file"][self.new_var_data.get()] = self.new_values_data.get()
        self.destroy()

    def btn_cancel_callback(self):
        print("Task is aborted")
        self.destroy()


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
