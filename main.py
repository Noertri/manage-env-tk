import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import os
from pathlib import Path
import re
import subprocess
from popup_windows import NewBtnWindow, EditBtnWindow


class Tabel(ttk.Treeview):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, show="headings", *args, **kwargs)
        
        self.parent = parent
        self.selected_items = []
        
        self.heading(0, text="Variable", anchor="center")
        self.heading(1, text="Values", anchor="center")
        self.column(0, width=250)
        self.column(1, width=300)
        self.bind("<Motion>", "break")

        # memuat environment variables
        self.load_env_vars()

    def load_env_vars(self):
        for item in sorted(dict(os.environ).items(), key=lambda x: x[0]):
            self.insert("", index=tk.END, values=item)


class TabelPanel(ttk.LabelFrame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, text="User Variables", padding=(10, 10, 10, 10), *args, **kwargs)
        self.parent = parent

        # tabel
        self.tabel = Tabel(self, column=(0, 1), height=10)
        self.tabel.bind("<<TreeviewSelect>>", self.treeview_selection_handler)
        self.tabel.pack(fill="both")

        # frame tombol new, edit, dan delete
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=(25, 0), anchor="se", side="bottom")

        # tombol new
        btn_new = ttk.Button(btn_frame, text="New", command=lambda : NewBtnWindow(self))
        btn_new.pack(side="left")

        # tombol edit
        self.btn_edit = ttk.Button(btn_frame, text="Edit")
        self.btn_edit.pack(padx=(5, 0), side="left")

        # tombol delete
        self.btn_del = ttk.Button(btn_frame, text="Delete")
        self.btn_del.pack(padx=(5, 0), side="left")

    def btn_del_callback(self, selected_items):
        try:
            items = self.tabel.item(selected_items)["values"]
            print(items)
            self.tabel.delete(selected_items)
        except Exception as e:
            raise e

    def treeview_selection_handler(self, event):
        for item in self.tabel.selection():
            selected_items = self.tabel.item(item)["values"]
            setattr(self, "selected_items", selected_items)
            self.btn_edit.configure(command=lambda : EditBtnWindow(self))
            self.btn_del.configure(command=lambda : self.btn_del_callback(item))


class MainWindow(tk.Tk):

    def __init__(self, app_title):
        super().__init__()
        self.title(app_title)
        # self.geometry("500x500")
        self.resizable(False, False)
        
        # inisialisai program
        self.env_file_path = Path("{0}/.environment".format(Path.home()))
        self.env_vars = dict(sorted(os.environ.items(), key=lambda x: x[0]))
        self.app_data = {
            "env_file": self.load_env_file()
        }
        self.init_app()
        setattr(TabelPanel, "app_data", self.app_data)

        main_style = ttk.Style()
        main_style.configure("Treeview.Heading", font=tkfont.Font(weight="normal"))

        # frame utama
        main_frame = ttk.Frame(self)
        main_frame.pack(padx=(20, 20), pady=(20, 20), anchor="nw")
        
        # tabel frame
        self.tabel_panel = TabelPanel(main_frame)
        self.tabel_panel.pack(anchor="center")
        
        self.tabel = self.tabel_panel.tabel

        # frame tombol konfirmasi
        confirm_frame = ttk.Frame(main_frame)
        confirm_frame.pack(side="bottom", pady=(25, 0), anchor="se")

        # tombol ok
        btn_ok = ttk.Button(confirm_frame, text="OK", command=self.btn_ok_callback)
        btn_ok.pack(side="left")

        # tombol close
        btn_close = ttk.Button(confirm_frame, text="Close", command=self.btn_close_callback)
        btn_close.pack(padx=(5, 0), side="left")

    def init_app(self):
        bashrc_path = Path("{0}/.bashrc".format(Path.home()))
        
        script = 'if [ -f ~/.environment ]; then\n\tset -a\n\tsource ~/.environment\n\tset +a\nfi'

        if not self.env_file_path.exists():
            self.env_file_path.touch()

            with bashrc_path.open("a", encoding="utf-8") as f:
                f.write("\n"+script.strip()+"\n")
                f.close()

    def load_env_file(self):
        pattern = re.compile(r'([_A-Za-z0-9]+?)="(.*)"|([_A-Za-z0-9]+?)=(.*)')

        env = dict()

        if self.env_file_path.exists():
            with self.env_file_path.open("r", encoding="utf-8") as f:
                for line in f.readlines():
                    if line.startswith("#"):
                        continue
                    matched = pattern.search(line.strip())
                    env[matched.group(1).strip()] = matched.group(2).strip()
                f.close()

        return env

    def btn_ok_callback(self):
        with self.env_file_path.open("w", encoding="utf-8") as f:
            for k, v in self.app_data["env_file"].items():
                f.write(f'{k}="{v}"\n')
            f.close()

        print("Variables has been saved")
        self.destroy()

    def btn_close_callback(self):
        print("Program is closed")
        self.destroy()


if __name__ == "__main__":
    app = MainWindow("Environment Variables")
    app.mainloop()
