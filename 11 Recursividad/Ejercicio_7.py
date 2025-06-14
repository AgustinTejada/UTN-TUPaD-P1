#Ejercicio 7
#Funciones
def contar_bloques(numero):
    if numero == 1:
        return 1
    return numero + contar_bloques(numero - 1)
    
#Programa principal
numero = int(input('Ingrese un numero entero positivo: '))
print(f'El total de bloques que necesita para construir la pirámide es: {contar_bloques(numero)}')
