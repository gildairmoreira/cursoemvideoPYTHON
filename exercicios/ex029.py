#RADAR DE MULTA
velo = int(input('Qual a velocidade atual do carro?'))
if velo >=80:
    print(f'MULTADO! Você Passou no radar de 80Km/h á {velo}km/h é foi multado')
    print(f'Você receberá uma multa de {(velo-80)*7}R$')
print(f'Você passou no radar á {velo}km/h é não foi multado PARABÉNS')