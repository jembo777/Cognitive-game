import msvcrt  # Librería estándar de Windows para detectar teclas sin presionar Enter
import random
import time 

print('''
====================
PRUEBA PARA EL JUEGO
====================''')

duracion_segundos = 10
tiempo_limite = time.time() + duracion_segundos

numero = random.randint(1, 20)
print(f"meta: {numero}")
print("Presiona la tecla 1 tantas veces como puedas...")

respuesta = 0

while time.time() < tiempo_limite:
    # Lee la tecla presionada al instante (sin esperar Enter)
    tecla = msvcrt.getwch()
    
    if time.time() >= tiempo_limite:
        break
        
    if tecla == "1":
        respuesta += 1
        print(f"Llevas: {respuesta}")
        
    if respuesta == numero:
        print("correcto")
        break

if respuesta < numero and time.time() >= tiempo_limite:
    print("nimodo pa q tardas ya perdistes")
