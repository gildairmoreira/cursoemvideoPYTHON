#OLHA SE TAL NUMERO E PRIMO OU NÃO
num = int(input('Digite um numero: '))
tot = 0
print('''====Se o Numero aparecer Vermelho ele não é divisivel pelo numero escolhido==== ''')
for n in range(1, num + 1):
    if num % n == 0:
        print('\033[32m')
        tot = tot + 1
    else:
        print('\033[31m')
    print(f'{n}', end=' ')
print(f'\nO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print(f'O numero {num} é um numero primo')
else:
    print(f'O numero {num} não é um numero primo')
