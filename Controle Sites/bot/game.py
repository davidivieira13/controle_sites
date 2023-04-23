import time
from turtle import onrelease
import pyautogui as py
import pygetwindow
from movimentos import Bot
import sys
import os
from interval import Interval
from pynput import keyboard
import threading
import pywinauto
import time
import win32gui
import webbrowser


nome = "youtube kids"



py.FAILSAFE = False
sys.setrecursionlimit(10**9)
var_reload = 0
Start_Bot = Bot()
#Start_Bot.ArrumaBoteCmd()


def fMain(): 


    while True:
        handles = pywinauto.findwindows.find_windows()
        titles = []
        sites = ['youtube kids','monkey','moto x3m','subway surfers','drive mad','crazy cars','go kart','dreadhead parkour']
        navegadores = ['chrome.exe','brave.exe','mozzila.exe']
        #navegadores = ['chrome.exe']

        for handle in handles:
            window = pywinauto.WindowSpecification({'handle': handle})
            title = window.window_text().lower()
            for site in sites:
                if site in title:
                    titles.append(title)


        if not titles:
            print("Nenhuma janela encontrada para os sites:", ", ".join(sites))
            for navegador in navegadores:
                os.system(f"taskkill /f /im {navegador}")
                time.sleep(2)
                webbrowser.open('https://poki.com.br/')

        else:
            for title in titles:
                print(title)  
        time.sleep(30)
       









def fVerificaKeyPress(): 
   while True:
       with keyboard.Events() as events:
           for event in events: 
               if event.key == keyboard.Key.esc:
                   os._exit(0)

threading.Thread(target=fVerificaKeyPress).start()
fMain()
