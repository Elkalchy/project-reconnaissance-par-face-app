import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style, Button, Entry
import face_recognizer
import face_taker
import face_train
from threading import Event





def quitter():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.quit()

def ajouter_personne():
    face_name = name_entry.get()
    if not face_name:
        messagebox.showwarning("Input Error", "Please enter a name.")
        return
    
    try:
        face_taker.capture_faces(face_name)
        face_train.train_model()
        messagebox.showinfo("Ajouter Personne", "Personne ajoutée avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))


# Initialize a stop event
stop_event = Event()
def stop_detection():
    stop_event.set()
def debut_detection():
    face_name = name_entry.get()
    if not face_name:
        messagebox.showwarning("Input Error", "Please enter a name.")
        return
    
    try:
        face_recognizer.start_recognition(face_name)
    except Exception as e:
        messagebox.showerror("Erreur", str(e))
    try:
        face_recognizer.start_recognition()
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

import import_img

def importer_images():
    face_name = name_entry.get()
    if not face_name:
        messagebox.showwarning("Input Error", "Please enter a name.")
        return

    try:
        import_img.import_images(face_name)
        messagebox.showinfo("Importer Images", "Images importées avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Add this button after the existing buttons



# Initialisation de l'application
style = Style(theme='litera')  # Choisissez un thème
root = style.master

# Création de la barre de menu
menu_bar = tk.Menu(root)

# Menu Accueil
accueil_menu = tk.Menu(menu_bar, tearoff=0)
accueil_menu.add_command(label="Accueil")
menu_bar.add_cascade(label="Accueil", menu=accueil_menu)

# Menu Archive
archive_menu = tk.Menu(menu_bar, tearoff=0)
archive_menu.add_command(label="Archive")
menu_bar.add_cascade(label="Archive", menu=archive_menu)

# Menu À propos
about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="À propos")
menu_bar.add_cascade(label="À propos", menu=about_menu)

# Menu Contact
contact_menu = tk.Menu(menu_bar, tearoff=0)
contact_menu.add_command(label="Contact")
menu_bar.add_cascade(label="Contact", menu=contact_menu)

# Menu Quitter
menu_bar.add_command(label="Quitter", command=quitter)

root.config(menu=menu_bar)

# Titre de la fenêtre
title_label = tk.Label(root, text="Gestion des personnes", font=("Helvetica", 16))
title_label.pack(pady=10)

# Entry pour le nom
name_label = tk.Label(root, text="Entrez le nom de la personne:")
name_label.pack(pady=5)
name_entry = Entry(root)
name_entry.pack(pady=5)

# Boutons
ajouter_button = Button(root, text="Ajouter personne", command=ajouter_personne)
ajouter_button.pack(pady=5)

debut_detection_button = Button(root, text="Début détection", command=debut_detection)
debut_detection_button.pack(pady=5)

import_button = Button(root, text="Importer Images", command=importer_images)
import_button.pack(pady=5)


# Lancement de l'application
root.geometry("400x300")
root.title("Gestion des personnes")
root.mainloop()
