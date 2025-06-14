# Funciones
def calcular_area_circulo(radio):
    area = radio * radio * 3.14 
    print(f'El área del circulo es: {area}')

def calcular_perimetro_circulo(radio): 
    perimetro = radio * 2 * 3.14
    print(f'El área del perimetro es: {perimetro}')
    

def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

# Programa Principal
radio = leer_entero_validado("Ingrese el radio", 1)
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
