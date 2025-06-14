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
