# https://youtu.be/wNF56qbNU5E?si=rcGsHihhJ83MulZG

def hanoi(n, origen, destino, auxiliar):
    if n == 1:
       print(f"Mover disco 1 de {origen} a {destino}")
       return
    hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    hanoi(n - 1, auxiliar, destino, origen)
    
num_discos = int(input("Ingrese el número de discos: "))
hanoi(num_discos, 'A', 'C', 'B')
