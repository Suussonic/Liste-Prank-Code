# 🗒️ Liste Prank Code

Répertoire contenant des petits projets.

## 📜 Sommaire
- [Popup Infini](#♾️popup-infini)
- [Dossier Desktop](#📁dossier-desktop)
- [Multiple Calculatrice](#🧮multiple-calculatrice)
- [BlueScreen](#🟦bluescreen)
- [ClavierInfernal](#🔥clavierinfernal)
- [SourisFolle](#🖱️sourisfolle)
- [LockDown](#🔒lockdown)
- [Error](#🚫error)
- [InversedMouse](#⏪inversedmouse)
- [TrollFace](#🤣trollface)
- [ZipBombe](#💣zipbombe)
- [WindowsShortcuts](#🪟windowsshortcuts)

# ♾️ Popup Infini

Cet exécutable VBS va ouvrir une popup sur l'écran avec un certain message. Le seul moyen de la fermer est d'aller dans le gestionnaire de tâches, rechercher "Microsoft ® Windows Based Script Host" et faire Fin de tâche.

# 📁 Dossier Desktop

Cet exécutable prend tous les fichiers présents sur le bureau et les éparpille parmi 100 dossiers nouvellement créés.

Pour ceux qui veulent modifier le code source, qui est en Python, il vous faudra installer PyInstaller :

    ```
    pip install pyinstaller
    ```

Ensuite, il faudra compiler le script grâce à cette commande. Attention à être dans le bon répertoire :

    ```
    pyinstaller --onefile --noconsole "Nom Du Fichier".py
    ```

L'exécutable se trouvera dans le dossier `dist` !

# 🧮 Multiple Calculatrice

Cet exécutable ouvre une calculatrice basique fonctionnelle. La beauté de ce code est qu'en fermant la calculatrice, une autre apparaît. Le seul moyen de les arrêter est de les fermer dans le gestionnaire de tâches sous le nom "MultipleCalculatrice.exe".

Pour ceux qui veulent modifier le code source, qui est en Python, il vous faudra installer PyInstaller :

    ```
    pip install pyinstaller
    ```

Ensuite, il faudra compiler le script grâce à cette commande. Attention à être dans le bon répertoire :

    ```
    pyinstaller --onefile --noconsole "Nom Du Fichier".py
    ```

L'exécutable se trouvera dans le dossier `dist` !

# 🟦 BlueScreen

Lorsqu'on exécute ce fichier en tant qu'administrateur, il va littéralement faire crasher le PC, et un Blue Screen apparaîtra. Il suffira alors de redémarrer l'ordinateur et il n'y aura plus de problème.

Aucune perte de données ne sera à déplorer, sauf si un fichier était en cours de modification et qu'il n'a pas été sauvegardé (par exemple, un fichier Word qui n'a pas été enregistré).

# 🔥 ClavierInfernal

C'est un exécutable échangeant les touches de manière complètement aléatoire.

Pour arrêter le supplice, il faudra aller dans le gestionnaire de tâches et faire Fin de tâche sur "ClavierInfernal.exe".

Pour ceux voulant modifier le code, il faudra installer la bibliothèque Keyboard :

    ```
    pip install keyboard
    ```

Ensuite, pour compiler, il faudra entrer cette commande : 

    ```
    pyinstaller --onefile --noconsole "Nom Du Fichier".py
    ```

# 🖱️ SourisFolle

Cet exécutable donne des mouvements à la souris et la rend incontrôlable.

Pour l'arrêter, il faudra aller dans le gestionnaire de tâches et faire Fin de tâche sur "SourisFolle.exe" (si vous y arrivez, personnellement j'ai préféré redémarrer).

Pour ceux voulant modifier le code, pour le compiler il vous faudra utiliser l'outil AutoHotKey :

https://www.autohotkey.com/

# 🔒 LockDown

Cet exécutable bloque les raccourcis et d'autre touches spécifiques.

Pour l'arrêter, il faudra aller dans le gestionnaire de tâches et faire Fin de tâche sur "LockDown.exe".

Pour ceux voulant modifier le code, pour le compiler il vous faudra utiliser l'outil AutoHotKey :

https://www.autohotkey.com/

# 🚫 Error

C'est un exécutable renomme tous les fichiers du bureau en "Erreur" et les raccourcis se retrouve avec une icone changé.


Pour ceux voulant modifier le code, il faudra installer la bibliothèque Keyboard :

    ```
    pip install pywin32
    ```

Ensuite, pour compiler, il faudra entrer cette commande : 

    ```
    pyinstaller --onefile --noconsole "Nom Du Fichier".py
    ```

# ⏪ InversedMouse

Cet exécutable inverse les axes de la souris.

Pour l'arrêter, il faudra aller dans le gestionnaire de tâches et faire Fin de tâche sur "InversedMouse.exe".

Pour ceux voulant modifier le code, pour le compiler il vous faudra utiliser l'outil AutoHotKey :

https://www.autohotkey.com/

# 🤣 TrollFace

C'est un exécutable change bêtement le fond d'écran.


Pour ceux voulant modifier le code, il faudra installer trois bibliothèque :

    ```
    pip install ctypes os sys
    ```

Ensuite, pour compiler, il faudra entrer cette commande : 

    ```
    pyinstaller --onefile --noconsole --add-data "troll_face.png;." "Nom Du Fichier".py
    ```

# 💣 ZipBombe

Une zip-bombe est une archive ZIP piégée, minuscule en taille mais qui se décompresse en un volume beaucoup plus élevé grâce à:
- une très forte redondance (taux de compression extrême),
- et/ou des archives imbriquées de manière récursive (ZIP dans ZIP...).

But: saturer l’espace disque, la RAM ou le CPU lors de la décompression.

Attention: n’exécutez/ouvrez jamais une zip-bombe sur une machine de production. Utilisez un environnement isolé si c’est pour de la démonstration, et évidement le risque de crash dépend de la configuration matérielle.

# 🪟 WindowsShortcuts

C'est un exécutable éxécute tous les raccourcis windows.

Pour compiler, il faudra entrer cette commande : 

    ```
    pyinstaller --onefile --noconsole --add-data "troll_face.png;." "Nom Du Fichier".py
    ```
