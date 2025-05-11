#Ejercicio 4
sumatoria = 0
numero = int(input("Ingrese un numero entero: "))

while numero != 0:
    sumatoria += numero
    numero = int(input("Ingrese un numero entero: "))

print(f"La suma de los numeros ingresado es: {sumatoria}")