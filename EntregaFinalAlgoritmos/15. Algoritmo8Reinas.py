# Algoritmo Genético para resolver el problema de las 8 reinas
import random

N = 8
POP_SIZE = 100
MUTATION_RATE = 0.1
GENERATIONS = 1000

def crear_individuo():
    ind = list(range(N))
    random.shuffle(ind)
    return ind

def fitness(ind):
    # Número de pares de reinas en conflicto (menor es mejor)
    conflictos = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(ind[i] - ind[j]) == abs(i - j):
                conflictos += 1
    return conflictos

def seleccion(poblacion):
    # Torneo: elegir dos y quedarse con el mejor
    i1, i2 = random.sample(range(len(poblacion)), 2)
    return poblacion[i1] if fitness(poblacion[i1]) < fitness(poblacion[i2]) else poblacion[i2]

def crossover(p1, p2):
    # Crossover ordenado para permutaciones
    start, end = sorted(random.sample(range(N), 2))
    hijo = [None]*N
    hijo[start:end] = p1[start:end]

    pos = end
    for gen in p2:
        if gen not in hijo:
            if pos >= N:
                pos = 0
            hijo[pos] = gen
            pos += 1
    return hijo

def mutacion(ind):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(N), 2)
        ind[i], ind[j] = ind[j], ind[i]

def imprimir_tablero(sol):
    for fila in range(N):
        linea = ""
        for col in range(N):
            if sol[fila] == col:
                linea += "♛ "
            else:
                linea += ". "
        print(linea)
    print()

def algoritmo_genetico():
    poblacion = [crear_individuo() for _ in range(POP_SIZE)]

    for gen in range(GENERATIONS):
        poblacion.sort(key=fitness)
        if fitness(poblacion[0]) == 0:
            print(f"Solución encontrada en generación {gen}:")
            imprimir_tablero(poblacion[0])
            return poblacion[0]

        nueva_poblacion = poblacion[:10]  # elitismo: mantenemos mejores 10
        while len(nueva_poblacion) < POP_SIZE:
            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)
            hijo = crossover(padre1, padre2)
            mutacion(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    print("No se encontró solución.")
    return None

# Ejecutar el algoritmo genético
algoritmo_genetico()

##########################################################################
##########################################################################
##########################################################################

# Algoritmo de Fuerza Bruta para resolver el problema de las 8 reinas
import itertools

def es_valida(perm):
    n = len(perm)
    for i in range(n):
        for j in range(i+1, n):
            if abs(perm[i] - perm[j]) == abs(i - j):
                return False
    return True

def imprimir_tablero(perm):
    n = len(perm)
    for fila in range(n):
        linea = ""
        for col in range(n):
            if perm[fila] == col:
                linea += "♛ "
            else:
                linea += ". "
        print(linea)
    print()

def fuerza_bruta_n_reinas(n):
    soluciones = 0
    for perm in itertools.permutations(range(n)):
        if es_valida(perm):
            soluciones += 1
            print(f"Solución #{soluciones}: {perm}")
            imprimir_tablero(perm)
            break
    print(f"Total de soluciones: {soluciones}")

# Ejecutamos con n = 8 para ver la tabla
fuerza_bruta_n_reinas(8)
