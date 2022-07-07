#Calcula a PA usando REPETIÇAO WHILE
num = int(input('Digite um numero: '))
razão = int(input('Digite a razão da PA: '))
cont = 1  #cont serve so pra sair do loop ele conta quantas vezes ele fez a conta PA+= RAZÃO E QUANDO CHEGA A 10 PARA
termo = num
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razão
    print(termo)
    cont += 1
print('FIM')
