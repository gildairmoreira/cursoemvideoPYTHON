#CALCULA AUMENTO SALARIAL
sal = float(input('Qual o seu salário? R$'))
if sal< 1250.00:
    print(f'Seu salário é {sal}\033[0;30;41m é com 15% de aumento irá para {sal+(sal*15/100)}')
else:
    print(f'Seu salário é {sal} é com 10% de aumento irá para {sal+(sal*10/100)}')
