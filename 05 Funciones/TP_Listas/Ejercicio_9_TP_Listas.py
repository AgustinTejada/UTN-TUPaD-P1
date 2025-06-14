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