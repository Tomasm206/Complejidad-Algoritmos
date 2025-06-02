# Serie de Fibonacci interativo.
def getFibo():
    yield 0
    a, b = 0, 1
    while True:
        yield b
        b = a + b
        a = b - a

fibo = getFibo()
print(type(fibo))
print("primer número", next(fibo))

for num in fibo:
    if num > 30000:
        break
    print("siguiente número", num)

# Serie de Fibonacci recursivo.
def fiboRecursivo(n):
    if n <= 1:
        return n
    return fiboRecursivo(n - 1) + fiboRecursivo(n - 2)

# Imprimir los primeros 20 números de la serie de Fibonacci recursiva.
for i in range(20):
    print(fiboRecursivo(i), end=" ")