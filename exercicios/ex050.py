#SOMA DE 5 NUMEROS Q SÃO PARES
soma = 0
cont = 0
for c in range (0,6):
    num =int(input('Digite um numero: '))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print(f'O valor da soma dos {cont} numeros pares são {soma}')