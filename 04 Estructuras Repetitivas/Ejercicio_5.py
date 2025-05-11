#Ejercicio 5
import random

numeroRandom = random.randint(0,9)
intentos = 0
acierto = False

print("Adivina el numero aleatorio entre 0 y 9")

while not acierto:
    intentos += 1
    numero = int(input("Ingrese el número: "))
    if numero == numeroRandom:
        acierto = True

print(f"Adivinó el número en: {intentos}")