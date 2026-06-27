from src import Tela 
from src.shapes.points import Ponto
from src.shapes.lines import Linha
from tkinter import *

class Single_Line(Tela):
    def __init__(self, linha: Linha, canvas: Canvas, janela: Tk):
        super().__init__(canva=canvas, janela=janela)
        self.linha = linha

    def criar_forma(self):
        def marca_inicio(event):
            self.linha.ponto1 = Ponto(event.x, event.y)

        def atualiza_fim(event):
            self.linha.ponto2 = Ponto(event.x, event.y)
            self.canva.delete("all")
            self.canva.create_line(self.linha.ponto1.x, self.linha.ponto1.y, self.linha.ponto2.x, self.linha.ponto2.y)

        self.canva.bind('<ButtonPress-1>', marca_inicio)
        self.canva.bind('<B1-Motion>', atualiza_fim)
