larg = float(input('qual a altura da parede?'))
alt = float(input('qual a largura da parede?'))
area = larg * alt
tinta = area/2
print(f'Sua parede tem as dimensão de {larg}x{alt} e sua área e {area}m²')
print(f'para pintar a área da parede vai precisar de \033[35m{tinta:.2f}\033[mlitros de tinta')