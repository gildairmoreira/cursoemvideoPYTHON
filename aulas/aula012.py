nome = str(input('Qual o seu nome?')).lower()
if nome == 'gildair':
    print(f'Que nome Bonito Você tem !!')
elif nome in 'jessica mari jett':
    print('Belo nome feminino')
elif nome=='pedro' or nome=='paulo' or nome=='maria':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é Normal')
print(f'Tenha um bom dia,\033[4;35m{nome}\033[m !!!')
