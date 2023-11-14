class Vertice:
    def __init__(self, id):
        self.id = id
        self.color = None

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [Vertice(i) for i in range(num_vertices)]
        self.matriz_adyacencia = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def agregar_arista(self, u, v):
        self.matriz_adyacencia[u][v] = 1
        self.matriz_adyacencia[v][u] = 1

    def es_seguro(self, v, color_actual):
        for i in range(self.num_vertices):
            if self.matriz_adyacencia[v][i] == 1 and self.vertices[i].color == color_actual:
                return False
        return True

    def colorear(self, num_colores):
        return self.colorear_util(0, num_colores)

    def colorear_util(self, v, num_colores):
        if v == self.num_vertices:
            return True

        for c in range(1, num_colores + 1):
            if self.es_seguro(v, c):
                self.vertices[v].color = c
                if self.colorear_util(v + 1, num_colores):
                    return True
                self.vertices[v].color = None

        return False

    def imprimir_colores(self):
        for v in self.vertices:
            print(f"Vértice {v.id}: Color {v.color}")


# Ejemplo de uso
grafo = Grafo(6)
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(0, 3)
grafo.agregar_arista(0, 4)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 5)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 5)

for x in range(1, 10):
    if grafo.colorear(x):
        print(f"El grafo puede ser coloreado con {x} color/es.")
        grafo.imprimir_colores()
        break
    else:
        print(f"No es posible colorear el grafo con {x} color/es.")