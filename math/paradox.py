import math
import random

def play() :
    num_jugadas = 0
    num_max_jugadas = 10
    play = True

    while ((num_jugadas < num_max_jugadas) & play) :
        if random.uniform(0, 1) >0.5 :
            play = False
        num_jugadas=num_jugadas+1

    beneficio = 2**num_jugadas
    return (beneficio, num_jugadas)


b = 0
l = 1000
for i in range(l) :
    beneficio, num_jugadas = play()
    b = b+beneficio
    print('Beneficio - Número de jugadas', beneficio, num_jugadas)

print('media', b/l)