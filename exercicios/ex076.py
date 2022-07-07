lista = ('lapis', 1.75,
         'borracha', 2,
         'caderno', 15.90,
         'Estojo', 25,
         'Trasnferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'canetas', 22.30,
         'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>4.2f}')
print('-'*40)
