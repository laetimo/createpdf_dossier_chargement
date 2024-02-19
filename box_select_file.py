import tkinter as tk
from tkinter import filedialog

def select_file(file):
    # Ouvrir la boîte de dialogue pour sélectionner le fichier
    file_path = filedialog.askopenfilename(title=f"Sélectionner le fichier {file}", filetypes=[("Fichiers Excel", "*.xlsx")])
    return file_path

def select_folder():
    folder_selected = filedialog.askdirectory(title=f"Sélectionner le dossier avec les fichiers de travail")
    return folder_selected

