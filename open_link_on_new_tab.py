#!/usr/bin/env python
# coding: utf-8

import webbrowser
from pywinauto import Application
import sys
import pyautogui
import pyperclip
import time

# def getLink():
#     app = Application(backend='uia')
#     app.connect(title_re=".*Chrome.*", found_index=0)
#     dlg = app.top_window()
#     url = dlg.child_window(control_type="Edit", found_index=0).get_value()
#     return url

pyautogui.hotkey('alt', 'tab')
time.sleep(0.3)
pyautogui.click(x=872, y=64)
# pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'l')
pyautogui.hotkey('ctrl', 'c')
# pyperclip.paste()



chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# current_link = "https://metruyenchu.com/truyen/ta-that-khong-co-at-chu-bai/chuong-57"
# current_link = sys.argv[1]

current_link = pyperclip.paste()
# current_link = getLink()


next_chapter = ''.join(current_link.rpartition('-')[:2])
# print(next_chapter)

chapter = int(current_link.rpartition('-')[-1])

# # next_chapter = "https://metruyenchu.com/truyen/vo-dich-dai-lao-sap-xuat-the/chuong-"

for i in range(1, 20):
    next_chapter_link = next_chapter + str((chapter + i))
    print(next_chapter_link)
    webbrowser.get(chrome_path).open(next_chapter_link)

# cmd >>> python open_link_on_new_tab.py https://metruyenchu.com/truyen/ta-chinh-la-khong-theo-sao-lo-ra-bai/chuong-1 1