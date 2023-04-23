import tkinter as tk
import subprocess
import sys



class Instalador:

    def __init__(self):
        self.pip = sys.executable + " -m pip"
        
    def esta_instalado(self, modulo):
        try:
            __import__(modulo)
        except ImportError:
            print(modulo,'- não esta instalado')
            return False
        return True
        
    def instalar(self, modulo):
        if not self.esta_instalado(modulo):
            print(modulo,'- Sendo instalado')
            subprocess.check_call(self.pip.split() + ["install", modulo])
            

instalador = Instalador()
instalador.instalar("tkinter")
instalador.instalar("subprocess")
instalador.instalar("interval")
instalador.instalar("pynput")
instalador.instalar("pywin32")
instalador.instalar("opencv-python")
instalador.instalar("pillow")
instalador.instalar("pyautogui")
instalador.instalar("webbrowser")
instalador.instalar("pywinauto")








