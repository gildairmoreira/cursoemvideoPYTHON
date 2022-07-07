palavras = ('Aprender', 'python', 'Curso', 'Cachorro',
            'lena', 'paul', 'linguagem', 'ingles',
            'trabalhar', 'Programaçao', 'mercado', 'FUTURO')
for p in palavras:
    print(f'\nNa palavra {p.upper()} Temos As vogais: ', end='')
    for letra in p:  #PARA CADA LETRA NA (P)'PEQUENA' PALAVRA VER SE TEM AEIOU E PRINTAR AS LETRAS
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='')
