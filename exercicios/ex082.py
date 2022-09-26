pares = []
impares = []
num = []
while True:
    num.append(int(input('Digite um numero: ')))
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
for v in num:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=='* 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
