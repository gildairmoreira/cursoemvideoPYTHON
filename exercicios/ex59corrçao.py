#CORREÇAO SO SAINDO DO PROGRAMA UMA VEZ
n1 = int(input('Digite o Primeiro Valor: '))
n2 = int(input('Digite o segundo Valor: '))
opçao = 0
maior = menor = 0
while opçao != 5:
    print('''\n  MENU
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR NUMERO
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opçao = int(input('>>>Qual sua opção: '))
    if opçao == 1:
        print(f'A soma entre {n1} é {n2} e igual á {n1 + n2}')
    elif opçao == 2:
        print(f'A multiplicação de {n1} com {n2} é igual á {n1 * n2}')
    elif opçao == 3:
        if n1 >n2:
            maior = n1
            menor = n2
            print(f'Dos numeros digitados o Maior é {maior} é o menor e {menor}')
        elif n2 > n1:
            maior = n2
            menor = n1
            print(f'Dos numeros digitados o Maior é {maior} é o menor e {menor}')
        else:
            print('Os dois numeros são iguais')
    elif opçao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.Tente novamente')
    print('=-='*10)
print('Fim do Programa.Volte Sempre!')
