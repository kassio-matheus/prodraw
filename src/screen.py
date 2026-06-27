from tkinter import *
from abc import ABC, abstractmethod

class Tela(ABC):
    def __init__(self, canva: Canvas, janela: Tk):
        self.canva = canva
        self.janela = janela
    
    @abstractmethod
    def criar_forma(self):
        pass