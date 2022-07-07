#MENU PARA NUMEROS MATEMATICOS
flag = 'sair'
maior = menor = 0
while flag == 'sair':
    n1 = int(input('Digite o 1ª numero: '))
    n2 = int(input('Digite o 2ª numero: '))
    print('''=== MENU DE INTERRAÇÃO ===
    DIGITE:
    [ 1 ] Para Somar
    [ 2 ] Para Multiplicar
    [ 3 ] Para saber o Maior
    [ 4 ] Para Digitar outros numeros
    [ 5 ] Para sair do programa''')

    opçao = int(input('Escolha uma opção: '))
    if opçao == 1:
        print(f'Você escolheu somar: {n1} + {n2} = {n1+n2}')
        sair1 = str(input('Deseja tentar novamente [S / N]: ')).strip().upper()
        if sair1 == 'S':
            flag = 'sair'
        elif sair1 == 'N':
            print('Você saiu do programa')
            flag = 'ficar'
        else:
            print('Opção invalida')
            flag='ficar'
    elif opçao == 2:
        print(f'Você escolheu multiplicar: {n1}x{n2}={n1*n2}')
        sair1 = str(input('Deseja tentar novamente [S / N]: ')).strip().upper()
        if sair1 =='S':
            flag = 'sair'
        elif sair1 == 'N':
            print('Você saiu do programa')
            flag = 'ficar'
        else:
            print('Opação invalida')
            flag = 'ficar'
    elif opçao == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print(f'O numero {maior} é maior que o numero {menor}\n')
            sair1 = str(input('Deseja tentar novamente [S / N]: ')).strip().upper()
            if sair1 == 'S':
                flag = 'sair'
            elif sair1 == 'N':
                print('Você saiu do programa')
                flag = 'ficar'
            else:
                print('Opação invalida')
                flag = 'ficar'
        elif n2 > n1:
            maior = n2
            menor = n1
            print(f'O numero {maior} é maior que o numero {menor}\n')
            sair1 = str(input('Deseja tentar novamente [S / N]: ')).strip().upper()
            if sair1 == 'S':
                flag = 'sair'
            elif sair1 == 'N':
                print('Você saiu do programa')
                flag = 'ficar'
            else:
                print('Opação invalida')
                flag = 'ficar'

        else:
            print(f'OS NUMEROS SÃO IGUAIS ({n1})')
    elif opçao == 4:
        flag == 'sair'
    elif opçao == 5:
        print('Você Saiu do programa...')
        flag = 'ficar'
    else:
        print('Opção invalida, Tente novamente')






