import tkinter as tk
from tkinter import messagebox, ttk

def on_close():
    open_calculator()  # Ouvre une nouvelle calculatrice avant de fermer l'ancienne
    root.destroy()

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Erreur", "Entrée invalide")
        entry.delete(0, tk.END)

def open_calculator():
    global root, entry
    root = tk.Tk()
    root.title("Calculatrice")
    root.geometry("340x480")  # Taille ajustée
    root.configure(bg="#2C3E50")  # Fond sombre
    root.resizable(False, False)  # Empêcher le redimensionnement
    root.protocol("WM_DELETE_WINDOW", on_close)  # Réouverture automatique

    # Style moderne avec arrondi et survol
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 16), padding=10, relief="flat", background="#34495E")
    style.map("TButton", background=[("active", "#1ABC9C")])  # Changement de couleur au survol

    # Champ d'affichage avec bords arrondis
    entry_frame = tk.Frame(root, bg="#2C3E50")
    entry_frame.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

    entry = tk.Entry(entry_frame, width=17, font=("Arial", 24), bd=5, relief=tk.FLAT, justify="right", bg="#ECF0F1")
    entry.pack(ipady=10, padx=5, pady=5)

    # Liste des boutons organisés par ligne
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ]

    # Création des boutons
    for (text, row, col) in buttons:
        action = calculate if text == '=' else lambda t=text: press(t)
        btn = ttk.Button(root, text=text, command=action)
        btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

    # Bouton "C" bien centré et ajusté
    clear_btn = tk.Button(root, text="C", font=("Arial", 16, "bold"), bg="#E74C3C", fg="white", command=clear, relief="flat")
    clear_btn.grid(row=5, column=0, columnspan=4, padx=10, pady=10, ipadx=5, ipady=15, sticky="nsew")

    # Ajuster la taille des colonnes pour un meilleur rendu
    for i in range(4):
        root.columnconfigure(i, weight=1)
        root.rowconfigure(i+1, weight=1)

    root.mainloop()

open_calculator()
