#olha quantas pessoas são maiores e menores de idade
from datetime import date
atual = date.today().year
contmaior=0
contmenor=0
for c in range(1,8):
    ano=int(input('Em que ano você nasceu?'))
    idade=atual-ano
    if idade < 21:
        contmenor = contmenor+1
    else:
        contmaior=contmaior+1
print(f'Dessas 7 Pessoas {contmaior} são maiores de idade é {contmenor} ainda não atingiram a maioridade')
