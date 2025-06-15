#Ejercicio 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

paises_capitales_invertido = {}

for pais, capital in paises_capitales.items():
    paises_capitales_invertido[capital] = pais

print(paises_capitales_invertido)