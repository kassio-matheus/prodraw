#Global imports
from tkinter import *

#Local imports
from src.shapes.points import Ponto
from src.shapes.lines import Linha
from src import Tela

class Multiples_Lines(Tela):
    def __init__(self,linha: Linha, canva: Canvas, janela: Tk):
        super().__init__(canva, janela)
        self.linha = linha
        self.linhas  = []
    def criar_forma(self):
         
         
         def inicia_linha(event):
            self.linha = Linha()
            self.linha.ponto1 = Ponto(event.x, event.y)
            
            

         def atualiza_linha(event):
            self.linha.ponto2 = Ponto(event.x, event.y)
            self.canva.delete("all")
            desenhar()
            self.canva.create_line(self.linha.ponto1.x, self.linha.ponto1.y, self.linha.ponto2.x, self.linha.ponto2.y)

         def incluir_linha(event):
            self.linhas.append(self.linha)
         def desenhar():
             self.canva.delete('all')
             for linha in self.linhas:
                
                self.canva.create_line(linha.ponto1.x, linha.ponto1.y, linha.ponto2.x, linha.ponto2.y)
        
         self.canva.bind('<ButtonPress-1>', inicia_linha)
         self.canva.bind('<B1-Motion>', atualiza_linha)
         self.canva.bind('<ButtonRelease-1>', incluir_linha)
