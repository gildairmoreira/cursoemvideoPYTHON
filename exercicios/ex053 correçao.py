#ANALISA SE E PALINDROMA USANDO FOR
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1): #O LENDO DO JUNTO VAI PEGAR A FRASE E CONTAR ATE A ULTIMA LETRA E -1 PRA IR DE TRAS PRA FRENTE
    inverso += junto[letra]
print(f'A frase {junto}, ao contrario fica {inverso}')
if junto == inverso:
    print('Essa frase e um palindromo')
else:
    print('Essa frase não é um palindromo')