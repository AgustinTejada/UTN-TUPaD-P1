# Funciones
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    imc = round(imc, 2)
    return imc

def leer_num_validado(mensaje, min = float('-Inf'), max = float('Inf')):
    n = float(input(f'{mensaje}: '))
    while n < min or n > max:
        n = float(input(f'ERROR. {mensaje}: '))
    return n

# Programa Principal
peso = leer_num_validado('Ingrese su peso en kg', 1)
altura = leer_num_validado('Ingrese su altura en metros', 1)
print(f'El índice de masa corporal (IMC) es: {calcular_imc(peso, altura)}')
