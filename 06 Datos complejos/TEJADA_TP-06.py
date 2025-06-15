#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


#Ejercicio 2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#Actualizacion de precios
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)


#Ejercicio 3
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#Actualizacion de precios
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

list_solo_frutas = precios_frutas.keys()
print(f'Lista de solo frutas {list_solo_frutas}')


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


#Ejercicio 5
frase = input('Ingrese una frase: ')
palabras = frase.split()
palabras_unicas = set(palabras)
print(f'Palabras únicas: {palabras_unicas}')

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Recuento:", recuento)


#Ejercicio 6
alumnos = {}

for i in range(1,4):
    nombre = input("Ingresá el nombre del alumno: ")
    notas = []
    for j in range(1,4):
        nota = int(input(f"Ingresá la nota {j} del alumno {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} tiene un promedio de {promedio:.2f}")


#Ejercicio 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2         # Intersección
solo_uno = parcial1 ^ parcial2      # Diferencia simetrica
al_menos_uno = parcial1 | parcial2  # Union

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)


#Ejercicio 8
productos = {
    "manzanas": 10,
    "bananas": 5,
    "naranjas": 8
}

producto = input("Ingresá el nombre del producto: ")

if producto in productos:
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {productos[producto]}")
else:
    nuevo_stock = int(input("Producto nuevo. Ingresá el stock inicial: "))
    productos[producto] = nuevo_stock
    print(f"Producto {producto} agregado con {nuevo_stock} unidades.")


#Ejercicio 9
agenda = {
    ("Lunes", "10:00"): "Reunion",
    ("Martes", "15:00"): "Clase de ingles",
}

dia = input("Ingrese el día que quiere consultar: ")
hora = input("Ingrese la hora que quiere consultar: ")
tupla_key = (dia, hora)
if tupla_key in agenda:
    print(f"El evento es: {agenda[tupla_key]}")
else:
    print("No hay eventos")


#Ejercicio 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

paises_capitales_invertido = {}

for pais, capital in paises_capitales.items():
    paises_capitales_invertido[capital] = pais

print(paises_capitales_invertido)