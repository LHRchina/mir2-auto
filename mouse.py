#mouse function
import pyautogui


def print_mouse_position(window):
    mouse_x, mouse_y = pyautogui.position()
    relative_x = mouse_x - window.left
    relative_y = mouse_y - window.top
    print(f"Mouse Position within window: ({relative_x}, {relative_y})")
