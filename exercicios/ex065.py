#CONTA NUMEROS PERGUNTANDO SE QUER CONTINUAR E MOSTRA A MEDIA MAIOR E MENOR
from time import sleep
cont = somar = maior = menor = 0
resp = 'S'
while resp in 'S':
    n = int(input('Digite um numeros: '))
    somar += n
    cont += 1
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [S/ N]:')).strip().upper()[0]
    if resp == 'N':
        media = somar / cont
        print(f'Finalizando...')
        resp = 'n'
        sleep(1.5)
    elif resp != 'S':
        print('Opção invalida. Tente novamente')
        resp = 'S'
print(f'A media dos numeros que Você digitou foi {media} ')
print(f'O maior Valor foi {maior} é o menor foi {menor}')
