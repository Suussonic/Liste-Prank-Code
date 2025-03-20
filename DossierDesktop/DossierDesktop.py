import os
import shutil
import random

# Trouver le bon chemin du bureau
desktop_paths = [
    os.path.join(os.path.expanduser("~"), "Desktop"),  
    os.path.join(os.path.expanduser("~"), "Bureau"),  
    os.path.join(os.path.expanduser("~"), "OneDrive", "Bureau"),
    os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
]

# Sélectionne le bon chemin du bureau
desktop = next((path for path in desktop_paths if os.path.exists(path)), None)

if not desktop:
    print("Erreur : Impossible de trouver le bureau.")
    exit()

# Création des 100 dossiers (Dossier_1 à Dossier_100)
dossiers = [os.path.join(desktop, f"Dossier_{i}") for i in range(1, 101)]
for dossier in dossiers:
    os.makedirs(dossier, exist_ok=True)

# Lister uniquement les fichiers à déplacer
elements = [f for f in os.listdir(desktop) if os.path.isfile(os.path.join(desktop, f))]

# Vérification : afficher les fichiers trouvés
print(f"Fichiers trouvés : {elements}")

# Déplacer chaque fichier dans un dossier aléatoire parmi les 100
for elem in elements:
    source = os.path.join(desktop, elem)
    dossier_choisi = random.choice(dossiers)
    destination = os.path.join(dossier_choisi, elem)
    
    shutil.move(source, destination)
    print(f"Déplacé : {elem} → {dossier_choisi}")

print("Tous les fichiers ont été répartis aléatoirement dans les dossiers ! ✅")
