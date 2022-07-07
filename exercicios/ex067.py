while True:
    print('-'*40)
    num = int(input('Quer Ver a tabuada de qual numero: '))
    print('-'*40)
    if num > -1:
        for c in range(1,11):
            print(f'{num} x {c} = {num*c}')
    else:
        break
print('ACABOU')