#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******

def procedimiento(lista):
    for elemento in lista:
        print(elemento * "*")

lista = [5, 6, 2, 5, 5, 2, 1, 6, 10, 3]
procedimiento(lista)