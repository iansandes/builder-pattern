from abc import ABC, abstractmethod

class EnderecoBuilder(ABC):

    @abstractmethod
    def getEndereco(self):
        pass