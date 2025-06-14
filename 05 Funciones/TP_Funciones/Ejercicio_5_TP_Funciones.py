# Funciones
def segundos_a_horas(segundos):
    return segundos / 3600

def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n


# Programa Principal
segundos = leer_entero_validado('Ingrese los segundos', 0)
print(f'Los {segundos} segundos equivalen a {segundos_a_horas(segundos)} horas')
