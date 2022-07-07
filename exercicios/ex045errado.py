#JOKENPO modo ERRADO
import random
lista = ('papel tesoura pedra').split()
esc = random.choice(lista)
print('-=-'*20)
print('VAMOS JOGAR \033[4;31mPEDRA\033[m \033[4;32mPAPEL\033[m \033[4;33mTESOURA\033[m !!!!!')
print('-=-'*20)
usu = str(input('Escolha PEDRA,PAPEL ou TESOURA:')).lower().strip()
if esc == 'papel' and usu == 'pedra':
    print(f'Você perdeu eu escolhi {esc}')
elif usu == 'papel' and esc == 'tesoura':
    print(f'Você perdeu eu escolhi {esc}')
elif usu == 'papel' and esc == 'papel':
    print(f'EMPATE eu escolhi {esc}')
elif esc == 'pedra' and usu == 'papel':
    print(f'Você ganhou eu escolhi {esc}')
elif esc == 'pedra' and usu == 'tesoura':
    print(f'Você perdeu eu escolhi {esc}')
elif esc == 'pedra' and usu == 'pedra':
    print(f'EMPATE eu escolhi {esc}')
elif esc == 'tesoura' and usu == 'papel':
    print(f'Você perdeu eu escolhi {esc}')
elif esc == 'tesoura' and usu == 'pedra':
    print(f'Você ganhou eu escolhi {esc}')
elif esc == 'tesoura' and usu == 'tesoura':
    print(f'EMPATE eu escolhi {esc}')