#Ejercicio 10
numero = int(input("Ingrese un número entero: "))
numero_absoluto = abs(numero)

# Inicializar la variable para almacenar el número invertido
numero_invertido = 0

while numero_absoluto > 0:
    digito = numero_absoluto % 10  # Obtener el último dígito
    numero_invertido = numero_invertido * 10 + digito  # Agregar el dígito al número invertido
    numero_absoluto //= 10  # Eliminar el último dígito del número

# Si el número original era negativo, hacer que el número invertido también sea negativo
if numero < 0:
    numero_invertido = -numero_invertido

# Mostrar el número invertido
print(f"El número invertido es: {numero_invertido}")