import pyautogui
import Ears

# Spellname, Key combination

listener = Ears.Ears()

print(listener.get_words())




def TypeCode(spellcode):
    pyautogui.write(spellcode, interval=.1)
