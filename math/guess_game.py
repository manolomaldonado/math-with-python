import random
# 1. Elegir un número aleaorio del 1 al 100
target = random.randint(1,100)
adivinado = False
count = 0
while not adivinado :
    count += 1
    # 2. Pedir al jugador que introduzca un número
    num = int(input("Introduce un número " ))
    # 3. Comparar el numero del jugador con el aleatorio
    # 3.1 Si el numero del jugador es mayor avisar de que el numero que tiene que buscar es menor
    if num > target : 
        print("Menor")
    # 3.2 Si el numero del jugador es menor avisar de que el numero que tiene que buscar es mayor
    elif num < target : 
        print("Mayor")
    # 3.3 Si el número es igual se acaba el juego
    else :
        adivinado = True
        print("Has acertado en " + str(count) + " pasos !!!!!")

# 4. Contamos los pasos