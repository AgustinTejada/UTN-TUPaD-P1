#Funciones
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num-1)

#Programa principal
numero = int(input('Ingrese un numero: '))

for i in range(1, numero + 1):
    print(f'{i}! = {factorial(i)}')
