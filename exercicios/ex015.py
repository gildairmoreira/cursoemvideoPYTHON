dias = int(input('Quantos dias ficou alugado?'))
km = float(input('Quantos km percorreu?'))
qdia = dias * 60
qkm = km * 0.15
print(f'Você ficou {dias} com o carro e rodou {km}km,você deve pagar {qdia+qkm}r$')