# nome = str(input('qual é o seu nome?'))
# if nome == 'Lucimar':
#     print('Que nome lindo você tem!')
# else:
#     print('Que nome tão normal!')
# print('Bom dia, {}'.format(nome))

#----------------------------------------------------------------------------

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 6:
    print('Parabens, sua media é {}, você esta aprovado!'.format(m))
else:
    print('Sua media é de {} e você esta reprovado, estude mais!'.format(m))