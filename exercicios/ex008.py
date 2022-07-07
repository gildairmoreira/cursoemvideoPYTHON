medida = float(input('quantos metros?'))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(f'\033[4;31m{medida}\033[mm são\n \033[1;34;97m{mm}mm\n {cm}cm\n {dm}dm\n {dam}dam\n {hm}hm\n {km}km\n')