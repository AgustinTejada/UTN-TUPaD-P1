# Funciones
def tabla_multiplicar(numero):
    for i in range(1,11):
       print(f'{numero} x {i} = {numero * i}')

def leer_entero_validado(mensaje, min = float('-Inf'), max = float('Inf')):
    n = int(input(f'{mensaje}: '))
    while n < min or n > max:
        n = int(input(f'ERROR. {mensaje}: '))
    return n

# Programa Principal
numero = leer_entero_validado('Ingrese un numero')
tabla_multiplicar(numero)