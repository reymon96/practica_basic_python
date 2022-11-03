#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max(numA : float, numB : float, numC : float):
    array = [numA, numB, numC]
    array.sort()
    return array[2]

pruebas = [[3,2,1], [2,1,3], [5,3,4], [3,2,2], [2,1,2], [1,1,1], [3,3,2]]

for prueba in pruebas:
    print(max(prueba[0], prueba[1], prueba[2]))