#JOGO DA ADIVINHAÇAO DE 0 A 10 COM MAIS CHANCES
from random import randint
from time import sleep
contador = 0
acertou = False
print('\033[31m======\033[m \033[4;34mJOGO DA ADIVINHAÇAO\033[m \033[31m======\033[m')
num = randint(0, 10)
while not acertou:
    jogador = int(input('Qual numero eu estou pensando de 0 a 10? '))
    sleep(1)
    contador += 1
    if jogador == num:
        acertou = True
    else:
        if jogador > num:
            print('Você \033[4;31mERROU\033[m tente um numero MENOR\n')
        elif jogador < num:
            print('Você \033[4:31mERROU\033[m tente um numero MAIOR\n')
print(f'Você \033[4;32mACERTOU!!!\033[m\nEu pensei no numero {num},Você precisou de {contador} tentativas para acertar')
