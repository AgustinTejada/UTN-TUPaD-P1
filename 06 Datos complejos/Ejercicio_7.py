#Ejercicio 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2         # Intersección
solo_uno = parcial1 ^ parcial2      # Diferencia simetrica
al_menos_uno = parcial1 | parcial2  # Union

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)