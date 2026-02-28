numeros = range(1, int(input("Ingrese un número: ")) + 1) 

def factorial_numeros_for(numeros: list) -> int:
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def factorial_numeros_while(numeros: list) -> int:
    i = 0
    resultado = 1
    while i < len(numeros):
        resultado *= numeros[i]
        i += 1
    return resultado

def factorial_numeros_recursivo(numeros: list) -> int:
    if not numeros:  
        return 1
    else:
        return numeros[0] * factorial_numeros_recursivo(numeros[1:]) 
    
print("recursivo",factorial_numeros_recursivo(numeros),"while",factorial_numeros_while(numeros),"for",factorial_numeros_for(numeros))  