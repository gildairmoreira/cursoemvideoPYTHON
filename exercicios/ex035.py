#ANALISA SE 3 RETAS PODEM FORMAR UM TRIANGULO
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Qual o comprimento da primeira reta? '))
r2 = float(input('Qual o comprimento da segunda reta? '))
r3 = float(input('Qual o comprimento da terceira reta? '))
lista = [r1,r2,r3]
ma = max(lista)
if (r1+r2+r3)-ma > ma:
    print('Essas retas podem formar um Triangulo')
else:
    print('Essas reta não podem formar um Triangulo')