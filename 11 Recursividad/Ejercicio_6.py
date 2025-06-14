#Ejercicio 6
#Funciones
def suma_digitos(numero):
    if numero < 10:
        return numero
    return (numero % 10) + suma_digitos(numero // 10)
    
#Programa principal
numero = int(input('Ingrese un numero entero positivo: '))
print(f'La suma de los digitos es: {suma_digitos(numero)}')
