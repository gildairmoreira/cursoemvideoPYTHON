# pergunta qual o seu sexo e se for invalido pergunta dnv
flag = (str('sair'))
while flag == 'sair':
    sexo = str(input('Qual o seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            sexo = 'MASCULINO'
        else:
            sexo = 'Feminino'
        print(f'sexo {sexo} registrado com Sucesso')
        flag = 'ficar'
    else:
        print('Digite uma opçao valida')
        flag = 'sair'

#CORREÇAO

#sexo = str(input(informe seu sexo: [M / F])).strip().upper()[0]
#while sexo not in 'mMFf':
#    sexo = str(input('Dados invalidos, tente novamente:')).strip().upper()[0]
#print(f'Sexo {sexo} registrado com sucesso')
