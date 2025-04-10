import keyboard
import random

# Liste des touches à mapper
keys = "abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_+-=[]{}|;:',.<>?/`~\"'"

mapping = {}

# Génère un mapping aléatoire des touches
def generate_mapping():
    shuffled = list(keys)
    random.shuffle(shuffled)
    for original, new in zip(keys, shuffled):
        mapping[original] = new

# Gère les événements de frappe de touche
def on_event(event):
    if event.event_type == "down":  # On ne gère que les pressions de touches
        name = event.name.lower()

        if name in mapping:
            fake_key = mapping[name]

            # Simule la frappe de la touche mappée
            keyboard.write(fake_key)

            # Empêche la touche d'origine d'être enregistrée
            return False

# Génère le mapping au démarrage
generate_mapping()

# Affiche le mapping
print("Mapping généré :")
for k, v in mapping.items():
    print(f"{k} -> {v}")

# Attache le hook aux frappes clavier
keyboard.hook(on_event, suppress=True)

# Boucle infinie pour garder le programme actif
keyboard.wait()