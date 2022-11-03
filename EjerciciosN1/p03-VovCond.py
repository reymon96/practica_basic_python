#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def caracter(letra):
    vocales = ["a","e","i","o","u"]
    if(letra in vocales):
        return True
    else:
        return False

print(caracter(input('Ingrese un caracter: ')))