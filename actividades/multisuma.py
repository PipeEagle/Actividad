a= int(input("Ingrese el primer numero multiplicar: "))
b = int(input("Ingrese el segundo numero multiplicar: "))

numeros = a, b

def multisuma_for(numeros: list) -> int:
    resultado = 0
    for i in range(numeros[0]):
        resultado += numeros[1]
    return resultado

def multisuma_while(numeros: list) -> int:
    resultado = 0
    i = 0
    while i < numeros[0]:
        resultado += numeros[1]
        i += 1
    return resultado

def multisuma_recursivo(numeros: list) -> int:
    if numeros[0] <= 0: 
        return 0
    else:
        return numeros[1] + multisuma_recursivo([numeros[0] - 1, numeros[1]])

print("for:", multisuma_for(numeros), "while:", multisuma_while(numeros), "recursivo:", multisuma_recursivo(numeros))