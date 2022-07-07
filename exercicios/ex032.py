#ANALISA SE O ANO E BISEXTO
from datetime import date
ano = int(input('Em que Ano você está? Coloque (0) para ver do ano atual:'))
if ano==0:
    ano=date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano}, É Bissexto')
else:
    print(f'O ano {ano}, não é Bissexto')