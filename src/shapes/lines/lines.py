from tkinter import *
from src.shapes.colors import SHAPE_COLORS


def Lines(canvas: Canvas, bg: StringVar, figures: list = []):
    figuras = figures
    # Quando o mouse é pressionado
    def inicia_linha(event):
        nonlocal ini_x, ini_y
        ini_x = event.x
        ini_y = event.y

    # Quando o mouse é movido com o botão pressionado
    def atualiza_linha(event):
        nonlocal fim_x, fim_y
        fim_x = event.x
        fim_y = event.y
        desenhar()
        canvas.create_line(ini_x, ini_y, fim_x, fim_y, fill=bg.get(), tags="line")

    # Quando o mouse é solto
    def incluir_linha(event):
        nonlocal fim_x, fim_y, ini_y, ini_x

        figuras.append(("linha",bg.get(),(ini_x, ini_y, fim_x, fim_y)))

    def desenhar():
        canvas.delete("line")
        for linha in figuras:
            if linha[0] == 'linha':
                canvas.create_line(linha[2], fill=linha[1], tags="line")



    fim_x = None
    fim_y = None
    ini_x = None
    ini_y = None
    canvas.bind('<ButtonPress-1>', inicia_linha)
    canvas.bind('<B1-Motion>', atualiza_linha)
    canvas.bind('<ButtonRelease-1>', incluir_linha)

    