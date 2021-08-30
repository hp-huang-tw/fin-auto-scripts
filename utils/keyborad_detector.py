def get_capslock_state():
    import ctypes
    win_ddl = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return bool(win_ddl.GetKeyState(VK_CAPITAL))


def disable_capslock():
    import pyautogui
    pyautogui.press('capslock')

    print("WARNING:  DISABLE CAPS LOCK.")
