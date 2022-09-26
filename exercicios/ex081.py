cont = 0
lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    cont += 1
    while True:
        continuar = str(input('Quer continua? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
lista.sort(reverse=True)
print('=' * 30)
print(f'Você Digitou {cont} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte Da lista')
else:
    print('O valor 5 não faz parte da lista')
