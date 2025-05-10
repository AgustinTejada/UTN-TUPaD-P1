contrasena = input("Ingrese su contraseña: ")
sizePass = len(contrasena)

if sizePass >= 8 and sizePass <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
