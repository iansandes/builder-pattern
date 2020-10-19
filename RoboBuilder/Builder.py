from Robo import *
from RoboBuilder import RoboBuilder

class HumanoideBuilder(RoboBuilder):
    def __init__(self):
        self.produto = Robo()

    def reset(self):
        self.produto = Robo()

    def get_produto(self):
        return self.produto

    def build_componentes(self):
        self.produto.bipede = True
        self.produto.bracos = True
        self.produto.componentes.append(DuasPernas())
        self.produto.componentes.append(Bracos())

    def build_sistema_deteccao(self):
        self.produto.sistemas_deteccao.append(SistemaDeteccaoCamera())

class CarroAutonomoBuilder(RoboBuilder):
    def __init__(self):
        self.produto = Robo()

    def reset(self):
        self.produto = Robo()

    def get_produto(self):
        return self.produto

    def build_componentes(self):
        self.produto.com_rodas = True
        self.produto.com_rodas.append(QuatroRodas())

    def build_sistema_deteccao(self):
        self.produto.sistemas_deteccao.append(SistemaDeteccaoInfravermelho())