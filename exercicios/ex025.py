#ANALISA SE TEM SILVA NO NOME
nome = str(input('Qual seu nome? ')).strip().lower()
silva = 'silva' in nome
print(f'seu nome é {nome}')
print(f'tem silva no nome? {silva}')