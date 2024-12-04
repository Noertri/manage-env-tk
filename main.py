import tkinter as tk
from tkinter import ttk
import os
from pathlib import Path


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Environment Variables")
        # self.geometry("500x500")

        self.label_frame1 = ttk.LabelFrame(self, text="User Variables")
        self.label_frame1.grid(column=0, row=0, padx=5, pady=5)

        self.frame1 = ttk.Frame(self.label_frame1, padding=(5, 5, 5, 5))
        self.frame1.grid(column=0, row=0)

        self.frame2 = ttk.Frame(self.label_frame1, padding=(5, 5, 5, 5))
        self.frame2.grid(column=0, row=1, sticky="E")
        
        self.tree_view = ttk.Treeview(self.frame1, columns=["Name"])
        self.tree_view.grid(column=0, row=0)

        self.btn1 = ttk.Button(self.frame2, text="new")
        self.btn1.grid(column=0, row=0)

        self.btn2 = ttk.Button(self.frame2, text="edit")
        self.btn2.grid(column=1, row=0, padx=(5, 5))

        self.btn3 = ttk.Button(self.frame2, text="delete")
        self.btn3.grid(column=2, row=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()
