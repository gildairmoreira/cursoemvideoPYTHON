#ALISTAMENTO
from datetime import date
ano = (int(input('Que no você nasceu? ')))
atual = date.today().year
idade = (atual-ano)
if idade < 18:
    print(f'Ainda não chegou a hora de se alistar, falta {(18-idade)} ano(s)')
    print(f'Seu alistamento será em {atual+(18-idade)} ano')
elif idade == 18:
    print('Você completou 18 anos, é hora de se alistar')
elif idade > 18:
    print(f'Jà passou da hora de se alistar você está {(idade-18)} ano(s) Atrasado')
    print(f'Seu alistamento foi em {atual - (idade-18)} ano')