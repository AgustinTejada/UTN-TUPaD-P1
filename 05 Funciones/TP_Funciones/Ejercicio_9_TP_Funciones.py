# Funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32 
    return fahrenheit

def leer_num_validado(mensaje, min = float('-Inf'), max = float('Inf')):
    n = float(input(f'{mensaje}: '))
    while n < min or n > max:
        n = float(input(f'ERROR. {mensaje}: '))
    return n

# Programa Principal
celsius = leer_num_validado('Ingrese los grados en celsius')
print(f'Los grados ingreados equivalen a {celsius_a_fahrenheit(celsius)} grados Fahrenheit')
