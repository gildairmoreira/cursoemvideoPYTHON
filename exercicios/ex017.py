from math import hypot
co = float(input('Qual o cateto oposto?'))
cad = float(input('Qual o cateto adjacente?'))
hi = hypot(co, cad)
print(f'o triangulo com cateto oposto {co} e adjacente {cad} tem a hipotenusa de {hi:.2f}')

#co = float(input('Qual o cateto oposto?'))
#cad = float(input('Qual o cateto adjacente?'))
#hi = (co**2 + cad**2) ** (1/2)
#print(f'A hipotenusa vai mendir {hi:.2f}')