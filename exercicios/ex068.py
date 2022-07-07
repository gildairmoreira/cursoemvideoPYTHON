from random import randint
vitorias = soma = 0
while True:
    print('-='*20)
    print('       Vamos jogar PAR ou IMPAR')
    print('-='*20)
    computador = randint(0, 10)
    jogador = int(input('Diga um Valor: '))
    esc = str(input('PAR ou IMPAR [P / I]: ')).strip().upper()[0]
    while esc not in 'PI':
        esc = str(input('PAR ou IMPAR [P / I]: ')).strip().upper()[0]
    soma = computador + jogador
    if soma % 2 == 0:
        if esc == 'I':
            print(f'Você jogou {jogador} é o computador {computador}. Total de {soma} DEU PAR')
            break
        if esc == 'P':
            print(f'Você jogou {jogador} é o computador {computador}. Total de {soma} DEU PAR')
            print('Você VENCEU!\nVamos Jogar Novamente...')
            vitorias += 1
    else:
        if esc == 'I':
            print(f'Você jogou {jogador} é o computador {computador}. Total de {soma} DEU IMPAR')
            print('Você VENCEU!\nVamos Jogar Novamente...')
            vitorias += 1
        if esc == 'P':
            print(f'Você jogou {jogador} é o computador {computador}. Total de {soma} DEU IMPAR')
            break
print('Você PERDEU!')
print(f'GAME OVER! Você venceu {vitorias} Vezes')