#SORTEIO
import random

no1 = input('qual o nome dos aluno 1?')
no2 = input('qual o nome do aluno 2?')
no3 = input('qual o nome do aluno 3?')
no4 = input('qual o nome do aluno 4?')
lista= random.choice([no4, no3, no2, no1])
print(f'O aluno escolhido foi {lista}')