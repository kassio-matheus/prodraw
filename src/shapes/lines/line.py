from src.shapes.points import Ponto

class Linha:

    def __init__(self, ponto1 = Ponto(), ponto2 = Ponto()):
        self.__ponto1 = ponto1
        self.__ponto2 = ponto2

    @property
    def ponto1(self):
        return self.__ponto1
    
    @ponto1.setter
    def ponto1(self, ponto1):
        self.__ponto1 = ponto1

    @property
    def ponto2(self):
        return self.__ponto2
    
    @ponto2.setter
    def ponto2(self, ponto2):
        self.__ponto2 = ponto2