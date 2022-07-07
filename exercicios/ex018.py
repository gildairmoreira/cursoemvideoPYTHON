import math
ang = float(input('Digite o Ângulo que você deseja:'))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print(f'O seu angulo é {ang},\n SENO é {seno:.2f}\n COSSENO é {cosseno:.2f}\n TANGENTE é {tangente:.2f}')