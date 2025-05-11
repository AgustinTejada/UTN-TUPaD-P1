#Ejercicio 3
numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese otro numero entero: "))

inicio = numero1 + 1
sumatoria = 0

for i in range(inicio, numero2):
    sumatoria += i 

print("La suma de los numeros enteros entre los numeros ingresados es: ", sumatoria)