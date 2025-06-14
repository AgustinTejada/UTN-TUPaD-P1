#Funciones
def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1) + fibonacci_recursivo(posicion-2)
#Programa principal
numero = int(input('Ingrese un numero: '))

for i in range(numero + 1):
    print(f'La posicion {i} de fibonacci es igual a {fibonacci_recursivo(i)}')
