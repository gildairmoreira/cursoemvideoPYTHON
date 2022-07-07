#ANALISA SEU PRIMEIRO E SEGUNDO NOME
nome = input('Digite seu nome completo').strip()
#pn = nome.split()[0]
#un = nome.split()[len(nome.split())-1]
print(f'primeiro nome:{nome.split()[0]}')
print(f'ultimo nome:{nome.split()[len(nome.split())-1]}')