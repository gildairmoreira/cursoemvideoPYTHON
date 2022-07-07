#>>>CALCULA FATORIAL DE UM NUMERO
num = int(input('Digite um numero: '))
cont= num
fatorial = 1
print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print('x' if cont > 1 else '=', end='')
    fatorial *=cont
    cont -= 1
print(f'{fatorial}')

#>>>USANDO FOR
num = int(input('Digite um numero: '))
cont = num
fatorial = 1
print(f'{num}! = ', end='')
for c in range(cont,0,-1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else '=', end='')
    fatorial *= c
print(f' {fatorial}')
