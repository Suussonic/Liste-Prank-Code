import keyboard
import time

delay = 0

shortcuts = [
    ["ctrl", "c"],          # Copier
    ["ctrl", "x"],          # Couper
    ["ctrl", "v"],          # Coller
    ["ctrl", "z"],          # Annuler
    ["ctrl", "y"],          # Rétablir
    ["ctrl", "a"],          # Tout sélectionner
    ["ctrl", "s"],          # Sauvegarder
    ["ctrl", "o"],          # Ouvrir
    ["ctrl", "p"],          # Imprimer
    ["ctrl", "n"],          # Nouveau
    ["ctrl", "f"],          # Rechercher
    ["ctrl", "h"],          # Remplacer
    ["ctrl", "w"],          # Fermer fenêtre/onglet
    ["ctrl", "tab"],        # Onglet suivant
    ["ctrl", "shift", "tab"], # Onglet précédent
    ["alt", "tab"],         # Basculer entre applis
    ["alt", "f4"],          # Fermer fenêtre
    ["alt", "space"],       # Menu fenêtre
    ["alt", "enter"],       # Propriétés / plein écran
    ["alt", "esc"],         # Cycle applis ouvertes
    ["alt", "shift", "tab"],# Cycle inverse applis
    ["shift", "delete"],    # Supprimer définitivement
    ["shift", "insert"],    # Coller (alternative)
    ["f1"],                 # Aide
    ["f2"],                 # Renommer
    ["f3"],                 # Recherche dans explorateur
    ["f4"],                 # Barre d’adresses
    ["f5"],                 # Actualiser
    ["f6"],                 # Parcourir éléments
    ["f10"],                # Menu d’appli
    ["shift", "f10"],       # Clic droit contextuel
    
    ["windows", "d"],            # Afficher / masquer le bureau
    ["windows", "e"],            # Ouvrir l’Explorateur de fichiers
    ["windows", "i"],            # Ouvrir Paramètres
    ["windows", "a"],            # Centre de notifications / actions rapides
    ["windows", "s"],            # Recherche Windows
    ["windows", "r"],            # Exécuter
    ["windows", "x"],            # Menu Power User
    ["windows", "m"],            # Réduire toutes les fenêtres
    ["windows", "shift", "m"],   # Restaurer fenêtres réduites
    ["windows", "tab"],          # Vue multitâche
    ["windows", "ctrl", "d"],    # Nouveau bureau virtuel
    ["windows", "ctrl", "f4"],   # Fermer bureau virtuel actif
    ["windows", "ctrl", "gauche"], # Passer au bureau précédent
    ["windows", "ctrl", "droite"], # Passer au bureau suivant
    ["windows", "l"],            # Verrouiller la session
    ["windows", "u"],            # Options d’accessibilité
    ["windows", "pause"],        # Système / Propriétés
    ["windows", "p"],            # Choisir mode d’affichage (écrans)
    ["windows", "prtscr"],       # Capture d’écran (PNG auto)
    ["windows", "shift", "s"],   # Capture d’écran (outil capture)
    ["windows", "plus"],         # Loupe zoom +
    ["windows", "minus"],        # Loupe zoom -
    ["windows", "esc"],          # Quitter loupe
    ["windows", "t"],            # Parcourir les apps dans la barre des tâches
    ["windows", "b"],            # Focus zone de notification
    ["windows", "v"],            # Historique du presse-papiers
    ["windows", "k"],            # Connexion périphériques sans fil
    ["windows", "o"],            # Verrouiller orientation écran
    ["windows", "h"],            # Dictée vocale
    ["windows", "g"],            # Xbox Game Bar
    ["windows", "alt", "r"],     # Démarrer/arrêter enregistrement écran (Game Bar)
    ["windows", "shift", "c"],   # Cortana (si activée)
    ["windows", "c"],            # Chat Microsoft Teams (Win11)
    ["windows", "n"],            # Centre de notifications + calendrier
    ["windows", "w"],            # Widgets (Win11)
    
    ["windows", "flèche_gauche"],      # Ancrer fenêtre à gauche
    ["windows", "flèche_droite"],      # Ancrer fenêtre à droite
    ["windows", "flèche_haut"],        # Agrandir fenêtre (maximiser)
    ["windows", "flèche_bas"],         # Réduire fenêtre / restaurer
    ["windows", "shift", "flèche_gauche"], # Déplacer fenêtre vers écran de gauche
    ["windows", "shift", "flèche_droite"], # Déplacer fenêtre vers écran de droite
    ["windows", "shift", "flèche_haut"],   # Étendre fenêtre en hauteur
    ["windows", "shift", "flèche_bas"],    # Réduire fenêtre en barre des tâches
    ["windows", "home"],               # Réduire toutes sauf la fenêtre active
    ["windows", "shift", "m"],         # Restaurer toutes les fenêtres réduites
    ["windows", "ctrl", "f4"],         # Fermer bureau virtuel actuel
    ["windows", "ctrl", "droite"],     # Bureau virtuel suivant
    ["windows", "ctrl", "gauche"],     # Bureau virtuel précédent
    ["windows", "ctrl", "d"],          # Créer nouveau bureau virtuel
    ["windows", "tab"],                # Vue multitâche (tous bureaux + fenêtres)
    ["windows", "ctrl", "shift", "b"], # Redémarrer driver graphique (⚠️ sensible)
    
    ["ctrl", "n"],             # Nouvelle fenêtre explorateur
    ["ctrl", "w"],             # Fermer fenêtre explorateur
    ["ctrl", "shift", "n"],    # Nouveau dossier
    ["alt", "flèche_droite"],  # Dossier suivant
    ["alt", "flèche_gauche"],  # Dossier précédent
    ["alt", "flèche_haut"],    # Remonter au dossier parent
    ["alt", "d"],              # Sélectionner barre d’adresse
    ["ctrl", "l"],             # Sélectionner barre d’adresse (alternative)
    ["f4"],                    # Liste déroulante barre d’adresse
    ["f5"],                    # Actualiser
    ["ctrl", "r"],             # Actualiser (alternative)
    ["ctrl", "shift", "e"],    # Développer l’arborescence du volet navigation
    ["ctrl", "shift", "n"],    # Créer nouveau dossier
    ["alt", "enter"],          # Propriétés d’un élément sélectionné
    ["alt", "p"],              # Activer/désactiver volet de visualisation
    ["alt", "shift", "p"],     # Activer/désactiver volet des détails
    ["f2"],                    # Renommer élément
    ["f3"],                    # Rechercher dans l’explorateur
    ["ctrl", "shift", "1"],    # Icônes extra larges
    ["ctrl", "shift", "2"],    # Icônes grandes
    ["ctrl", "shift", "3"],    # Icônes moyennes
    ["ctrl", "shift", "4"],    # Icônes petites
    ["ctrl", "shift", "5"],    # Liste
    ["ctrl", "shift", "6"],    # Détails
    ["ctrl", "shift", "7"],    # Mosaïques
    ["ctrl", "shift", "8"],    # Contenu
    ["ctrl", "mousewheel"],    # Zoom icônes (Ctrl + molette souris)
    ["alt", "f4"],             # Fermer explorateur
    ["ctrl", "shift", "t"],    # Rouvrir dernier onglet fermé (Win11 onglets)
    ["ctrl", "t"],             # Nouvel onglet (Win11)
    ["ctrl", "tab"],           # Onglet suivant
    ["ctrl", "shift", "tab"],  # Onglet précédent
    
    # --- Capture d’écran ---
    ["prtscr"],                    # Capture plein écran (presse-papiers)
    ["alt", "prtscr"],             # Capture fenêtre active (presse-papiers)
    ["windows", "prtscr"],         # Capture plein écran (fichier PNG auto)
    ["windows", "shift", "s"],     # Capture personnalisée (outil capture)

    # --- Loupe / Accessibilité ---
    ["windows", "plus"],           # Loupe zoom +
    ["windows", "minus"],          # Loupe zoom -
    ["windows", "esc"],            # Quitter la loupe
    ["windows", "ctrl", "c"],      # Couleurs inversées
    ["windows", "u"],              # Paramètres accessibilité

    # --- Outils système ---
    ["windows", "pause"],          # Propriétés système
    ["windows", "r"],              # Exécuter
    ["windows", "x"],              # Menu avancé (Power User)
    ["windows", "ctrl", "shift", "b"], # Redémarrer le driver graphique
    ["ctrl", "shift", "esc"],      # Gestionnaire des tâches
    ["ctrl", "alt", "delete"],     # Sécurité (⚠️ non simulable via keyboard)

    # --- Bureau & multitâche ---
    ["windows", "d"],              # Afficher / masquer bureau
    ["windows", "m"],              # Réduire toutes fenêtres
    ["windows", "shift", "m"],     # Restaurer fenêtres réduites
    ["windows", "tab"],            # Vue multitâche
    ["alt", "tab"],                # Basculer entre applis
    ["ctrl", "alt", "tab"],        # Liste applis avec navigation clavier

    # --- Dictée & saisie ---
    ["windows", "h"],              # Dictée vocale
    ["windows", ".",],             # Emoji / caractères spéciaux
    ["windows", ";"],              # Emoji / caractères spéciaux (alternative)
    ["windows", "v"],              # Presse-papiers étendu
]


for combo in shortcuts:
    print(f" Raccourci : {' + '.join(combo)}")
    keyboard.press_and_release('+'.join(combo))
    time.sleep(delay)