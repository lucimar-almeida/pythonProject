
# Exercício 3
# Crie um sistema de consulta de bônus dos funcionários
# Seu sistema deve:
# - Pegar o valor de vendas do funcinoário por meio de um input
# - Calcular o bônus do funcionário de acordo com a seguinte regra:
#       - Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para cada unidade vendida
#       - Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para cada unidade + um valor fixo de R$1000
#       - Se o funcionário vendeu menos de 1000 unidades, ele não ganha bônus
# - Printar no final o valor do bônus do funcionário
vendas_fucionario = float(input('Digite o valor de vendas feitas pelo funcionario: '))
if vendas_fucionario > 1000:
    print(f'O valor do bônus do funcionario é R${vendas_fucionario * 2}')
elif vendas_fucionario > 5000:
    print(f'O valor do bônus do funcionario é R${vendas_fucionario * 2}')
else:
    print(f'O funcionario não ganhará bônus, ficou abaixo da meta miníma.')



# Exercício 4
# Crie um programa que consiga descobrir qual dos vendedores vendeu mais
# As vendas dos vendedores são listas com a quantidade vendida por cada vendedor

vendas = [
    [10, 20, 100, 80, 90, 100, 20, 30, 44, 55, 33, 34, 100, 90, 80, 39, 87, 45, 50, 50, 50, 50, 40, 30, 3, 93, 39, 49, 88],    
    [100, 1, 1, 4, 5, 90, 100, 20, 4, 5, 100, 100, 100, 100, 100, 93, 20, 15, 40, 90, 90, 90, 90, 90, 90, 33, 22, 44, 43, 34],
]