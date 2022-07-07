num = [2, 5, 9, 1]
num[2] = 3  #Muda a 'casa' numero 2 (9) para 3
num.append(7)  #Adiciona 7 em uma nova 'CASA'
num.sort()  #deixa em ordem (CRESCENTE)
num.sort(reverse=True)  #deixa em ordem decrescente
num.insert(2, 0)  #Na posiçao 2 eu quero colocar 0
num.pop()   #Remove o ultimo numero da lista (Se eu colocar um num ele remove a 'casa'
if 5 in num:   #se eu mandar remover um numero que não existe na lista DA ERRO
    num.remove(5) #Remove o numero e não a casa e so faz para o primeiro elemento encontrado
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} Elementos')

valores = []


#SERVE PARA COLOCAR EM ORDEM
for v in valores:
    print(f'{v}...', end='')

#PARA COLOCAR VALORES DENTRO DE UMA LISTA USANDO REPETIÇAO
for con in range(0, 5):
    valores.append(int(input('Digite um valor: ')))


#SERVE PARA MOSTRAR O INDICE, MOSTRA A POSIÇAO E O QUE ESTA NA POSIÇÃO
for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}!')
print('Cheguei ao final da lista.')

#PROBLEMA DO PY
a = [2, 3, 4, 7]
b = a[:]  #SE COLOCAR B=A SE EU MANDAR MUTAR O B O A TBM VAI MUDAR PARA NÃO ACONTECER COLOCA A[:]
print(f'LISTA A:{a}')
print(f'Lista B:{b}')

#O COMANDO PARA ACHAR A POSIÇAO DE UM NUMERO ESPECIFICO NA LISTA
print(valores.index(max(valores)))  #ACHA A POSIÇAO DO MAIOR VALOR DE UMA LISTA
