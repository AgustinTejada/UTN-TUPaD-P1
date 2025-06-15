#Ejercicio 4
contactos = {}

for i in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("Ingresá el nombre del contacto a consultar: ")

if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print("Contacto no encontrado.")