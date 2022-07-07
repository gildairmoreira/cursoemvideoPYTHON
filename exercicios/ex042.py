# OLHA SE RETAS PODE FORMAR TRIANGULO E MOSTRA Q TIPO DE TRIANGULO
r1 = float(input('Qual o comprimento da primeira reta? '))
r2 = float(input('Qual o comprimento da segunda reta?'))
r3 = float(input('Qual o comprimento da terceira reta? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triângulo',end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Não pode formar um triângulo')