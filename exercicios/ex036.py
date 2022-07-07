#FINANCIAMETO DE UMA CASA
casa = float(input('Qual e o valor da casa?'))
salario = float(input('Quanto você ganha por mes?'))
anos = int(input('Quantos anos para pagar?'))
prestaçao = casa/(anos*12)
minimo = salario*30/100
print(f'Para comprar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestaçao:.2f} por mês')
if prestaçao <= minimo:
    print(f'seu emprestimo foi APROVADO')
else:
    print(f'Seu emprestimo imobiliario foi NEGADO ')