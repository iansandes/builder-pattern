from abc import ABC, abstractmethod

class RoboBuilder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_componentes(self):
        pass

    @abstractmethod
    def build_sistema_deteccao(self):
        pass