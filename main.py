import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import os
from pathlib import Path
import pickle
import shutil
import re
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


class TabelFrame(ttk.LabelFrame):

    def __init__(self, parent, data, *args, **kwargs):
        super().__init__(parent, text="User Variables", padding=(10, 10, 10, 10), *args, **kwargs)
        self.parent = parent
        self.data = data

        # tabel
        self.tabel = Tabel(self, column=(0, 1), height=8)
        self.tabel.pack(anchor="nw")

        # frame tombol new, edit, dan delete
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=(10, 0), anchor="se", side="bottom")

        # tombol new
        btn_new = ttk.Button(btn_frame, text="New", command=self.btn_new_callback)
        btn_new.pack(side="left")

        # tombol edit
        btn_edit = ttk.Button(btn_frame, text="Edit")
        btn_edit.pack(padx=(5, 0), side="left")

        # tombol delete
        btn_del = ttk.Button(btn_frame, text="Delete")
        btn_del.pack(padx=(5, 0), side="left")

    def btn_new_callback(self):
        self.new_btn_win = NewBtnWindow(self)


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
            "new": [],
            "edit": [],
            "env_file": dict()
        }
        self.init_app()
        self.load_env_file()

        main_style = ttk.Style()
        main_style.configure("Treeview.Heading", font=tkfont.Font(weight="normal"))

        # frame utama
        main_frame = ttk.Frame(self)
        main_frame.pack(anchor="center", padx=(20, 20), pady=(20, 20))
        
        # tabel frame
        self.tabel_frame1 = TabelFrame(main_frame, self.app_data)
        self.tabel_frame1.pack(anchor="nw")

        self.tabel: Tabel = self.tabel_frame1.tabel

        # frame tombol konfirmasi
        confirm_frame = ttk.Frame(main_frame)
        confirm_frame.pack(side="bottom", anchor="se", pady=(10, 0))

        # tombol ok
        btn_ok = ttk.Button(confirm_frame, text="OK", command=self.btn_ok_callback)
        btn_ok.pack(side="left")

        # tombol close
        btn_close = ttk.Button(confirm_frame, text="Close", command=self.btn_close_callback)
        btn_close.pack(padx=(5, 0), side="left")

        self.new_btn_win = None

    def init_app(self):
        bashrc_path = Path("{0}/.bashrc".format(Path.home()))
        profile_path = Path("{0}/.profile".format(Path.home()))
        
        script = 'if [ -f ~/.environment ]; then\n\tset -a\n\tsource ~/.environment\n\tset +a\nfi'

        if not self.env_file_path.exists():
            self.env_file_path.touch()

            with bashrc_path.open("a", encoding="utf-8") as f:
                f.write("\n"+script.strip()+"\n")
                f.close()

            with profile_path.open("a", encoding="utf-8") as f:
                f.write(script.strip()+"\n")
                f.close()

    def load_env_file(self):
        pattern = re.compile(r'([_A-Za-z0-9]+?)="(.*)"|([_A-Za-z0-9]+?)=(.*)')

        if self.env_file_path.exists():
            with self.env_file_path.open("r", encoding="utf-8") as f:
                for line in f.readlines():
                    if line.startswith("#"):
                        continue
                    matched = pattern.search(str(line.strip()))
                    print("{0}".format({matched.group(1): matched.group(2)}))
                f.close()

        return {}

    def btn_ok_callback(self):
        print("Data has been submitted")
        print(self.app_data)
        self.destroy()

    def btn_close_callback(self):
        print("Program is closed")
        self.destroy()


if __name__ == "__main__":
    app = MainWindow("Environment Variables")
    app.mainloop()
