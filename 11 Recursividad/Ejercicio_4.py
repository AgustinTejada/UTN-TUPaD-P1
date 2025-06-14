#Ejercicio 4
#Funciones
def decimal_a_binario(num):
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    if num % 2 == 0:
        return f'{decimal_a_binario(num // 2)}0' 
    else:
        return f'{decimal_a_binario(num // 2)}1'
    

#Programa principal
numero = int(input('Ingrese un numero entero positivo en base decimal: '))
print(f'El numero {numero} en binario es: {decimal_a_binario(numero)}')
