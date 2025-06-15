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

