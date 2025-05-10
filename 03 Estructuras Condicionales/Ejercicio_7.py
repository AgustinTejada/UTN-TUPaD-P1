palabra = input("Ingrese una palabra o frase: ")
ultimoChar = palabra[-1]
terminaEnVocal = ultimoChar == "a" or ultimoChar == "A" or ultimoChar == "e" or ultimoChar == "E" or ultimoChar == "i" or ultimoChar == "I" or ultimoChar == "o" or ultimoChar == "O" or ultimoChar == "u" or ultimoChar == "U"

if terminaEnVocal:
    print(f"{palabra}!")
else:
    print(f"{palabra}")
