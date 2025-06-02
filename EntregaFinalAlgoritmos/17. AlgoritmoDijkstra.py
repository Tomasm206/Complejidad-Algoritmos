import heapq

def codificacionDijkstra(G, origen):
    n = len(G)  # Número de nodos
    distancia = [float('inf')] * n
    predecesor = [None] * n

    distancia[origen] = 0
    cola = [(0, origen)]  # (distancia, nodo)

    while cola:
        dist_u, u = heapq.heappop(cola)

        for v, peso_uv in enumerate(G[u]):
            if peso_uv > 0:  # solo considerar vecinos conectados (no peso 0)
                nueva_distancia = dist_u + peso_uv
                if nueva_distancia < distancia[v]:
                    distancia[v] = nueva_distancia
                    predecesor[v] = u
                    heapq.heappush(cola, (nueva_distancia, v))

    return distancia, predecesor

# Matriz de adyacencia (10 nodos)
G = [ 
    [ 0, 34, 56, 12, 78, 90, 43, 67, 23, 55 ],
    [ 34, 0, 64, 21, 12, 44, 90, 13, 45, 66 ],
    [ 56, 64, 0, 50, 34, 33, 76, 82, 28, 59 ],
    [ 12, 21, 50, 0, 22, 88, 16, 44, 73, 10 ],
    [ 78, 12, 34, 22, 0, 25, 90, 17, 65, 33 ],
    [ 90, 44, 33, 88, 25, 0, 14, 56, 32, 71 ],
    [ 43, 90, 76, 16, 90, 14, 0, 36, 48, 11 ],
    [ 67, 13, 82, 44, 17, 56, 36, 0, 20, 24 ],
    [ 23, 45, 28, 73, 65, 32, 48, 20, 0, 60 ],
    [ 55, 66, 59, 10, 33, 71, 11, 24, 60, 0 ]
]

distancias, predecesores = codificacionDijkstra(G, 0)
suma = sum(distancias)
print("Distancias desde nodo 0:", suma)
print("Predecesores:", predecesores)
