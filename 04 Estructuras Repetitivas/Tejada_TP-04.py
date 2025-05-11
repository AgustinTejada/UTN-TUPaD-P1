#Agustín Tejada
#Ejercicios del TP. 4

#Ejercicio 1
for i in range(101):
    print(i)

#Ejercicio 2
numero = int(input("Ingrese un numero entero: "))

numeroAbs = abs(numero)
numeroStr = str(numeroAbs)

print("La cantidad de digitos del numero es: ", len(numeroStr))

#Ejercicio 3
numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese otro numero entero: "))

inicio = numero1 + 1
sumatoria = 0

for i in range(inicio, numero2):
    sumatoria += i 

print("La suma de los numeros enteros entre los numeros ingresados es: ", sumatoria)

#Ejercicio 4
sumatoria = 0
numero = int(input("Ingrese un numero entero: "))

while numero != 0:
    sumatoria += numero
    numero = int(input("Ingrese un numero entero: "))

print(f"La suma de los numeros ingresado es: {sumatoria}")

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

#Ejercicio 6 
for i in range(100, -1, -2):
    print(i)

#Ejercicio 7
numero = int(input("Ingrese un número entero positivo: "))
sumatoria = 0

if numero > 0:
    for i in range(0,numero+1):
        sumatoria += i
    print(f"La suma de todos los números comprendidos entre 0 y el número ingresado es: {sumatoria}")
else: 
    print("Numero ingresado no valido")

#Ejercicio 8
NUMEROS_A_INGRESAR = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingresa {NUMEROS_A_INGRESAR} números enteros:")

for i in range(NUMEROS_A_INGRESAR):
    numero = int(input("Ingrese un número entero: "))
    #Validacion de par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    #Validacion de positivo o negativo
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"Cantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")
print(f"Cantidad de numeros positivos: {positivos}")
print(f"Cantidad de numeros negativos: {negativos}")

#Ejercicio 9
NUMEROS_A_INGRESAR = 100
suma = 0

print(f"Ingresa {NUMEROS_A_INGRESAR} números enteros:")

for i in range(NUMEROS_A_INGRESAR):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / NUMEROS_A_INGRESAR

print(f"La media de los numeros ingresados es: {media}")

#Ejercicio 10
numero = int(input("Ingrese un número entero: "))
numero_absoluto = abs(numero)

# Inicializar la variable para almacenar el número invertido
numero_invertido = 0

while numero_absoluto > 0:
    digito = numero_absoluto % 10  # Obtener el último dígito
    numero_invertido = numero_invertido * 10 + digito  # Agregar el dígito al número invertido
    numero_absoluto //= 10  # Eliminar el último dígito del número

# Si el número original era negativo, hacer que el número invertido también sea negativo
if numero < 0:
    numero_invertido = -numero_invertido

# Mostrar el número invertido
print(f"El número invertido es: {numero_invertido}")