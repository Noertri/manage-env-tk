import tkinter as tk
from tkinter import ttk, messagebox


class NewBtnWindow(tk.Toplevel):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.new_var_data = tk.StringVar()
        self.new_values_data = tk.StringVar()

        self.title("New Variable")
        self.resizable(False, False)
        self.geometry("500x200")

        frame0 = ttk.Frame(self, padding=(10, 10, 10, 10))
        frame0.pack(padx=(20, 20), pady=(20, 20), anchor="nw", fill="both")

        frame1 = ttk.Frame(frame0)
        frame1.pack(fill="both")

        btn_frame = ttk.Frame(frame0)
        btn_frame.pack(anchor="se", pady=(25, 0))

        # entry box untuk Variable
        label1 = ttk.Label(frame1, text="Variable:", width=10)
        label1.grid(column=0, row=0, sticky=tk.W)

        new_var = ttk.Entry(frame1, textvariable=self.new_var_data)
        new_var.grid(column=1, row=0, sticky=tk.W+tk.E)

        # entry box untuk Value(s)
        label2 = ttk.Label(frame1, text="Value(s):", width=10)
        label2.grid(column=0, row=1, pady=(10, 0), sticky=tk.W)

        new_values = ttk.Entry(frame1, textvariable=self.new_values_data, width=52)
        new_values.grid(column=1, row=1, pady=(10, 0), sticky=tk.W)

        # tombol save
        btn_save = ttk.Button(btn_frame, text="Save", command=self.btn_save_callback)
        btn_save.pack(side="left")

        # tombol cancel
        btn_cancel = ttk.Button(btn_frame, text="Cancel", command=self.btn_cancel_callback)
        btn_cancel.pack(padx=(10, 0))

    def btn_save_callback(self):
        self.parent.new_btn_window = None
        if (k := self.new_var_data.get().strip()) and (v := self.new_values_data.get().strip()):
            self.parent.tabel.insert("", index=0, values=(k, v))
            self.parent.app_data["env_file"][k] = v
            self.parent.app_data["btn_new_confirm"] = True
            self.destroy()
        else:
            messagebox.showerror("Invalid value", message="Variable and value(s) are empty!!!", parent=self)

    def btn_cancel_callback(self):
        self.parent.new_btn_window = None
        self.parent.app_data["btn_new_confirm"] = False
        self.destroy()


class TextBoxPanel(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.data = parent.selected_items
        selected_values = self.data[1].replace(":", "\n") if len(self.data[1]) > 40 else self.data[1]

        # bagian yang menampilkan nama variabel yang dipilih
        label = ttk.Label(self, text="Variable:", width=10)
        label.grid(column=0, row=0, sticky=tk.NW)

        self.var_input = ttk.Entry(self)
        self.var_input.insert(0, self.data[0])
        self.var_input.grid(column=1, row=0, sticky=tk.W+tk.E, padx=(10, 0))

        # bagian yang menampilkan nilai variabel yang dipilih
        text_box_frame = ttk.Frame(self)
        text_box_frame.grid(column=1, row=1, sticky=tk.NW+tk.SE)

        label2 = ttk.Label(self, text="Value(s):", width=10)
        label2.grid(column=0, row=1, sticky=tk.NW, pady=(10, 0))

        self.val_input = tk.Text(text_box_frame, height=8, width=52, wrap="none")
        self.val_input.insert(tk.END, selected_values)
        self.val_input.grid(column=1, row=1, sticky=tk.NW+tk.SE, padx=(10,0), pady=(10, 0))

        # scrollbar sumbu x
        xscroll = tk.Scrollbar(text_box_frame, orient="horizontal")
        xscroll.configure(command=self.val_input.xview)
        self.val_input.configure(xscrollcommand=xscroll.set)
        xscroll.grid(column=1, row=2, sticky=tk.W+tk.E, padx=(10, 0))

        # scrollbar sumbu y
        yscroll = tk.Scrollbar(text_box_frame, orient="vertical")
        yscroll.configure(command=self.val_input.yview)
        self.val_input.configure(yscrollcommand=yscroll.set)
        yscroll.grid(column=2, row=1, sticky=tk.N+tk.S, pady=(10, 0))

        
class EditBtnWindow(tk.Toplevel):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

        self.title("Edit Variable")
        self.resizable(False, False)

        frame0 = ttk.Frame(self, padding=(10, 10, 10, 10))
        setattr(frame0, "selected_items", self.parent.selected_items)
        setattr(frame0, "app_data", self.parent.app_data)
        frame0.pack(anchor="nw", padx=(20, 20), pady=(20, 20))
        
        self.text_panel = TextBoxPanel(frame0)
        self.text_panel.pack(anchor="nw")

        btn_frame = ttk.Frame(frame0)
        btn_frame.pack(side="bottom", anchor="se", pady=(25, 0))

        btn_save = ttk.Button(btn_frame, text="Save", command=self.btn_save_callback)
        btn_save.pack(side="left")

        btn_cancel = ttk.Button(btn_frame, text="Cancel", command=self.btn_cancel_callback)
        btn_cancel.pack(padx=(10, 0))

    def btn_cancel_callback(self):
        self.parent.edit_btn_window = None
        self.parent.app_data["btn_edit_confirm"] = False
        self.destroy()

    def btn_save_callback(self):
        self.parent.edit_btn_window = None
        if hasattr(self.parent, "app_data"):
            self.parent.app_data["btn_edit_confirm"] = True
            
            # simpan data ke app_data
            if (k := self.text_panel.var_input.get()) and (v := self.text_panel.val_input.get("1.0", tk.END).strip()):
                self.parent.app_data["env_file"][k] = v.replace("\n", ":")
                print(self.parent.app_data)

                # self.destroy()
