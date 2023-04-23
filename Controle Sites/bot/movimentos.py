import math
import time
import pyautogui as py
import pygetwindow
from interval import Interval
import os
import logging
import random


x = 1095
y = 740

bot_pos_x = 1095
bot_pos_y = 100

bot_tam_x = 270
bot_tam_y = 205

nome_usuario = os.environ['USERNAME']
logging.basicConfig(filename=f'meu_log_{nome_usuario}.log', level=logging.DEBUG, format='%(asctime)s %(message)s')  
#logging.debug('text')

class Bot:

    def IdentificaProblema(self):
        pass

    def IdentificaClica(self, imagem_path): 
        if self.Identifica(imagem_path):
            x, y = py.center(imagem_path)
            py.click(x, y)   
            return True
        else:
            return False         

    def Identifica(self, imagem_path): 
        self.Animate()
        regiao=(0, 0, x, y)
        posicao = py.locateOnScreen(imagem_path, region=regiao, confidence=0.85)
        if posicao is not None:
            return True
        else:
            return False          

    def IdentificaMove(self, imagem_path): 
        if self.Identifica(imagem_path):
            x, y = py.center(imagem_path)
            py.move(x, y)   
            return True
        else:
            return False            

    def WhileClica(self,imagem_path):
        var_break = 0
        while True:
            var_break += 1
            if self.IdentificaClica(imagem_path):
                time.sleep(1)
                print(imagem_path,'encontrado')
                self.IdentificaClica(imagem_path)
                return True
            else:
                pass
                print(imagem_path,'não encontrado', var_break)
                
            if var_break > 5:
                return False               

##################################################################################################

    def acao_na_janela(self, janela):
        py.keyDown('alt')
        py.press('tab')    
        py.keyUp('alt')           
        janela.size=(x,y) 
        janela.moveTo(-6,0)        
        janela.activate()
        time.sleep(0.1)
 
    def BuscaJanelaBot(self):
       py.keyDown('alt')
       py.press('tab')    
       py.keyUp('alt')
       try:
           win = pygetwindow.getWindowsWithTitle('Bot Dsv')[0]
           if win != None:  
               win.size=(bot_tam_x, bot_tam_y)    
               win.moveTo(bot_pos_x, bot_pos_y)
               win.activate()
               return True
           else:
               return False
       except:
               return False                

    def BuscaJanelaCmd(self):
        py.keyDown('alt')
        py.press('tab')    
        py.keyUp('alt')
        try:
            win = pygetwindow.getWindowsWithTitle('python.exe')[0]
            if win != None:
                win.size=(bot_tam_x, bot_tam_y + 60)        
                win.moveTo(bot_pos_x, bot_pos_y + 205)
                win.activate()
                return True
            else:
                return False
        except:
                return False    
            
    def ArrumaBoteCmd(self):
        if self.BuscaJanelaBot(): 
            self.AnimateJanela()
            time.sleep(0.4)                          

        if self.BuscaJanelaCmd(): 
            self.AnimateJanela()
            time.sleep(0.4)  

    def AnimateJanela(self):
        FRAMES = [
      r"""          
Estou Arrumando as Janelas !
          _____
         | ò O |
         |__-__| 
          _ | _
       __/  |  \__
           / \
          /   \
      """,
      r"""          
Estou Arrumando as Janelas !
          ______
         |[.][.]|
         |__-___| /
          _ | ___/
       __/  |  
           / \
          /   \
      """,
      r"""          
Estou Arrumando as Janelas !
          ______
         | ^  ^ |
         |__()__| 
      _____ | _
            |  \__
           / \
          /   \
      """               
        ]

        def robozin():
            frame = random.choice(FRAMES)
            print('\n' * 100)
            print('\n' * 20)
            print(frame)
            time.sleep(0.5) 
        robozin()        

    def Animate(self):
        FRAMES = [
      r""" 
      To the Moon !           
          _____
         | - o |
         |__=__|/  
          _ | _/
       __/  |
         __/ \
              \
      """, 
      r"""
Vai la qualquer coisa te aviso !      
          _____
         | | | |
         |__¨__|
          _ | __/ 
        \/  |   
          \/ \
              \
      """, 
      r"""
     Estou de olho !      
          _____
         | ò Ó |
        \|__¨__|
         \_ | __ 
            |   \
           / \   \
          /   \
      """,    
      r"""
Já fez os 100 Dol de cada dia ?      
          _____
         | \ / |
        \|__¨__|/
         \_ | _/
            |
           / \
          /   \
      """,
      r"""
Que tal contruibuir hoje em ?     
          _____
         | ^ ^ |
       __|__^__|/
         \_ | _/
            |
           / \
          /   \
      """,   
      r"""
   Ja contriubiu hoje ?      
          _____
         | ^ o |
       \_|__º__| 
         \_ | _
            |  \
         __/ \  \
              \
      """, 
       r"""
Vai dar problema não relaxa !       
          _____
         | ` * |
         |__:__|/
          _ | _/
         /  |
        /  / \__
          /   
      """, 
      r"""
    Vai durmirrrr !!      
          _____
         | * * |
       __|__~__|__
         \_ | _/
            |
         __/ \__
             
      """, 
      r"""
     Vamos pra LUA !?
          _____
         |[] []|
        _|__^__|_
       / \_ | _/ \
            |
           / \__
          /   
      """, 
      r"""
    Ja bebeu aguá hoje ?      
          _____
         | $ $ |
        \|__O__|
         \_ | _
            |  \    
         __/ \  \
              \
      """, 
      r"""
    Sabia que sou Lendario ?      
          _____
         | 0 - |
       __|__<__|
         \_ | _
            |  \__    
         __/ \  
              \
      """, 
      r"""      
    Deixa comigo !!!      
          _____
         | 0 - |
       __|__<__|
         \_ | _
            |  \__    
         __/ \  
              \
      """, 
      r"""        
    Coloca a casa, vai da bom !    
          _____
         | - - |
        _|__x__|
       / \_ | _
            |  \__    
           / \  
          /   \
      """, 
      r"""          
Estou Trabalhando para Você !
          _____
         | | o |
         |__-__| 
          _ | _
       __/  |  \__
           / \
          /   \
      """    
        ]

        def robozin():
            frame = random.choice(FRAMES)
            print('\n' * 100)
            print('\n' * 20)
            print(frame)
            time.sleep(0.5) 
        robozin()