import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

def waste(waste_types):
    waste_categories = {
        'plastmasas pudele':'Plastmasas',
        'alumīnija kanniņa':'Metāla',
        'piena kartons':'Papīra',
        'augļi':'Organisko atkritumu',
        'stikla pudele':'Stikla',
        'dators':'E-atkritumu',
        'banāna miza':'Organisko atkritumu',
        'kartons':'Papīra',
        'plastmasas maisiņš':'Plastmasas',
        'koku lapas':'Organisko atkritumu'
    }

    waste_types = waste_types.lower().strip()

    if waste_types in waste_categories:
        return f"{waste_types.capitalize()} jāliek {waste_categories[waste_types]} konteinerā."
    else:
        return "Atkritumu veids nav sarakstā. Lūdzu mēģiniet vēlreiz!"

def sort_button():
    waste_entryyy = combo.get()

    result = waste(waste_entryyy)

    messagebox.showinfo("Rezultāts",result)

waste_options = [
    'plastmasas pudele',
    'alumīnija kanniņa',
    'piena kartons',
    'augļi',
    'stikla pudele',
    'dators',
    'banāna miza',
    'kartons',
    'plastmasas maisiņš',
    'koku lapas'
]


window = tk.Tk()
window.title("Atkritumu šķirošanas sistēma")
window.geometry("750x600")

label= tk.Label(window, text = 'Ievadiet atkritumu veidu: ')
label.pack(pady=10)

combo = ttk.Combobox(window, values = waste_options)
combo.pack(pady=70)

button = tk.Button(window, text = 'Šķirot! ', command = sort_button)
button.pack(pady=10)

foto_image = Image.open("e39comp.png")
resize = foto_image.resize((705,397))
foto = ImageTk.PhotoImage(resize)
foto_label = ttk.Label(window, image = foto)
foto_label.pack(pady=10)

window.mainloop()
