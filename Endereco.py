class Endereco():

    def __init__(self):
        self.rua = False
        self.praca = False
        self.avenida = False
        self.loteamento = False
        self.nome = False
        self.bairro = False
        self.numero = False
        self.cidade = False
        self.referencia = False
        self.estado = False
        self.pais = False

    def setNome(self, nome):
        self.nome = nome
    
    def setBairro(self, bairro):
        self.bairro = bairro

    def setNumero(self, numero):
        self.numero = numero

    def setReferencia(self, referencia):
        self.numero = numero

    def setCidade(self, cidade):
        self.cidade = cidade

    def setEstado(self, estado):
        self.estado = estado

    def setPais(self, pais):
        self.pais = pais

    def __str__(self):
        string = ""
        if self.rua:
            string += "Esta é uma Rua:  "
        if self.praca:
            string += "Esta é uma Praça: "
        if self.avenida:
            string += "Esta é uma Avenida: "
        if self.loteamento:
            string += "Este é um Loteamento: "
        if self.nome:
            string += self.nome + ", "
        else:
            string += "SEM NOME, "
        if self.bairro:
            string += self.bairro + ", "
        else:
            string += "SEM BAIRRO, "
        if self.numero:
            string += self.numero + ", "
        else:
            string += "SEM NÚMERO, "
        if self.referencia:
            string += self.referencia + ", "
        else:
            string += "SEM REFERÊNCIA, "
        if self.cidade:
            string += self.cidade + ", "
        else:
            string += "SEM CIDADE, "
        if self.estado:
            string += self.estado + ", "
        else:
            string += "SEM ESTADO, "
        if self.pais:
            string += self.pais + ", "
        else:
            string += "SEM PAÍS, "
        
        return string






        