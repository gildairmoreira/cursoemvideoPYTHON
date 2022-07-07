#ALUNO REPROVADO, APROVADO OU RECUPERAÇAO
nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))
media = (nota1+nota2)/2
if media < 5.0:
    print(f'Você foi \033[4;31mREPROVADO\033[m, sua nota foi abaixo da media de 5.0')
elif 5 <= media <=6.9:
    print(f'Sua media foi de {media} é você está de \033[4;33mRECUPERAÇÂO\033[m')
elif media >=7.0:
    print(f'Você foi \033[4;32mAPROVADO\033[m sua media foi de {media}')
