




def send_key(hwnd, key):
    """
    Send a single key press to the specified window.

    :param hwnd: Handle to the target window.
    :param key: The key to press (e.g., 'f2').
    """
    # Convert the key to its virtual-key code (VK)
    vk_code = win32api.VkKeyScan(key.upper()) & 0xFF

    # Send WM_KEYDOWN message
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, vk_code, 0)

    # Optional: Small delay between key down and key up
    time.sleep(0.05)

    # Send WM_KEYUP message
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, vk_code, 0)

def press_key_loop(hwnd, key, duration=0.1, interval=1.0):
    """
    Continuously press a key in a separate thread.

    :param hwnd: Handle to the target window.
    :param key: The key to press.
    :param duration: How long to hold the key down (not used here but kept for consistency).
    :param interval: Wait time between presses.
    """
    def loop_press():
        while True:
            send_key(hwnd, key)
            time.sleep(interval)
    
    t = threading.Thread(target=loop_press, daemon=True)
    t.start()

def get_window_handle(title_part):
    """
    Retrieve the window handle for a window containing the specified title part.

    :param title_part: Partial or full title of the window.
    :return: Window handle (HWND) or None if not found.
    """
    windows = gw.getWindowsWithTitle(title_part)
    if windows:
        return windows[0]._hWnd  # Access the private _hWnd attribute
    else:
        return None

