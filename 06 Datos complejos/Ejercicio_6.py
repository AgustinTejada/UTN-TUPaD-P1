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