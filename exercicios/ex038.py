#COMPARA DOIS NUMEROS PARA SABER QUAL E MAIOR MENOR OU IGUAL
n1 = int(input('Digite um Numero: '))
n2 = int(input('digite outro numero: '))
if n1 > n2:
    print(f'O primeiro valor ({n1}) e maior que o segundo valor ({n2})')
elif n2 > n1:
    print(f'O segundo valor ({n2}) e maior que o primeiro valor ({n1}) ')
else:
    print('Os dois valores são iguais')
