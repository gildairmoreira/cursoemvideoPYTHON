valores = []
for v in range(1, 6):
    valores.append(int(input(f'Digite o {v}ª numero: ')))
maior = max(valores)
menor = min(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior Valor Digitado foi {maior} na posiçao {valores.index(max(valores))}')
print(f'O menor Valor Digitado foi {menor} na posiçao {valores.index(min(valores))}')
