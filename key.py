import time
import pyautogui

def press_f2(window,key_name):
    window.set_focus()  # Activate the window
    time.sleep(0.5)  # Wait for the window to be active
    pyautogui.press(key_name)
