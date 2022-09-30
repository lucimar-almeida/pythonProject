# Operações Matemeticas

print(1 + 3)  # Adição
print(3 - 1)  # Subtração
print(2.2 * 5)  # Multiplicação
print(1 ** 3)  # potencia
print(1 / 3)  # Divisão
print(7 % 3)  # Resto da divisão

# Em python sempre separar numeros por pontos!
# Em python mantem as ordens das operações matematicas!
# ---------------------------------------------------------

# STRINGS

# concatenação
nome = "Lucimar"
print("Meu nome é " + nome + "!")

#in
# case sensiive - significa que maiusculo e minusculo é diferente para meios de comparação
print("Meu nome é" in "Lucimar")
print("L" in "Lucimar")

# ------------------------------------------------------------

# Variaveis

qde_vendas = "1500"
print("A quantidade de vendas foi de " + qde_vendas)

# -------------------------------------------------------

# Como pegar informação do ususario

nome = input("Qual é o seu nome?")
sobrenome = input("Qual é o seu sobrenome?")
print(nome + ' ' + sobrenome)

# ------------------------------------------------------
# Exercicios

qde_coca = 1500
qde_pepsi = 130
preco_coca = 1.50
preco_pepsi = 1.50
custo = 2500

print(qde_coca * preco_coca)
print(qde_pepsi * preco_pepsi)

faturamento = qde_coca * qde_coca + qde_pepsi * preco_pepsi
lucro = faturamento - custo
print(lucro)

codigo_bebida = input('Insira o codigo da bebida para saber se é alcoolica?')
print('BAC' in codigo_bebida)

# --------------------------------------------------------
# Variaveis
# int = Inteiro
# string = Texo
# float = Números com casas decimais (ponto flutuante)
# bool ou boolean = True pu False
# Obs. 1: Variaveis em Python não são decladas  explicitamente, mas isso não significa que vc deve ficar mudando o tempo todo 
# Obs. 2: Cuidado com os números restritos (arquivos p/ download)

