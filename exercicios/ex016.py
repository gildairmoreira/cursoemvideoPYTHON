'''import math
num = float(input('Digite um numero:'))
print(f'o valor digitado e {num} numero inteiro é {math.floor(num)}')'''
from math import trunc
num = float(input('digite um valor:'))
print(f'O valor digitado é {num} e a parte inteira é {trunc(num)}')