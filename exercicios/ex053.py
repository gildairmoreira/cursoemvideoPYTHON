#ANALISA SE A FRASE E PALINDROMO SEM 'FOR'
frase = str(input('Escreva uma frase: ')).strip()
junto = frase.replace(" ","")
frase2= junto[::-1]
print(frase2)
if junto == frase2:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')
