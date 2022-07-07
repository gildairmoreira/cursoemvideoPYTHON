total = maismil = maisbarato = cont = 0
nomebarato = ''
print('--'*20)
print('             SUPER STORE')
print('--'*20)
while True:
    produto = str(input('Qual produto? '))
    preço = float(input('Qual o Preço : '))
    total += preço
    cont += 1
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        nomebarato = produto
#    else:
#        if preço < maisbarato:
#            maisbarato = preço
#            nomebarato = produto
    if preço >= 1000:
        maismil += 1
    continuar = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('0pçao invalida, Tente novamente')
        continuar = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi R${total}')
print(f'Temos {maismil} Produtos Custando mais de R$1000.00 ')
print(f'O Produto mais Barato foi {nomebarato.title()} que custa R${maisbarato}')