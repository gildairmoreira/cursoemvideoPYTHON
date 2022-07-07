#JOGO DA ADIVINHAÇAO
from random import randint
from time import sleep
num = randint(0,5)
print('--<>--'*10)
print('Vou pensar em um numero de 0 a 5 Tente adivinhar!!')
print('--<>--'*10)
sleep(1)
p = int(input('Qual o numero sorteado: '))
sleep(2)
if p == num:
    print('Acertou!!!!!')
else:
    print('ERROUUUUUUU!')
    print(f'O numero escolhido foi {num}')