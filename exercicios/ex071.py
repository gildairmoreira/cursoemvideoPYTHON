print('='*30)
print('     CAIXA ELETRONICO')
print('='*30)
valor = int(input('Qual valor deseja Sacar: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= 50
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de {ced} reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced == 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao Caixa Eletrônico')

