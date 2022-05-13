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

locadora = []
