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