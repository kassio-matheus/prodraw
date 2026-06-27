#Global imports
from tkinter import * 

#Local imports
from src.shapes.points import Ponto
from src.shapes.lines import Linha

from src.draws.lines.single_line import Single_Line
from src.draws.lines.multiples_lines import Multiples_Lines

def setup(root):
    canvas = Canvas(root, bg='black', width=600, height=600)
    canvas.pack()

    ponto1 = Ponto(0, 0)
    ponto2 = Ponto(0, 0)
    linha = Linha(ponto1, ponto2)

    draw_types = {
        'linha': Single_Line(linha, canvas, root).criar_forma,
        'linhas': Multiples_Lines(linha, canvas, root).criar_forma
    }

    opcao = StringVar()

    def draw(opcao):
        draw_types[opcao]()

    OptionMenu(root, opcao, 'linha', 'linhas', command=draw).pack()