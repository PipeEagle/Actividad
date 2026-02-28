numero = int(input("Ingrese un al que desea sumar sus digitos: "))
total = 0

def sumardig_for(numero: int) -> int:
	total = 0
	for digito in str(numero):
		total += int(digito)
	return total

def sumardig_while(numero: int) -> int:
    total = 0
    resultado = 0
    while total < len (str(numero)):
        resultado += int(str(numero)[total])
        total += 1
    return resultado

def sumardig_recursivo(numero: int, indice: int = 0) -> int:
    if indice >= len(str(numero)):
        return 0
    else:
        digito = int(str(numero)[indice])
        return digito + sumardig_recursivo(numero, indice + 1)

print("Suma de dígitos (for):", sumardig_for(numero), "(while):", sumardig_while(numero), "(recursivo):", sumardig_recursivo(numero))