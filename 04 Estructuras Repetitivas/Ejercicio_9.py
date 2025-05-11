#Ejercicio 9
NUMEROS_A_INGRESAR = 100
suma = 0

print(f"Ingresa {NUMEROS_A_INGRESAR} números enteros:")

for i in range(NUMEROS_A_INGRESAR):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / NUMEROS_A_INGRESAR

print(f"La media de los numeros ingresados es: {media}")
