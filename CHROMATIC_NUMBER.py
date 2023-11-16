import time
from random import randint
class Nodo:
    def __init__(self, id):
        self.id = id
        self.color = None

class Grafo:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.nodos = [Nodo(i) for i in range(num_nodos)]
        self.matriz_adyacencia = [[0 for _ in range(num_nodos)] for _ in range(num_nodos)] #crea matriz de la cantidad de nodos x cantidad de nodos y la llena con 0

    def agregar_arista(self, u, v):
        self.matriz_adyacencia[u][v] = 1
        self.matriz_adyacencia[v][u] = 1

    def es_seguro(self, v, color_actual):
        for i in range(self.num_nodos):
            if self.matriz_adyacencia[v][i] == 1 and self.nodos[i].color == color_actual:
                return False
        return True

    def colorear(self, num_colores):
        return self.colorear_util(0, num_colores)

    def colorear_util(self, v, num_colores):
        if v == self.num_nodos:
            return True

        for c in range(1, num_colores + 1):
            if self.es_seguro(v, c):
                self.nodos[v].color = c
                if self.colorear_util(v + 1, num_colores):
                    return True
                self.nodos[v].color = None

        return False

    def imprimir_colores(self):
        for v in self.nodos:
            print(f"Nodo {v.id}: Color {v.color}")



# Guarda el tiempo de inicio

# Ejemplo de uso
nodos= 24
relaciones = 276

# relaciones = randint(0, ((nodos*(nodos-1))/2))
contador = 0
grafo = Grafo(nodos)
lista_relaciones = []

for x in range(nodos):
    for y in range(nodos):
        if x != y:
            lista_relaciones.append((x,y))
while relaciones > contador:
    if len(lista_relaciones)-1 > -1:
        indice= randint(0, len(lista_relaciones)-1)
    tupla= lista_relaciones[indice]
    lista_relaciones.remove(tupla)
    lista_relaciones.remove((tupla[1],tupla[0]))
    grafo.agregar_arista(tupla[0], tupla[1])
    contador+=1
   
        
tiempo_inicio = time.time()
for x in range(1, 20):
    tiempo_medio = time.time()
    if grafo.colorear(x):
        print(f"El grafo puede ser coloreado con {x} color/es.")
        grafo.imprimir_colores()
        break
    else:
        parcial_time= time.time()
        tiempo_parcial = parcial_time - tiempo_medio
        print(f"No es posible colorear el grafo con {x} color/es. En este color se tardo: {round(tiempo_parcial, 3)} segundos en ejecutarse.")
tiempo_fin = time.time()

# Calcula el tiempo transcurrido
tiempo_transcurrido = tiempo_fin - tiempo_inicio

print(f"El script tomó {round(tiempo_transcurrido, 3)} segundos en ejecutarse.")