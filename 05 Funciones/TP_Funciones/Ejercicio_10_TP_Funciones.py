# Funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return round(promedio, 2)

def leer_num_validado(mensaje, min = float('-Inf'), max = float('Inf')):
    n = float(input(f'{mensaje}: '))
    while n < min or n > max:
        n = float(input(f'ERROR. {mensaje}: '))
    return n

# Programa Principal
numero1 = leer_num_validado('Ingrese el numero 1')
numero2 = leer_num_validado('Ingrese el numero 2')
numero3 = leer_num_validado('Ingrese el numero 3')

print(f'El promedio de los 3 numeros ingresados es: {calcular_promedio(numero1, numero2, numero3)}')