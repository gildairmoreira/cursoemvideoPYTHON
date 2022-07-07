#LER VARIOS NUMEROS
num = int(input('Digite um numero [999 para parar]: '))
soma = 0
soma += num
cont = 1
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print(f'Você digitou {cont} é a soma deles é igual á {soma}')
