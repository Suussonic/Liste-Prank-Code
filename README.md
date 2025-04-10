# 🗒️ Liste Prank Code

Répertoire contenant des petits projets a but comique et non pour nuire.

## 📜 Sommaire
- [Popup Infini](#♾️popup-infini)
- [Dossier Desktop](#📁dossier-desktop)
- [Multiple Calculatrice](#🧮multiple-calculatrice)
- [BlueScreen](#🟦blueScreen)

# ♾️ Popup Infini

Cette éxecutable VBS va ouvrir une popup sur l'ecran avec un certain message, le seule moyen de le fermer est d'aller dans le gestionnaire de tâche, rechercher "Microsoft ® Windows Based Script Host" et faire Fin de tâche.

# 📁 Dossier Desktop

Cette éxecutable prendre tout les fichiers présent dans le bureau et les éparpillés parmi 100 dossier nouvellement crée.

Pour ceux qui veulent modifier le code source qui est en python, il vous faudra installer pyinstaller :

    ```
    pip install pyinstaller
```

Ensuite il faudra compiler le script grâce à cet commande, attention à être dans le bon répertoire :

    ```
    pyinstaller --onefile --noconsole "Nom Du Fichier".py
```

L'éxécutable se trouvera dans le dossier dist !

# 🧮 Multiple Calculatrice

Cette éxecutable ouvre une calculatrice basique fonctionnelle, la beauté de ce code est qu'en fermant la calculatrice, une apparait, le seule moyen de les arrêter est de les fermer dans le gestionnaire de tâche "MultipleCalculatrice.exe".

Pour ceux qui veulent modifier le code source qui est en python, il vous faudra installer pyinstaller :

    ```
    pip install pyinstaller
```

Ensuite il faudra compiler le script grâce à cet commande, attention à être dans le bon répertoire :

    ```
    pyinstaller --onefile --noconsole "Nom Du Fichier".py
```

L'éxécutable se trouvera dans le dossier dist !

# 🟦 BlueScreen

Lorsqu'on exécute ce fichier en tant qu'administrateur, il va littéralement faire crasher le PC, et un Blue Screen apparaîtra. Il suffira alors de redémarrer l'ordinateur et il n'y aura plus de problème.

Aucune perte de donnée ne sera à déplorer, sauf si un fichier était en cours de modification et qu'il n'a pas été sauvegardé (par exemple, un fichier Word qui n'a pas été enregistré).

# 🔥 ClavierInfernal

C'est un exécutable échangeant les touches de manière complètement aléatoire.

Pour arrêter le supplice, il faudra aller dans le gestionnaire de tâches et faire Fin de tâche sur "ClavierInfernal.exe"

pour ceux voulant modifier le code, il faudra installer la bibliothèque Keyboard :

    ```
    pip install keyboard
```

Ensuite, pour compiler, il faudra entrer cette commande : 

    ```
    pyinstaller --onefile --noconsole ClavierInfernal.py
```
