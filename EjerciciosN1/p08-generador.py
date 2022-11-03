#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5) debería devolver "xxxxx".
import random, string

def generar_n_caracteres(n : int):
    caracter = random.choices(string.ascii_letters)
    return n * caracter

print(generar_n_caracteres(5))