#Factorial de un número recursivo.
def factorial_r(n):
    if n <= 1:
        return 1
    return n * factorial_r(n - 1)

print(f"Factorial recursivo: {factorial_r(5)}")

# Factorial de un número iterativo.
def factorial_i(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print(f"Factorial iterativo: {factorial_i(5)}")
