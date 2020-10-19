from EnderecoBuilder import EnderecoBuilder
from Endereco import Endereco

class RuaSemReferenciaBuilder(EnderecoBuilder):

    def __init__(self):
        self.produto = Endereco()

    def getProduto(self):
        return self.produto

    def getEndereco(self):
        self.produto.rua = True
        self.produto.setNome("Rua da Tocaia")
        self.produto.setNumero("18")
        self.produto.setBairro("Bairro das Estrelas")
        self.produto.setCidade("Lagarto")
        self.produto.setEstado("Sergipe")
        self.produto.setPais("Brasil")

class AvenidaApenasComNomeBuilder(EnderecoBuilder):
    
    def __init__(self):
        self.produto = Endereco()

    def getProduto(self):
        return self.produto

    def getEndereco(self):
        self.produto.avenida = True
        self.produto.setNome("Avenida 13 de Julho")
        