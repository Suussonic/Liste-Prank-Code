import os
import shutil
import random

# Trouver le bon chemin du bureau
desktop_paths = [
    os.path.join(os.path.expanduser("~"), "Desktop"),  # Bureau classique
    os.path.join(os.path.expanduser("~"), "Bureau"),   # Bureau en français
    os.path.join(os.path.expanduser("~"), "OneDrive", "Bureau"), # Bureau OneDrive
    os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")  # Bureau classique OneDrive
]

# Sélectionne le bon chemin du bureau
desktop = next((path for path in desktop_paths if os.path.exists(path)), None)

if not desktop:
    print("Erreur : Impossible de trouver le bureau.")
    exit()

# Création des 100 dossiers (Dossier_1 à Dossier_100)
dossiers = []
for i in range(1, 101):
    dossier_path = os.path.join(desktop, f"Dossier_{i}")
    os.makedirs(dossier_path, exist_ok=True)
    dossiers.append(dossier_path)  # Stocke les chemins des dossiers

# Lister les éléments (fichiers et dossiers) à déplacer
elements = [f for f in os.listdir(desktop) if not f.startswith("Dossier_")]

# Déplacer chaque élément dans un dossier aléatoire parmi les 100
for elem in elements:
    dossier_choisi = random.choice(dossiers)  # Sélectionne un dossier au hasard
    shutil.move(os.path.join(desktop, elem), dossier_choisi)

print("Tous les fichiers ont été répartis aléatoirement dans les dossiers ! ✅")