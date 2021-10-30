#!/usr/bin/env python
# coding: utf-8

import webbrowser
import sys
import pyautogui

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# current_link = "https://metruyenchu.com/truyen/vo-dich-dai-lao-sap-xuat-the/chuong-1"
current_link = sys.argv[1]

next_chapter = ''.join(current_link.rpartition('-')[:2])
# print(next_chapter)

chapter = int(sys.argv[2])

# next_chapter = "https://metruyenchu.com/truyen/vo-dich-dai-lao-sap-xuat-the/chuong-"

for i in range(1, 20):
    next_chapter_link = next_chapter + str((chapter + i))
    print(next_chapter_link)
    webbrowser.get(chrome_path).open(next_chapter_link)

# cmd >>> python open_link_on_new_tab.py https://metruyenchu.com/truyen/ta-chinh-la-khong-theo-sao-lo-ra-bai/chuong-1 1