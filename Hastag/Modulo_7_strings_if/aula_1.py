email = "lucimar@gmail.com"
nome = 'Lucimar'

print(len(nome))
print(email[9])
print(email[:-1])
print(email[5:8])

# metodos

texto = 'lucimar'
print(texto.capitalize())
# print(texto.casefold())
print(texto.count('u'))

text1 = 'lucimar@gmail.com'

print(text1.endswith('gmail.com'))

print(text1.find('@'))

texto2 = '1000.00'

print(texto2.replace('.', ','))

# texto.strip() -> retira tudo antes e depois do texto

nome1 = input('Digite seu nome')
e_mail = input('Digite seu a-mail')

if nome1 and e_mail:
    pos_a = e_mail.find('@') 
    servidor = e_mail[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro concluido!')        
else:
    print('Digite seu nome e seu email corretamente!')