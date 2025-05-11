#Ejercicio 7
numero = int(input("Ingrese un número entero positivo: "))
sumatoria = 0

if numero > 0:
    for i in range(0,numero+1):
        sumatoria += i
    print(f"La suma de todos los números comprendidos entre 0 y el número ingresado es: {sumatoria}")
else: 
    print("Numero ingresado no valido")
