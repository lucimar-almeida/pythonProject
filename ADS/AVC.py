# AVC
def title(t):
    print('='*20)
    print(t)
    print('='*20)

def space():
    print('-'*40)

#Programa principal

title('Teste de condutor')
nome = str(input('Qual é o seu nome: '))
title(f'Óla {nome} vamos começar seu teste de condutor')
acerto = 0
pergunta1 = str(input('''01 - Se o farol estiver vermelho, você pode avançar com o carro?
[ 1 ] Sim
[ 2 ] Não
: '''))
while pergunta1 != '1' and pergunta1 != '2':
    pergunta1 = str(input('''01 - Se o farol estiver vermelho, você pode avançar com o carro?
    [ 1 ] Sim
    [ 2 ] Não
    : '''))
if pergunta1 == '1':
    print('Você errou! estude mais o assunto.')
elif pergunta1 == '2':
    print('Parabens! Você acertou.')
    acerto += 1
space()

pergunta2 = str(input('''02 - Se o farol está amarelo, você deve acelerar o carro para passar?
[ 1 ] Sim
[ 2 ] Não
: '''))
while pergunta2 != '1' and pergunta2 != '2':
    pergunta2 = str(input('''02 - Se o farol está amarelo, você deve acelerar o carro para passar?
    [ 1 ] Sim
    [ 2 ] Não
    : '''))

if pergunta2 == '1':
    print('Você errou! estude mais o assunto.')
elif pergunta2 == '2':
    print('Parabens! Você acertou.')
    acerto += 1
space()

pergunta3 = str(input('''03 – Pergunta: Se o farol está verde e não há nenhum pedestre atravessando, você pode avançar?
[ 1 ] Sim
[ 2 ] Não
: '''))
while pergunta3 != '1' and pergunta3 != '2':
    pergunta3 = str(input('''03 – Pergunta: Se o farol está verde e não há nenhum pedestre atravessando, você pode avançar?
    [ 1 ] Sim
    [ 2 ] Não
    : '''))

if pergunta3 == '1':
    print('Parabens! Você acertou.')
    acerto += 1
elif pergunta3 == '2':
    print('Você errou! estude mais o assunto.')
space()

pergunta4 = str(input('''04 - Pergunta: Se o farol está verde e há pedestre atravessando, você pode avançar?
[ 1 ] Sim
[ 2 ] Não
: '''))
while pergunta4 != '1' and pergunta4 != '2':
    pergunta4 = str(input('''04 - Pergunta: Se o farol está verde e há pedestre atravessando, você pode avançar?
    [ 1 ] Sim
    [ 2 ] Não
    : '''))

if pergunta4 == '1':
    print('Você errou! estude mais o assunto.')
elif pergunta4 == '2':
    print('Parabens! Você acertou.')
    acerto += 1
space()

pergunta5 = str(input('''05 - Se o farol está vermelho, você deve parar o carro?
[ 1 ] Sim
[ 2 ] Não
: '''))
while pergunta5 != '1' and pergunta5 != '2':
    pergunta5 = str(input('''05 - Se o farol está vermelho, você deve parar o carro?
    [ 1 ] Sim
    [ 2 ] Não
    : '''))

if pergunta5 == '1':
    print('Parabens! Você acertou.')
    acerto += 1
elif pergunta5 == '2':
    print('Você errou! estude mais o assunto.')
space()

print(f'Parabéns {nome}, você acertou {acerto} perguntas!')