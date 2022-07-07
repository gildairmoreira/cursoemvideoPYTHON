#ANALISA SE O NOME DA CIDADE TEM SANTO
cid = str(input('Qual o nome da sua cidade? ')).strip().lower()
santo = cid.find('santo')
tem = 'santo' in cid
print(f'Sua cidade tem santo no nome? {tem}')
