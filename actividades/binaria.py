#https://youtu.be/6-e_kVZkECI?si=r4YswUFvp3SENpRy

lista = [0, 88, 72,21,14,16,90,35,47,68, 100, 45, 23, 12, 9, 55, 78, 34, 67, 89]
lista.sort()
print("Lista ordenada:", lista)
print(len(lista), "datos en la lista")

#1buscar punto medio (puntero)
#2comparar el valor del punto medio con el valor a buscar
#3 el numero es menor al valor que buscamos aumentamos inicio 1 sobre el puntero
#4 el numero es mayor al valor que buscamos disminuimos fin 1 debajo del puntero
#5 si inicio se vuelve mayor o igual que fin entonces el valor no se encuentra en la lista

def busqueda_binaria(valor):
    inicio = 0 
    fin= len(lista) - 1 
    while inicio <= fin:
     puntero = (inicio + fin) // 2
     if valor == lista[puntero]:
         return puntero
     elif valor > lista[puntero]:   
         inicio = puntero + 1
     else:
        fin = puntero - 1
    return None

def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f"El valor {valor} no se encuentra en la lista."
    else:
        return f"El valor {valor} se encuentra en la posición {res_busqueda}."
    
print(buscar_valor(int(input("Ingrese el valor a buscar: "))))