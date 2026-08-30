import msvcrt  # Librería estándar de Windows para detectar teclas sin presionar Enter
import random
import time 

print('''
╔══════════════════════════════════════╗
║     👾 A R C A D E  M A S H E R 👾   ║
╚══════════════════════════════════════╝
''')
while True:
        duracion_segundos = 10
        tiempo_limite = time.time() + duracion_segundos

        numero = random.randint(1, 20)
        print(f"🎯 OBJETIVO: [ {numero} ] pulsaciones en {duracion_segundos}s.")
        print("⏳ ¡PREPÁRATE! Presiona '1' a máxima velocidad...")
        salida = msvcrt.getwch()

        respuesta = 0

        while time.time() < tiempo_limite:
            # Lee la tecla presionada al instante (sin esperar Enter)
            tecla = msvcrt.getwch()
            
            if time.time() >= tiempo_limite:
                break
                
            if tecla == "1":
                respuesta += 1
                print(f"\r🔥 COMBO: [ {respuesta} / {numero} ]", end="", flush=True)
                
            if respuesta == numero:
                print("\n\n🎉 ¡NIVEL SUPERADO! ERES UNA MÁQUINA 🎉\n")
                break

        if respuesta < numero and time.time() >= tiempo_limite:
                print("\n\n💀 GAME OVER. EL TIEMPO TE HA VENCIDO 💀\n")
        opcion = int(input("""
========================================
  [1] INSERT COIN (Jugar de nuevo)
  [2] EXIT (Rendirse)
========================================
▶ INGRESA TU OPCIÓN: """))

        if opcion == 1:
                continue
        elif opcion == 2:
                print("GAME OVER")
                break
