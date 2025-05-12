# Agustín Tejada
# Ejercicios corresponidente al TP 5 Listas

#Ejercicio 1
lista_multiplos_4 = list(range(4,101,4))
print(f"La lista de 0 a 100 con los multiplos de 4 es: {lista_multiplos_4}")

#Ejercicio 2
lista = ["HTML", "CSS", "JS", "JAVA", "PYTHON"]
penultimo_elemento = lista[-2]

print(f"La lista de elemento es: {lista}")
print(f"El penultimo elemnto es: {penultimo_elemento}")

#Ejercicio 3
lista_vacia = []
lista_vacia.append("elemento1")
lista_vacia.append("elemento2")
lista_vacia.append("elemento3")

print(f"Lista con 3 elementos agregados: {lista_vacia}")

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
print(f"Lista animales: {animales}")

animales[1] = "loro"
animales[-1] = "oso"
print(f"Lista animales modificada: {animales}")

#Ejercicio 5
#Explicación de cada línea del codigo
numeros = [8, 15, 3, 22, 7] # Se crea una lista llamada numeros que contiene 5 números
numeros.remove(max(numeros)) # Se obtiene el número mas grande de la lista numeros y se elimina de la lista
print(numeros) # Se imprime la lista numeros [8, 15, 3, 7]

#Ejercicio 6
lista = list(range(10, 31, 5))
print(f"Lista: {lista}")
print("Los dos primeros elementos de la lista son:", (lista[:2]))

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["clio", "golf"]

print(f"Lista de autos modificada es: {autos}")

#Ejercicio 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(f"Lista de dobles: {dobles}")

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

#Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

#Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

#Imprimir la lista resultante por pantalla
print(compras)

#Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)