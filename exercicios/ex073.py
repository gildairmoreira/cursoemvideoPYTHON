times = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Internacional',
         'Atlético-MG', 'Fluminense', 'Santos', 'São Paulo', 'Flamengo',
         'Botafogo', 'Avaí', 'Bragantino', 'Atlético-GO', 'Goiás', 'Ceará',
         'Coritiba', 'América-MG', 'Cuiabá', 'Juventude', 'Fortaleza')
print('='*40)

print('OS 5 PRIMEIROS DO BRASILEIRÃO 2022 SÃO:')
print(times[0:5])
print('='*40)
print('OS 4 LANTERNAS SÃO:')
print(times[-4:])
print('='*40)
print('OS TIMES EM ORDEM ALFABETICA FICA:')
print(sorted(times))
print('='*40)
print(f'O Time do Galo Está na possiçao {times.index("Atlético-MG")+1}ª')
