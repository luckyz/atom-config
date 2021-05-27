#!/usr/bin/env python3
import json
import os
import tkinter as tk
from tkinter import filedialog
import platform
import shutil

platforms = {
    "Linux": "sudo apt-get install python3-tk",
    "Darwin": "brew install python-tk",
}

os.popen("pip install -r requirements.txt")

os.system(platforms.get(platform.system()))

DEFAULT_DIR = "./packages.json"
FILEOPENOPTIONS = (("JSON files", "*.json"), ("All files", "*.*"))

root = tk.Tk()
root.withdraw()
FILE_INPUT = "packages.json"

with open(FILE_INPUT, "r") as json_file:
    dir_path = os.path.dirname(json_file.name)
    source = json.load(json_file)
    packages = []
    for index in range(len(source["packages"])):
        package_name = source["packages"][index]
        packages.append(package_name)

os.system("apm install {}".format(" ".join(packages)))

for file in os.listdir("settings/"):
    shutil.copy(os.path.join("settings", file),
                os.path.join(os.getenv("HOME"), ".atom"))
