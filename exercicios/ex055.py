#olhar quem te o pesso mais pesado e mais leve
peso = []
for c in range(1,6):
    peso.append(float(input('informe seu peso: ')))
print(f'A pessoa mais pessada dos 5 informados é a que pesa {max(peso)}Kg e a mais leve é a que pesa {min(peso)}Kg')