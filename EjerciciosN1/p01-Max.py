#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(numA, numB):
    try:
        numA = float(numA)
        numB = float(numB)
        if(numA > numB):
            return (f'{numA} es el mayor!')
        elif (numA == numB):
            return (f'{numB} y {numA} son iguales!')
        else:
            return (f'{numB} es el mayor!')
    except:
        return ('Número invalido')
    
print(max(input('Ingrese el primer número: '), input('Ingrese el segundo número: ')))