n1 = int(input('digite um numero:'))
n2 = int(input('outro numero:'))
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
s = n1+n2
print('a soma vale \033[31m{}\033[m,o produto é \033[31m{}\033[m, e a divisão é \033[31m{:.3f}\033[m'.format(s,m,d), end=' ')
print('Divisão inteira {} e potência {}'.format(di,e,))
