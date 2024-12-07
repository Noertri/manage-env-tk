import tkinter as tk
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

        frame0 = ttk.Frame(self, padding=(10, 10, 10, 10), relief="sunken")
        frame0.pack(padx=(20, 20), pady=(20, 20), anchor="nw")

        frame1 = ttk.Frame(frame0)
        frame1.pack()

        frame2 = ttk.Frame(frame0)
        frame2.pack(pady=(10, 0))

        btn_frame = ttk.Frame(frame0)
        btn_frame.pack(anchor="se", pady=(25, 0), side="right")

        label1 = ttk.Label(frame1, text="Variable", width=10)
        label1.grid(column=0, row=0, sticky=tk.W)

        label2 = ttk.Label(frame2, text="Value(s)", width=10)
        label2.grid(column=0, row=1, sticky=tk.W)

        # entry box untuk variabel baru
        new_var = ttk.Entry(frame1, width=26, textvariable=self.new_var_data)
        new_var.grid(column=1, row=0, sticky=tk.W)

        # entry box untuk nilai variabel baru
        new_values = ttk.Entry(frame2, width=26, textvariable=self.new_values_data)
        new_values.grid(column=1, row=1, sticky=tk.W)

        # tombol add
        btn_add = ttk.Button(btn_frame, text="Add", command=self.btn_add_callback)
        btn_add.pack(side="left")

        # tombol cancel
        btn_cancel = ttk.Button(btn_frame, text="Cancel", command=self.btn_cancel_callback)
        btn_cancel.pack(padx=(10, 0))

    def btn_add_callback(self):
        if (k := self.new_var_data.get().strip()) and (v := self.new_values_data.get().strip()):
            self.parent.tabel.insert("", index=0, values=(k, v))
            self.parent.app_data["env_file"][k] = v
            self.destroy()

    def btn_cancel_callback(self):
        print("Task is aborted")
        self.destroy()


class TextBoxPanel(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.data = parent.selected_items
        selected_values = self.data[1].replace(":", "\n") if len(self.data[1]) > 40 else self.data[1]

        main_frame = ttk.Frame(self, padding=(10, 10, 10, 10), relief="sunken")
        main_frame.pack()
        
        # bagian yang menampilkan nama variabel yang dipilih
        label = ttk.Label(main_frame, text="Variable:", width=10)
        label.grid(column=0, row=0, sticky=tk.NW)

        var_name = ttk.Entry(main_frame)
        var_name.insert(0, self.data[0])
        var_name.grid(column=1, row=0, sticky=tk.W+tk.E, padx=(10, 0))

        # bagian yang menampilkan nilai variabel yang dipilih
        text_box_frame = ttk.Frame(main_frame)
        text_box_frame.grid(column=1, row=1, sticky=tk.NW+tk.SE)

        label2 = ttk.Label(main_frame, text="Value(s):", width=10)
        label2.grid(column=0, row=1, sticky=tk.NW, pady=(10, 0))

        val_entry = tk.Text(text_box_frame, height=8, width=40, wrap="none")
        val_entry.insert(tk.END, selected_values)
        val_entry.insert(tk.END, "\n")
        val_entry.grid(column=1, row=1, sticky=tk.NW+tk.SE, padx=(10,0), pady=(10, 0))

        # scrollbar sumbu x
        xscroll = tk.Scrollbar(text_box_frame, orient="horizontal")
        xscroll.configure(command=val_entry.xview)
        val_entry.configure(xscrollcommand=xscroll.set)
        xscroll.grid(column=1, row=2, sticky=tk.W+tk.E, padx=(10, 0))

        # scrollbar sumbu y
        yscroll = tk.Scrollbar(text_box_frame, orient="vertical")
        yscroll.configure(command=val_entry.yview)
        val_entry.configure(yscrollcommand=yscroll.set)
        yscroll.grid(column=2, row=1, sticky=tk.N+tk.S, pady=(10, 0))


class EditBtnWindow(tk.Toplevel):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

        self.title("Edit Variable")
        # self.resizable(False, False)

        frame0 = ttk.Frame(self)
        setattr(frame0, "selected_items", self.parent.selected_items)
        frame0.pack(anchor="nw", padx=(20, 20), pady=(20, 20))
        
        list_box_panel = TextBoxPanel(frame0)
        list_box_panel.pack()

        btn_frame = ttk.Frame(frame0)
        btn_frame.pack(side="bottom", anchor="se", pady=(25, 0))

        btn_ok = ttk.Button(btn_frame, text="OK")
        btn_ok.pack(side="left")

        btn_cancel = ttk.Button(btn_frame, text="Cancel", command=self.btn_cancel_callback)
        btn_cancel.pack(padx=(10, 0))

    def btn_cancel_callback(self):
        self.destroy()
