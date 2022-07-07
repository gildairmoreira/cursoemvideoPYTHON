#CONVERSÃO PARA BASES NUMERICAS
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a Conversão: 
[ 1 ] Para Converter Para BINÁRIO
[ 2 ] Para Converter Para OCTAL
[ 3 ] Para Converter Para HEXADECIMAL''')
opçao = int(input('Sua opçao: '))
if opçao == 1:
    print(f'{num} convertido para BINÁRIO é igual á:{bin(num)[2:]}')
elif opçao == 2:
    print(f'{num} convertido para OCTAL é igual á:{oct(num)[2:]}')
elif opçao == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Digite uma opção valida.Tente novamente')