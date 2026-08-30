
import random
import time 
print('''
====================
PRUEBA PARA EL JUEGO
====================''')

print("Hola Mundo")

duracion_segundos = 10
tiempo_limite = time.time() + duracion_segundos

numero = random.randint(1, 20)
print(f"meta: {numero}")

respuesta = 0

while time.time() < tiempo_limite:
        num = int(input(":"))
        if time.time() >= tiempo_limite:
            break
        if num == 1:
                respuesta += 1
        if respuesta == numero:
            print("correcto")
            break
if respuesta < numero and time.time() >= tiempo_limite:
            print("nimodo pa q tardas ya perdistes")


