#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(array):
    suma = 0
    for num in array:
        suma+=num
    return suma

def multip(array):
    multi = 0
    for i in range(0, len(array) - 1):
        array[i + 1] = array[i] * array[i + 1]
        multi = array[i + 1]
    return multi

lista = [[1,2,3,4], [4,3,2,1], [3,2,4,6,1,4,6], [5,2], [8,4,1,9,2]]

for casilla in lista:
    print(f'suma: {sum(casilla)}, Multiplicación: {multip(casilla)}')