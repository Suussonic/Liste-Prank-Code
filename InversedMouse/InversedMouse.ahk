#SingleInstance, Force
#Persistent
SetBatchLines, -1
SetMouseDelay, -1
CoordMode, Mouse, Screen  ; Coordonnées de la souris par rapport à l'écran

toggle := true
oldX := ""
oldY := ""

SetTimer, WatchMouse, 1  ; Exécuter toutes les millisecondes
return

WatchMouse:
if (!toggle)
    return

MouseGetPos, x, y

; Initialisation des anciennes coordonnées
if (oldX = "")
{
    oldX := x
    oldY := y
    return
}

; Calcul du déplacement sur l'axe X et Y
deltaX := x - oldX
deltaY := y - oldY

; Si le déplacement est significatif sur l'axe X et Y, on l'inverse
if (Abs(deltaX) > 1 || Abs(deltaY) > 1)
{
    ; Inverser le mouvement des deux axes
    MouseMove, -2*deltaX, -2*deltaY, 0, R  ; Inversion de X et Y (mouvement relatif)
    ; Mise à jour des anciennes positions après inversion
    oldX := x - 2*deltaX
    oldY := y - 2*deltaY
}
else
{
    ; Si peu de mouvement, on met simplement à jour les positions
    oldX := x
    oldY := y
}
return

F12::  ; Toggle pour activer/désactiver
toggle := !toggle
ToolTip % toggle ? "🌀 Inversion X/Y activée" : "🛑 Inversion désactivée"
SetTimer, RemoveToolTip, -1000
return

RemoveToolTip:
ToolTip
return
