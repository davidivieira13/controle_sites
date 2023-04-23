import tkinter as tk
from tkinter import ttk
import subprocess
import time

nome_do_jogo = 'nome do game'

class Janela:
    
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Bot Dsv")
        self.label = tk.Label(self.janela, text="")
        self.janela.iconbitmap('./img/icone.ico')
        self.label.pack()
        self.frame_botoes = tk.Frame(self.janela)
        self.frame_botoes.pack()
        style = ttk.Style()
        style.configure('my.TButton', font=('Arial', 12, "bold"))
        self.botao_iniciar = ttk.Button(self.frame_botoes, text="Iniciar", command=self.iniciar_script, style='my.TButton')
        self.botao_iniciar.pack(side=tk.TOP, padx=3, pady=3)        
        self.botao_parar = ttk.Button(self.frame_botoes, text="Parar", command=self.parar_script, style='my.TButton')
        self.botao_parar.pack(side=tk.TOP, padx=3, pady=3)   
        self.label_tempo = tk.Label(self.frame_botoes, text="Tempo de execução", font=("Arial", 11, "bold"))
        self.label_tempo.pack(side=tk.TOP, padx=5, pady=5)   
        self.botao_ajudar = ttk.Button(self.frame_botoes, text="Contribuir", command=self.Contribuir, style='my.TButton')
        self.botao_ajudar.pack(side=tk.TOP, padx=3, pady=3)               
        self.contador = 0
        self.id_contagem = None  # ID da contagem iniciada pelo método after
        self.script = None
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_janela)
        self.janela.mainloop()

    def Contribuir(self):
        janela_contribuir = tk.Toplevel()
        janela_contribuir.title("Carteira Metamask")
        janela_contribuir.geometry("400x80")
        texto2 = "0x734fdcbbb19d96e1a25c7e3209dde3ee65c6b686"
        label_contribuir = tk.Label(janela_contribuir, text=texto2,font=("Arial", 10, "bold"))
        label_contribuir.pack()
        botao_copiar = tk.Button(janela_contribuir, text="Copiar Carteira", command=lambda: janela_contribuir.clipboard_append(texto2))
        botao_copiar.pack()        
        texto1 = "Obrigado =)"
        label_contribuir = tk.Label(janela_contribuir, text=texto1,font=("Arial", 10, "bold"))
        label_contribuir.pack()   
           



    def iniciar_contagem(self):
        self.contador += 1
        self.label_tempo.config(text=self.tempo_de_execucao())
        self.id_contagem = self.janela.after(1000, self.iniciar_contagem)
        
    def tempo_de_execucao(self):
        horas = self.contador // 3600
        minutos = (self.contador % 3600) // 60
        segundos = self.contador % 60
        return f"Tempo de execução: {horas:02d}:{minutos:02d}:{segundos:02d}"
    
    def iniciar_script(self):
        self.label.config(text=f"Bot {nome_do_jogo} Iniciado",fg='#32CD32')
        self.iniciar_contagem()
        self.script = subprocess.Popen(["python", "game.py"])
        
    def parar_script(self):
        self.label.config(text=f"Bot {nome_do_jogo} Parado",fg='red')
        if self.script:
            self.script.terminate()
        if self.id_contagem:
            self.janela.after_cancel(self.id_contagem)
        
    def fechar_janela(self):
        self.janela.destroy()
        if self.script:
            self.script.terminate()
        if self.id_contagem:
            self.janela.after_cancel(self.id_contagem)

janela = Janela()

