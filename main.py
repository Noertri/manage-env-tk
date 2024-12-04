import tkinter as tk
from tkinter import ttk
import os
from pathlib import Path
from collections import OrderedDict


env_vars = dict(os.environ)

for name, values in env_vars.items():
    print(f"{name}={values.strip()}")
