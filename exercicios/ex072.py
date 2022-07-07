num = ('Zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    p = int(input('Digite um numero Entre 0 é 20: '))
    if 0 <= p <= 20:
        print(f'O numero escrito por extenso é {num[p]}')
        while c != 'SN':
            c = str(input('Quer continuar? [S/N]')).strip().upper()
            if c == 'S':
                break
        break
print('FIM')