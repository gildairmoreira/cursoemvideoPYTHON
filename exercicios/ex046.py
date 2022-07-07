#Contagem regresiva
from time import sleep
import emoji

for c in range(10 , 0 , -1):
    print(c)
    sleep(1)
print(emoji.emojize(":fireworks::fireworks::fireworks::fireworks:", language='alias'),'FELIZ ANO NOVO',emoji.emojize(":fireworks::fireworks::fireworks::fireworks:", language='alias'))
