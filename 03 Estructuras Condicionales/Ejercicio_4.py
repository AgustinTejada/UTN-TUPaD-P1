edad = int(input("Escriba su edad: "))
if edad < 12:
    print("Pertenece a la categoría Niño/a")
elif edad >= 12 and edad < 18:
    print("Pertenece a la categoría Adolescente")
elif edad >= 18 and edad < 30:
    print("Pertenece a la categoría Adulto/a joven")
else:
    print("Pertenece a la categoría Adulto/a")
