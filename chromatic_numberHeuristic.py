import time
import string
def greedy_coloring(grafo):
    """
    Algoritmo heurístico Greedy Coloring para el problema del Chromatic Number.

    Args:
    
grafo: Un grafo representado como un diccionario de adyacencia.

    Returns:
    
Un diccionario que asigna colores a los vértices."""

    # Inicializar un diccionario para almacenar los colores asignados a cada vértice
    colores_asignados = {}

    # Recorrer todos los vértices del grafo
    for vertice in grafo:
        # Obtener los colores de los vértices adyacentes ya coloreados
        colores_adyacentes = set(colores_asignados.get(adyacente) for adyacente in grafo[vertice] if adyacente in colores_asignados)

        # Encontrar el color mínimo no utilizado por los vértices adyacentes
        color = 1
        while color in colores_adyacentes:
            color += 1

        # Asignar el color al vértice actual
        colores_asignados[vertice] = color

    return colores_asignados


# Generar nodos de la A a la Z
nodos = list(string.ascii_uppercase)

# Crear el grafo completo
grafo_ejemplo = {nodo: [otro_nodo for otro_nodo in nodos if otro_nodo != nodo] for nodo in nodos}

tiempo_inicio = time.time()
colores_asignados = greedy_coloring(grafo_ejemplo)
tiempo_fin = time.time()
print("Colores asignados a los vértices:")
for vertice, color in colores_asignados.items():
    print(f"{vertice}: Color {color}")
tiempo_transcurrido = tiempo_fin - tiempo_inicio

print(f"El script tomó {round(tiempo_transcurrido, 40)} segundos en ejecutarse.")