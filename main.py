from EnderecoDirector import RuaSemReferenciaBuilder, AvenidaApenasComNomeBuilder

builder = RuaSemReferenciaBuilder()
builder.getEndereco()
print(builder.getProduto())

builder = AvenidaApenasComNomeBuilder()
builder.getEndereco()
print(builder.getProduto())