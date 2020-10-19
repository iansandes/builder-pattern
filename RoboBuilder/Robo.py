class Robo:
    def __init__(self):
        self.bipede = False
        self.quadrupede = False
        self.com_rodas = False
        self.voador = False
        self.componentes = []
        self.sistemas_deteccao = []

    def __str__(self):
        string = ""
        if self.bipede:
            string += "Bípede"
        if self.quadrupede:
            string += "Quadrúpede "   
        if self.voador:
            string += "Voador "
        if self.com_rodas:
            string += "Robô com rodas\n"
        else:
            string = "ROBOT" + string + "\n"

        if self.componentes:
            string += "Componentes instalados:\n"

        for module in self.componentes:
            string += "- " + str(module) + "\n"

        if self.sistemas_deteccao:
            string += "Sistemas de detecccao instalados:\n"

        for system in self.sistemas_deteccao:
            string += "- " + str(system) + "\n"

        return string

class DuasPernas:
    def __str__(self):
        return "Duas Pernas"

class QuatroPernas:
    def __str__(self):
        return "Quatro Pernas"

class Bracos:
    def __str__(self):
        return "Dois Braços"

class Asas:
    def __str__(self):
        return "Asas"

class QuatroRodas:
    def __str__(self):
        return "Quatro Rodas"

class DuasRodas:
    def __str__(self):
        return "Duas Rodas"

class SistemaDeteccaoCamera:
    def __str__(self):
        return "Câmeras"

class SistemaDeteccaoInfravermelho:
    def __str__(self):
        return "Infravermelho"