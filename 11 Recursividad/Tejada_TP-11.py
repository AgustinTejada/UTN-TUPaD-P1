#Ejercicio 1
#Funciones
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num-1)

#Programa principal
numero = int(input('Ingrese un numero: '))

for i in range(1, numero + 1):
    print(f'{i}! = {factorial(i)}')


#Ejercicio 2
#Funciones
def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1) + fibonacci_recursivo(posicion-2)

#Programa principal
numero = int(input('Ingrese un numero: '))

for i in range(numero + 1):
    print(f'La posicion {i} de fibonacci es igual a {fibonacci_recursivo(i)}')


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


#Ejercicio 5
#Funciones
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
    
#Programa principal
palabra = input('Ingrese una palabra sin espacios ni tildes: ')
if es_palindromo(palabra):
    print('La palabra es palíndroma')
else:    
    print('La palabra NO es palíndroma')


#Ejercicio 6
#Funciones
def suma_digitos(numero):
    if numero < 10:
        return numero
    return (numero % 10) + suma_digitos(numero // 10)
    
#Programa principal
numero = int(input('Ingrese un numero entero positivo: '))
print(f'La suma de los digitos es: {suma_digitos(numero)}')


#Ejercicio 7
#Funciones
def contar_bloques(numero):
    if numero == 1:
        return 1
    return numero + contar_bloques(numero - 1)
    
#Programa principal
numero = int(input('Ingrese un numero entero positivo: '))
print(f'El total de bloques que necesita para construir la pirámide es: {contar_bloques(numero)}')


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
