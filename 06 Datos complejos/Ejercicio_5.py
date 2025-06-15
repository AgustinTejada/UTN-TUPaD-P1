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