# Busqueda lineal para encontrar el mínimo en una lista
def encontrarMin(lista):
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo

# Ejemplo de uso
numeros = [5, 3, 8, 1, 4]
minimo = encontrarMin(numeros)
print(f"El número mínimo en la lista es: {minimo}")