lista = []
maior = 0
menor = 0
for v in range(0, 5):
    lista.append(int(input(f'Digite um Valor na posição {v}: ')))
    if v ==0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]
print('-='*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, c in enumerate(lista):
    if c == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor Valor digitado foi {menor} nas posições ', end='')
for i, c in enumerate(lista):
    if c == menor:
        print(f'{i}... ', end='')
