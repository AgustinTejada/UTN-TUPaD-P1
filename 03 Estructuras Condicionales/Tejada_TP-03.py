#Agustín Tejada
#Ejercicios del T. P. 3

#Ejercicio 1
edad = int(input("Escriba su edad: "))
if edad > 18:
    print("Es mayor de edad.")

#Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
edad = int(input("Escriba su edad: "))
if edad < 12:
    print("Pertenece a la categoría Niño/a")
elif edad >= 12 and edad < 18:
    print("Pertenece a la categoría Adolescente")
elif edad >= 18 and edad < 30:
    print("Pertenece a la categoría Adulto/a joven")
else:
    print("Pertenece a la categoría Adulto/a")

#Ejercicio 5
contrasena = input("Ingrese su contraseña: ")
sizePass = len(contrasena)

if sizePass >= 8 and sizePass <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6
import random 
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)


if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")

#Ejercicio 7
palabra = input("Ingrese una palabra o frase: ")
ultimoChar = palabra[-1]
terminaEnVocal = ultimoChar == "a" or ultimoChar == "A" or ultimoChar == "e" or ultimoChar == "E" or ultimoChar == "i" or ultimoChar == "I" or ultimoChar == "o" or ultimoChar == "O" or ultimoChar == "u" or ultimoChar == "U"

if terminaEnVocal:
    print(f"{palabra}!")
else:
    print(f"{palabra}")

#Ejercicio 8
nombre = input("Escriba su numbre: ")

print("Opciones: ")
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
instruccion = int(input("Ingrese su opción: "))

if instruccion == 1:
    print(nombre.upper())
elif instruccion == 2:
    print(nombre.lower())
elif instruccion == 3:
    print(nombre.title())
else:
    print("Su opción es incorrecta")

#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

#Ejercicio 10
print("Ingrese en que hemisferio se encuntra: ")
print("N = Norte")
print("S = Sur")
hemisferio = input("(N/S): ")

mes = int(input("Ingrese que mes (1/12) del año es: "))
dia = int(input("Ingrese que dia (1/31) del año es: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion = "Otoño" if hemisferio == "N" else "Primavera"
else:
    estacion = "Fecha inválida"

print(f"La estación del año es: {estacion}")
