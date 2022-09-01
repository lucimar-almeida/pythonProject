# Criar uma classe de produtos de um supermercado

class produto:
    def __init__(self, produto1, produto2, produto3, produto4):
        self.produto1 = produto1
        self.produto2 = produto2
        self.produto3 = produto3
        self.produto4 = produto4

    def preco(self):
        print('R$20')


cliente1 = produto('Banana', 'Maça', 'Abacaxi', 'Melão')
print(cliente1.produto1, cliente1.produto2,
      cliente1.produto3, cliente1.produto4)

cliente1.preco()

cliente2 = produto('Sabão', 'Detergente', 'Alvejante', 'Sabão em pó')
print(cliente2.produto1, cliente2.produto2,
      cliente2.produto3, cliente2.produto4)

cliente2.preco()
