import ctypes
import os
import sys
from io import BytesIO

# Fonction pour obtenir le chemin du fichier image intégré
def get_image_path():
    if getattr(sys, 'frozen', False):  # Si le script est exécuté depuis un exécutable
        return os.path.join(sys._MEIPASS, 'troll_face.png')  # Chemin temporaire
    else:
        return os.path.join(os.path.dirname(__file__), 'troll_face.png')  # Chemin relatif dans le même dossier

# Spécifie le chemin de ton image de visage troll
image_path = get_image_path()

# Vérifie si l'image existe
if os.path.exists(image_path):
    # Change le fond d'écran sur Windows
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
else:
    print("L'image spécifiée n'existe pas.")
