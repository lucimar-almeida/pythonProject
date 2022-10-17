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

# in
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

# -------------------------------------------------------
faturamento = 1000
custo = 500
lucro = faturamento - custo
print('O faturamento foi ' + str(faturamento) + ' reais.')
print('O custo da loja foi de ' + str(custo) + ' reais.')
print('A assim o lucro da loja foi de ' + str(lucro) + ' reais.')

print('O faturamento da lojo foi de {}'.format(faturamento))

print('O faturamento da loja foi {} reais. O custo da loja foi de {} reais. O lucro da loja foi de {} reais.'.format(
    faturamento, custo, lucro))

# ------------------------------------------------------
# Comparadores
# == igual
# != diferente
# > maior que
# < menor que
# in texto existe dentro de outro
# not verifica o contrario da comparação
# Em alguma operação vc não quiser fazer nada, simplesmente use o   pass

# -----------------------------------------------------

meta = 50000
qtde_vendidas = 56000

if qtde_vendidas > meta:
    print('batemos a meta de vendas de Iphone, vendemos {} unidades.'.format(
        qtde_vendidas))
print('Fim do programa!')

# ------------------------------------------------------

meta = 1000

vendas_funcionario_1 = 1000
vendas_funcionario_2 = 770
vendas_funcionario_3 = 2700


if vendas_funcionario_1 >= 1000:
    print('O funcionario 1 ganhou {} bonus.'.format(meta * 0.1))
else:
    print('O funcionario 1 não ganhou bônus.')

if vendas_funcionario_2 >= 1000:
    print('O funcionario 2 ganhou {} bonus.'.format(meta * 0.1))
else:
    print('O funcionario 2 não ganhou bônus.')

if vendas_funcionario_3 >= 1000:
    print('O funcionario 3 ganhou {} bonus.'.format(meta * 0.1))
else:
    print('O funcionario 3 não ganhou bônus.')

print('-----------------------------------------')


if vendas_funcionario_1 >= 2000:
    bonus = (vendas_funcionario_1 * 0.015)
elif vendas_funcionario_1 < 2000:
    bonus = (vendas_funcionario_1 * 0.01)
else:
    bonus = 0
print('O funcionario 1 ganhou {} de bônus!'.format(bonus))

if vendas_funcionario_2 >= 2000:
    bonus = (vendas_funcionario_2 * 0.015)
elif vendas_funcionario_2 < 2000:
    bonus = (vendas_funcionario_2 * 0.01)
else:
    bonus = 0
print('O funcionario 2 ganhou {} de bônus!'.format(bonus))

if vendas_funcionario_3 >= 2000:
    bonus = (vendas_funcionario_3 * 0.015)
elif vendas_funcionario_3 < 2000:
    bonus = (vendas_funcionario_3 * 0.01)
else:
    ponus = 0
print('O funcionario 3 ganhou {} de bônus!'.format(bonus))

print('-----------------------------------------')


meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 5000
vendas_loja = 200000

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print('Bônus do funcionario foi de {}.'.format(bonus))
else:
    print('O funcionario não ganhou bônus.')

print('-----------------------------------------')

nota_meta = 9
nota_funcionario = 5

if nota_funcionario >= nota_meta or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja):
    bonus = vendas_funcionario * 0.015
    print('O funcionario ganhou {} de bônus!'.format(bonus))
else:
    print('O funcionario não ganhou bônus!')
# -------------------------------------------------------------

faturamento = input('Qual o faturamento da loja?')
custo = input('Qual o custo da loja?')

if faturamento:
    lucro = int(faturamento) - int(custo)
    print('O lucro da loja foi de {} reais'.format(lucro))
else:
    print('Preencha corretamente os espaços necessarios!')


# --------------------------------------------------------
produto = str(input('Qual o produto?'))
categoria = str(input('Qual a categoria do Produto?'))
qtde_str = str(input('Qual a quantidade do produto?'))


if produto and categoria and qtde_str:
    qtde = int(qtde_str)
    if categoria == 'bebidas':
        if qtde < 75:
            print(
                f'Soliciatar {categoria} a equipe de compras, temos apenas {qtde} unidades em estoque.')
    if categoria == 'limpeza':
        if qtde < 30:
            print(
                f'Solicitar {categoria} a equipe de compras, temos apenas {qtde} unidades em estoque.')

else:
    print('Preencha todas as informações')

# -----------------------------------------------------
# exercicio 1
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

if numero_1 > numero_2:
    print(f'O número maior é {numero_1}')
elif numero_2 > numero_1:
    print(f'O número maior é {numero_2}')
else:
    print(f'Os números {numero_1} e {numero_2} são iguais!')

# -----------------------------------------------------
# exercicio 2

numero = int(input('Digite um número: '))
if numero > 0:
    print(f'O número {numero} é positivo!')
elif numero < 0:
    print(f'O número {numero} é negativo!')
else:
    print('O número é 0 e não é positivo e nem negativo!')

# -----------------------------------------------------
# exercicio 3


def qual_sexo():
    sexo = input('F - Feminino\nM - Masculino\n:')
    if sexo == 'f':
        print('O sexo é feminino.')
    elif sexo == 'm':
        print('o sexo é masculino.')
    else:
        print('Digite "F" ou "M"?')
        qual_sexo()


qual_sexo()

# -----------------------------------------------------
# exercicio 4

emails_spams = ('fulano@gmail.com, beltrano@gmail.com, ciclano@gmail.com')


def validacao():
    email = input('Digite o email para a verificação no banco de dados: ')

    if '@' in email and '.com' in email:
        if email in emails_spams:
            print('Email encontrado no sistema.')
        else:
            print('Email não encontrado no sistema.')
            validacao()
    else:
        print('Email invalido! tente novamente.')
        validacao()


validacao()

# -----------------------------------------------------
# exercicio 5

# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))


def calculo_nota(n1, n2):

    media = (n1 + n2) / 2

    if media < 7:
        print(f'Reprovado, sua média é menor que {media}!')
    elif media >= 7 and media < 9.5:
        print(f'Aprovado, sua média é maior que {media}!')
    elif media == 10:
        print(f'Aprovado com destinção, sua média foi {media}!')


calculo_nota(nota1, nota2)

# ----------------------------------------------------
# Exercicio 9
# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.


