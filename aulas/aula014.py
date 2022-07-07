'''for c in range(1, 10):
    print(c)
print('fim')'''
#ex:1
'''c = 1
while c < 10: #enquanto o contador for menor que 10
    print(c)
    c += 1
print('fim')'''
#ex=2
#vendo se e par ou impar no while
n = 1
par = impar = 0 #variavel par e impar recebe zero
while n != 0:
        n = int(input('Digite um numero: '))
        if n != 0: #serve pra não usar o flag de saida na operaçao
            if n % 2 == 0:
                par += 1
            else:
                impar += 1
print(f'TEM {impar} NUMEROS IMPARES E {par} NUMEROS PARES')
