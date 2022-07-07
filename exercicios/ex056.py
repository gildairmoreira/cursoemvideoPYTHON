#olha a idade media o homem mais velho e mina menos 20 anos de um grupo
idademedia = 0
maioridademacho = 0
nomevelho = ''
novinha = 0
for p in range(1,5):
    print(f'===== {p}ª PESSOA =====')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    idademedia =idade+idademedia
    sexo = str(input('Sexo [M/F]: ')).strip()
    if p == 1 and sexo in 'Mm':
        maioridademacho=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maioridademacho:
        maioridademacho=idade
        nomevelho=nome
    if sexo in 'Ff' and idade < 20:
        novinha += 1
print(f'A idade media do grupo é de {idademedia/4} anos')
print(f'O homem mais Velho tem {maioridademacho} anos e Se chama {nomevelho}')
print(f'São {novinha} mulheres com menos de 20 anos')
