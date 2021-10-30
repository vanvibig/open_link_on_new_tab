import webbrowser
import sys
import pyautogui
import pyperclip

def getLink():
    from pywinauto import Application
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*", found_index=0)
    dlg = app.top_window()
    url = dlg.child_window(control_type="Edit", found_index=0).get_value()
    return url