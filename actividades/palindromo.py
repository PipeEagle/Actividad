#https://youtu.be/9JzD1dGOMg4?si=6UZg-dGpv0DrIB4b

palabra = input("Ingrese una palabra: ")

def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")
    
    # n = largo de la frase - 1
    
    a = 0
    b = len(palabra) - 1

    for i in range(0,len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else: 
            return False
      
    return True

print("La palabra es un palíndromo:", es_palindromo(palabra))

if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")

