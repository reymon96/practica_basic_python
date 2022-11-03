#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    arreglo, array = [], []
    for letra in cadena:
        arreglo.append(letra)
    
    x = len(arreglo)
    for i in range(0, len(arreglo)):
        array.append(arreglo[x - 1])
        x=x-1
    
    return array

print(inversa(input('Ingrese un texto: ')))