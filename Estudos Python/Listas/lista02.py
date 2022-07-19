# pessoas = [['Lucimar', 34], ['Ana', 28], ['priscila', 36]]
# print(pessoas[2])

#-------------------------------------------------------------------------------------------------

# teste = list()
#
# teste.append('Lucimar')
# teste.append(34)
# galera = list()
# galera.append(teste[:]) # Se não usar os dois pontos após(:) teste, ele não fará uma cópia e sim uma ligação.
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

#-----------------------------------------------------------------------------------------------------------------

# galera = [['Lucimar', 34], ['Ana', 28], ['priscila', 36], ['João', 30]]
#
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

#---------------------------------------------------------------------------------------------------------------

galera = list()
dado = list()
totalMaior = totalmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] > 30:
        print(f'{p[0]} é maior de idade.')
        totalMaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1
print(f'Temos {totalmenor} de idade e {totalMaior} de idade.')  