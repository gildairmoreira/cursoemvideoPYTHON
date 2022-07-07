#CATEGORIAS DE ATLETAS DE ACORDO IDADE
from datetime import date
ano = int(input('Em que ano Você nasceu? '))
idade = (date.today().year) - ano
if idade <= 9:
    print('A categoria Que você vai competir é a MIRIM')
elif idade <= 14:
    print('A categoria Que você vai compertir é a INFANTIL')
elif idade <= 19:
    print('A categoria Que você vai competir é a JUNIOR')
elif idade <= 25:
    print('A categoria que você vai competir é a SÊNIOR')
else:
    print('A categoria que você vai competir é a MASTER')
