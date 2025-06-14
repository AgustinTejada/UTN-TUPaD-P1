# Funciones
def operaciones_basicas(a, b):
    suma = f'{a} + {b} = {a + b}'
    resta = f'{a} - {b} = {a - b}'
    multiplicacion = f'{a} x {b} = {a * b}'
    division = f'{a} / {b} = {a / b}'
    return (suma, resta, multiplicacion, division)

def leer_entero_validado(mensaje, min = float('-Inf'), max = float('Inf')):
    n = int(input(f'{mensaje}: '))
    while n < min or n > max:
        n = int(input(f'ERROR. {mensaje}: '))
    return n

# Programa Principal
a = leer_entero_validado('Ingrese el numero a')
b = leer_entero_validado('Ingrese el numero b')

print(f'{operaciones_basicas(a,b)}')