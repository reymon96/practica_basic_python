#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(listaA, listaB):
    find = False
    for elementoA in listaA:
        for elementoB in listaB:
            if(elementoA == elementoB):
                find = True
        
    return find

listaA = [1, 2, 3, 4, "e","r",'y','a', "a", 3, "t", 6]
listaB = [3,"z", 5, 0, "1", "s", "v", 5, 7, 7, 8, 9]
listaC = [10, -1, "b", "n", 'n', '123', 33, 90, 'r', "q", 'w', "t"]

print(superposicion(listaA, listaB))
print(superposicion(listaB, listaC))
print(superposicion(listaA, listaC))