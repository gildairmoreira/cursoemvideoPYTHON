'''nome = str(input('Qual é seu nome:')).strip().lower()
if nome == 'gildair':
    print('Que nome bonito você tem!')
else:
    print('Seu nome e uma merda')
print(f'bom dia, {nome}')'''

n1 = float(input('Qual a sua nota? '))
n2 = float(input('Qual a segunda nota? '))
m = (n1+n2)/2
print(f'A sua nota media foi de {m:.1f}')

'''print('PARABENS' if m >=6 else 'ESTUDE MAIS')'''
if m >= 6.0:
    print('nice boy')
else:
    print('Bad note')