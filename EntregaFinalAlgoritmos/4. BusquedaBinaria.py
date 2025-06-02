# Busqueda Binaria para encontrar un elemento en una lista ordenada
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Ejemplo
lista_ordenada = [1, 3, 5, 7, 9, 12, 15]
indice = busqueda_binaria(lista_ordenada, 9)
print("Índice del número buscado:", indice)
