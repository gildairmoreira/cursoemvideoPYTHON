#PARCELAMENTO DO PRODUTO COM JUROS
print(f'{("=")*20} CAMELÔ DO GIL {"="*20}')
produto = float(input('Qual o valor do Produto? '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista no Dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
paga = int(input('Escolha a forma de pagamento: '))
if paga == 1:
    print(f'Você terá 10% de desconto em sua compra o valor irá para {produto-(produto*(10/100))}R$')
elif paga == 2:
    print(f'Você terá 5% de desconto em sua compra o valor irá para {produto-(produto*(5/100))}R$')
elif paga == 3:
    print(f'Você não terá nenhum desconto em sua compra o valor será de {produto}')
elif paga == 4:
    vezes = int(input('Quantas vezes no cartão? '))
    print(f'Se você escolheu {vezes}x no cartão pagará 20% de juros o valor irá para {produto+(produto*(20/100))}')
    print(f'Você pagará R${(produto+(produto*(20/100))) / vezes:.2f} Por mês')
else:
    print('\033[4;31mOpção invalida,Tente novamente')