# Algoritmo de Euclides Interativo
def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a

# Algoritmo de Euclides Recursivo
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
