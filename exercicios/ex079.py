num = []
while True:
    valor = (int(input('Digite um numero: ')))
    if valor not in num:
        num.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor Repetido, não sera Adicionado')
    while True:
        conti = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if conti in 'SN':
            break
    if conti in 'N':
        break
num.sort()
print('-='*20)
print(f'Você Digitou os valores {num}')
