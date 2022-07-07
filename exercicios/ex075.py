num = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
       int(input('Digite um numero: ')), int(input('Digite um numero: ')),)
print(f'Você Digitou os valores {num}')
print(f'O numero 9 Apareceu {num.count(9)} Vezes')
if 3 in num:
    print(f'O Valor 3 apareceu na posição {num.index(3) + 1}ª')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')
