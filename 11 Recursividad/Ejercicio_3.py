#Ejercicio 3
#Funciones
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente-1)

#Programa principal
base = int(input('Ingrese un numero base: '))
exponente = int(input('Ingrese un numero exponente: '))

print(f'{base}^{exponente}: {potencia(base, exponente)}')
