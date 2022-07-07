#ANALISA QUAL NUMERO DOS DIGITADOS E MAIOR
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
lista = [n1, n2, n3]
print(f'O numero com valor mais alto é {max(lista)} e com o mais baixo é {min(lista)}')
# Vendo o menor usando if
'''if n1 < n2 or n1 < n3:
    menor = n1
if n2 < n1 or n2 < n3:
    menor = n2
if n3 < n1 or n3 < n2:
    menor = n3
# Vendo o Maior usando if
if n1 > n2 or n1 > n3:
    maior = n1
if n2 > n1 or n2 > n3:
    maior = n2
if n3 > n1 or n3 > n2:
    maior = n3
print(f'O numero maior é {maior} é o menor {menor}')'''
