#JOKENPO
from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
computador = randint(0,2)
print('''Suas opçoes
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
usuario = int(input('QUAL SUA JOGADA: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*15)
print(f'Computador jogou \033[4;35m{itens[computador].upper()}\033[m')
print(f'Jogador jogou \033[4;32m{itens[usuario].upper()}\033[m')
print('-='*15)
if computador == 0: #pc jogou pedra
    if usuario ==0:
        print('EMPATE !!!')
    elif usuario == 1:
        print('JOGADOR VENCE')
    elif usuario == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA !!!')
elif computador == 1: #pc jogou papel
    if usuario ==0:
        print('COMPUTADOR VENCE')
    elif usuario == 1:
        print('EMPATE')
    elif usuario == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA !!!')
elif computador == 2: #pcjogou tesoura
    if usuario ==0:
        print('JOGADOR VENCE')
    elif usuario == 1:
        print('COMPUTADOR VENCE')
    elif usuario == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA !!!')
