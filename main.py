import time

import keyboard
import pyautogui
import win32api
import win32con
from selenium import webdriver

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
# driver.get('http://www.donttap.com/')
driver.get('https://www.agame.com/game/magic-piano-tiles')
driver.maximize_window()
time.sleep(2.5)
driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="zoom-fullscreen"]/div').click()
time.sleep(1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


click(947, 519)
time.sleep(20)

time.sleep(3)
click(970, 550)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(758, 320)[0] == 0:
        click(758, 320)

    if pyautogui.pixel(900, 320)[0] == 0:
        click(900, 320)

    if pyautogui.pixel(1045, 320)[0] == 0:
        click(1045, 320)

    if pyautogui.pixel(1130, 320)[0] == 0:
        click(1130, 320)
