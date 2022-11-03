#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(palabra):
    array, reversed = [], []
    for letra in palabra:
        array.append(letra)
        reversed.append(letra)

    reversed.reverse()
    if(array == reversed):
        return True
    else:
        return False

print(es_palindromo(input('Ingrese una palabra: ')))