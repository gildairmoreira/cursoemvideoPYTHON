#TERMOS DE PA
print('='*32)
print('      TERMOS DE UMA PA')
print('='*32)
primeiro = int(input('Digite um numero: '))
razão = int(input('Digite a Razão da PA: '))
decimo = primeiro+(10-1)*razão
for c in range(primeiro, decimo+razão, razão):
    print(c,end='-')
print('ACABOU')