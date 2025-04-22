import os
import win32com.client

def get_desktop_path():
    paths = [
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "Bureau"),
        os.path.join(os.path.expanduser("~"), "OneDrive", "Bureau"),
        os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    raise Exception("Bureau introuvable.")

def generate_unique_name(base_name, folder, ext):
    i = 1
    new_name = base_name + ext
    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{base_name} ({i}){ext}"
        i += 1
    return new_name

def prank_desktop():
    desktop = get_desktop_path()
    icon_path = "%SystemRoot%\\System32\\SHELL32.dll,109"  # ✅ Icône carré rouge avec croix blanche

    shell = win32com.client.Dispatch("WScript.Shell")

    for item in os.listdir(desktop):
        item_path = os.path.join(desktop, item)

        if item.startswith("Erreur") or item.endswith(".tmp"):
            continue

        ext = os.path.splitext(item)[1]
        new_name = generate_unique_name("Erreur", desktop, ext)
        new_path = os.path.join(desktop, new_name)

        try:
            os.rename(item_path, new_path)
            print(f"{item} → {new_name}")

            if new_path.endswith(".lnk"):
                shortcut = shell.CreateShortcut(new_path)
                shortcut.IconLocation = icon_path
                shortcut.save()

        except Exception as e:
            print(f"Erreur sur {item} : {e}")

if __name__ == "__main__":
    prank_desktop()
