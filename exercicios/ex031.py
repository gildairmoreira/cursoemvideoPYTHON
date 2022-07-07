#CALCULA PASSAGEM DE ONIBUS
travel = int(input('Quantos km/h terá sua viagem? '))
#preço = travel * 0.50 if travel <=200: else travel*0.45 >>>Forma simplificada SO COLOCAR O PRINT
if travel <=200:
    print(f'A sua viagem de {travel}km custará {(travel*0.5):.2f}R$')
else:
    print(f'A sua viagem de {travel}km custará {(travel*0.45):.2f}R$')
