mais18 = homens = novinhas20 = 0
while True:
    print('-'*30)
    print('     Cadastre Uma Pessoa')
    print('-'*30)
    idade = int(input('Digite A idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M / F]: ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        novinhas20 += 1
    if continuar == 'N':
        break
print('======= FIM DO PROGRAMA =======')
print(f'Total de Pessoas com mais de 18 Anos: {mais18}')
print(f'Ao todo Temos {homens} Homens Cadastrados')
print(f'É Temos {novinhas20} mulheres com menos de 20 anos')
