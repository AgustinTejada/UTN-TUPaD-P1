
#Ejercicio 8 
#Funciones
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        coincidencia = 1 if numero % 10 == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)
    
#Programa principal
numero = int(input('Ingrese un numero entero positivo: '))
digito = int(input('Ingrese un dígito (entre 0 y 9): '))
print(f'El dígito aparece: {contar_digito(numero, digito)} veces')
