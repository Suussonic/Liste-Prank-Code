#Persistent
#InstallKeybdHook
#UseHook
#NoTrayIcon
SetBatchLines, -1

; =========================
; BLOCAGE DES TOUCHES SPÉCIALES
; =========================

AppsKey::Return
ScrollLock::Return
Pause::Return

; =========================
; RACCOURCIS CLASSIQUES
; =========================

!Tab::Return
!F4::Return
!Space::Return

^Tab::Return
^+Tab::Return
^Esc::Return
^+Esc::Return

+Tab::Return

#r::Return
#e::Return
#d::Return
#m::Return
#+m::Return
#Tab::Return
#^Right::Return
#^Left::Return
#^d::Return
#^f::Return
#^n::Return

Tab::Return

F1::Return
F2::Return
F3::Return
F4::Return
F5::Return
F6::Return
F7::Return
F8::Return
F9::Return
F10::Return
F11::Return
F12::Return

; =========================
; INTERCEPTER TOUTES LES COMBOS MODIFIÉES
; =========================

~Ctrl::
~Alt::
~Shift::
~LWin::
~RWin::
    BlockAllShortcuts()
    Return

BlockAllShortcuts() {
    ih := InputHook("V L0 I0 M")
    ih.KeyOpt("{All}", "E")
    ih.Start()
    ih.Wait()
}
