#MELHORANDO O 61 PERGUNTANDO QUANTOS QUER A MAIS
num = int(input('Digite um numero: '))
razão = int(input('Digite a razão da PA: '))
cont = 1
termo = num
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voçe quer mostra a mais? '))
print(f'Progresão Finalizada com {total} termos Exibidos')