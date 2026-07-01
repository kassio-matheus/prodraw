from tkinter import *
from abc import ABC, abstractmethod

#SO DEPOIS A GENTE VAI USAR ISSO 


class Screen(ABC):
    def __init__(self, canva: Canvas, window: Tk):
        self.canva = canva
        self.window = window

    @abstractmethod
    def create_draw(self):
        pass
