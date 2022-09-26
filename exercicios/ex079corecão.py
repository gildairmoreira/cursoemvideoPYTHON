num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!!!')
    else:
        print('Valor Duplicado, não foi Adicionado')
    r = str(input('Quer continua? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('==' * 30)
num.sort()
print(f'Você Digitou os valores {num}')
