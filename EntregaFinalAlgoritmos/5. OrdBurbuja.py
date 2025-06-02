def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista
# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)
numeros_ordenados = ordenamiento_burbuja(numeros)
print("Lista ordenada:", numeros_ordenados)