dados = dict()
dados = {'nome': 'Pedro', 'Idade': 25}
dados['Sexo'] = 'M' # Para adicionar um item no dicionario, não precisa de append
del dados['Idade'] # Para deletar um item
print(dados)

#-------------------------------------------------------------------------------------

filme = {
    'Titulo': 'Star Wars',
    'Ano': '1977',
    'Diretor': 'George Lucas'
}

# print(filme.keys()) # Para pegar apenas as chaves (O que seria os index)
# print(filme.values()) # Para pegar os valores dentro dos keys (index)
# print(filme.items()) # Para pegar tanto as keys e os valores

for k, v in filme.items():
    print(f'O {k} é {v}')
print('-------------------------------------------------------------------------')

pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
print(f'{pessoas["nome"]} tem {pessoas["Idade"]} anos.')
print(pessoas.values())

print('---------------------------------------------------------------')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])

print('-------------------------------------------------------------------')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v, in e.items():
       # print(f'O campo {k} tem valor {v}.')
