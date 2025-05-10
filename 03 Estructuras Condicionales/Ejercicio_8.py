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