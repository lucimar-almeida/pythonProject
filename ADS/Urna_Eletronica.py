# Projeto ADS - "Urna Eletronica"

def tela(titulo):
    print('-' * 30)
    print(titulo)
    print('-' * 30)


def space():
    print(' ')


def subtitulo(text):
    print('-' * 5, text, '-' * 5)


# Candidatos a prefeito
prefeitos = [{'Candidato': 'Ademir da Guia', 'votos': 0}, # 'Número': 10
             {'Candidato': 'João Gois', 'votos': 0}] # 'Número': 20

# Condidatos a vereadores
vereadores = [{'vereador': 'Ana Maria', 'votos': 0}, #'Número': 35401
              {'vereador': 'Luiz Herminio', 'votos': 0}, # Número': 25600
              {'vereador': 'Fernanda Silva', 'votos': 0}, # Número': 10123
              {'vereador': 'Felipe Camargo', 'votos': 0}, # Número': 10456
              {'vereador': 'Evandro Alves', 'votos': 0}, # Número': 20256
              {'vereador': 'Rafael Sugesmundo', 'votos': 0}, # Número': 20789
              {'vereador': 'Marcos Pacheco', 'votos': 0}, # Número': 10333
              {'vereador': 'Fabio Henrique', 'votos': 0}, # Número': 20963
              {'vereador': 'Jean Gomes', 'votos': 0}, # Número': 10100
              {'vereador': 'Jessica Mendes', 'votos': 0} # 'Número': 35555
              ]

#Votos brancos e nulos
nulos_brancos_prefeitos = [{'Nulos': 0}, {'Brancos': 0}]
nulos_brancos_vereadores = [{'Nulos': 0}, {'Brancos': 0}]


tela('         Eleições 2022')
tela('''Candidatos a prefeito:
     [ 10 ] Ademir da Guia
     [ 20 ] João Gois
     
Candidatos a vereador:
     [ 35401 ] Ana Maria
     [ 25600 ] Luiz Herminio
     [ 10123 ] Fernanda Silva
     [ 10456 ] Felipe Camargo
     [ 20256 ] Evandro Alves
     [ 20789 ] Rafael Sugesmundo
     [ 10333 ] Marcos Pacheco
     [ 20963 ] Fabio Henrique
     [ 10100 ] Jean Gomes
     [ 35555 ] Jessica Mendes
     ''')

def tela_principal():
    opt = int(input('''Digite:
    [ 1 ] Zerésima
    [ 2 ] Iniciar votação
    : '''))
    # if opt != 2:
    #      tela_principal()
    # elif opt != 1:
    #     tela_principal()
    if opt == 1:
        tela('       Zerésima')
        space()
        subtitulo('Candidatos a prefeitos')
        for e in prefeitos:
            for k, v in e.items():
                print(f'{k} {v}')
        space()
        subtitulo('Candidatos a vereador')
        for e in vereadores:
            for k, v in e.items():
                print(f'{k} {v}')
        tela_principal()

    elif opt == 2:
        tela_votação_prefeito()
def tela_votação_prefeito():
    tela('       Votação')
    space()
    subtitulo('Voto para prefeito')
    voto = int(input('Digite o número do seu candidato a prefeito'
                     '\nou digite 1 para votar em "Branco": '))
    if voto == 10:
        conf = int(input('''Confirma seu voto em ADEMIR DA GUIA para vereador:
                                                 [ 1 ] Sim
                                                 [ 2 ] Não
                                                 : '''))
        if conf == 1:
            print('Ademir da Guia')
            prefeitos[0]['votos'] += 1
            tela_votação_vereador()
        else:
            tela_votação_prefeito()
    elif voto == 20:
        conf = int(input('''Confirma seu voto em JOÃO GOIS para vereador:
                                                         [ 1 ] Sim
                                                         [ 2 ] Não
                                                         : '''))
        if conf == 1:
            print('João Gois')
            prefeitos[1]['votos'] += 1
            tela_votação_vereador()
        else:
            tela_votação_prefeito()
    elif voto == 1:
        option = str(input('tem certeza que deseja votar em "BRANCO"? Sim = [S], Não = [N]: '))
        if option == 's':
            print('Seu voto foi "Branco" para prefeito.')
            nulos_brancos_prefeitos[1]['Brancos'] += 1
            tela_votação_vereador()
        else:
            tela_votação_prefeito()
    else:
        option = str(input('Tem certeza que quer anular seu voto? Sim = [S], Não = [N]: '))
        if option == 'n':
            tela_votação_prefeito()
        else:
            print('Seu voto para prefeito foi anulado.')
            nulos_brancos_prefeitos[0]['Nulos'] += 1
            tela_votação_vereador()

def tela_votação_vereador():
    tela('        Votação')
    space()
    subtitulo('Voto para vereador')
    voto = int(input('Digite o número do seu candidato a vereador'
                     '\nou digite 1 para votar em "Branco": '))
    if voto == 35401:
        conf = int(input('''Confirma seu voto em ANA MARIA:
                         [ 1 ] Sim
                         [ 2 ] Não
                         : '''))
        if conf == 1:
            print('Ana Maria')
            vereadores[0]['votos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    elif voto == 25600:
        conf = int(input('''Confirma seu voto em LUIZ HERMINIO para vereador:
                                 [ 1 ] Sim
                                 [ 2 ] Não
                                 : '''))
        if conf == 1:
            print('Luiz Herminio')
            vereadores[1]['votos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    elif voto == 10123:
        conf = int(input('''Confirma seu voto em FERNANDA SILVA para vereador:
                                         [ 1 ] Sim
                                         [ 2 ] Não
                                         : '''))
        if conf == 1:
            print('Fernanda Silva')
            vereadores[2]['votos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    elif voto == 10456:
        conf = int(input('''Confirma seu voto em FELIPE CAMARGO para vereador:
                                         [ 1 ] Sim
                                         [ 2 ] Não
                                         : '''))
        if conf == 1:
            print('Felipe Camargo')
            vereadores[3]['votos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    elif voto == 20256:
        conf = int(input('''Confirma seu voto em EVANDRO ALVES para vereador:
                                         [ 1 ] Sim
                                         [ 2 ] Não
                                         : '''))
        if conf == 1:
            print('Evandro Alves')
            vereadores[4]['votos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    elif voto == 20789:
        conf = int(input('''Confirma seu voto em RAFAEL SUGESMUNDO para vereador:
                                         [ 1 ] Sim
                                         [ 2 ] Não
                                         : '''))
        if conf == 1:
            print('Rafael Sugesmundo')
            vereadores[5]['votos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    elif voto == 10333:
        conf = int(input('''Confirma seu voto em MARCOS PACHECO para vereador:
                                         [ 1 ] Sim
                                         [ 2 ] Não
                                         : '''))
        if conf == 1:
            print('Marcos Pacheco')
            vereadores[6]['votos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    elif voto == 20963:
        conf = int(input('''Confirma seu voto em FABIO HENRIQUE para vereador:
                                         [ 1 ] Sim
                                         [ 2 ] Não
                                         : '''))
        if conf == 1:
            print('Fabio Henrique')
            vereadores[7]['votos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    elif voto == 10100:
        conf = int(input('''Confirma seu voto em JEAN GOMES para vereador:
                                         [ 1 ] Sim
                                         [ 2 ] Não
                                         : '''))
        if conf == 1:
            print('Jean Gomes')
            vereadores[8]['votos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    elif voto == 35555:
        conf = int(input('''Confirma seu voto em JESSICA MENDES para vereador:
                                         [ 1 ] Sim
                                         [ 2 ] Não
                                         : '''))
        if conf == 1:
            print('Jessica Mendes')
            vereadores[9]['votos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    elif voto == 1:
        option = str(input('tem certeza que deseja votar em "BRANCO"? Sim = [S], Não = [N]: '))
        if option == 's':
            print('Seu voto foi "Branco" para vereador.')
            nulos_brancos_vereadores[1]['Brancos'] += 1
            tela_fim()
        else:
            tela_votação_vereador()
    else:
        option = str(input('Tem certeza que quer anular seu voto? Sim = [S], Não = [N]: '))
        if option == 'n':
            tela_votação_vereador()
        else:
            print('Seu voto para vereador foi anulado.')
            nulos_brancos_vereadores[0]['Nulos'] += 1
            tela_fim()

def tela_fim():
    tela('FIM')
    opt = int(input('''Digite:
    [ 1 ] Iniciar nova votação
    [ 2 ] Finalizar processo de votação e imprimir resultados
    : '''))
    if opt == 1:
        tela_votação_prefeito()
    elif opt == 2:
        tela('       Resultados')
        space()
        subtitulo('Candidatos a prefeitos')
        for e in prefeitos:
            for k, v in e.items():
                print(f'{k} {v}')
        space()
        subtitulo('Candidatos a vereador')
        for e in vereadores:
            for k, v in e.items():
                print(f'{k} {v}')
        space()
        subtitulo('Nulos e Brancos para prefeito')
        for e in nulos_brancos_prefeitos:
            for k, v in e.items():
                print(f'{k} {v}')
        space()
        subtitulo('Nulos e Brancos para vereador')
        for e in nulos_brancos_vereadores:
            for k, v in e.items():
                print(f'{k} {v}')
    else:
        tela_fim()

tela_principal()