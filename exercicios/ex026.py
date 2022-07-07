#ANALISADOR DE FRASE
frase = str(input('Escreva uma frase:')).strip()
letraA = frase.upper().count('A')
posiçao = frase.upper().find('A')
ultima = frase.upper().rfind('A')
print(f'A sua frase é {frase}')
print(f'A letra "A" aparece: {letraA} vezes')
print(f'A posiçao em que aparece a primeira vez é na {posiçao+1} posiçao')
print(f'A posiçao que aparece por ultimo é {ultima+1} posiçao')