from cola import Queue
from heap import HeapMin
from pila import Stack

class Graph:
    def __init__(self, dirigido=True):
        self.elements = []
        self.dirigido = dirigido

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index
        return None

    def insert_vertice(self, value):
        nodo = {
            'value': value,
            'aristas': [],
            'visitado': False,
        }
        self.elements.append(nodo)

    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            arista = {
                'value': destino,
                'peso': peso
            }
            self.elements[pos_origen]['aristas'].append(arista)
            if not self.dirigido:
                arista = {
                    'value': origen,
                    'peso': peso
                }
                self.elements[pos_destino]['aristas'].append(arista)

    def kruskal_con_yoda(self):
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                if buscado in arbol:
                    return index
            return None

        bosque = []
        aristas = HeapMin()
        contiene_yoda = False

        for nodo in self.elements:
            bosque.append([nodo['value']])
            if nodo['value'] == 'Yoda':
                contiene_yoda = True
            for adyacente in nodo['aristas']:
                aristas.arrive((nodo['value'], adyacente['value'], adyacente['peso']), adyacente['peso'])

        arbol_minimo = []

        while len(bosque) > 1 and len(aristas.elements) > 0:
            peso, (origen, destino, _) = aristas.atention()
            pos_origen = buscar_en_bosque(bosque, origen)
            pos_destino = buscar_en_bosque(bosque, destino)

            if pos_origen is not None and pos_destino is not None and pos_origen != pos_destino:
                bosque[pos_origen].extend(bosque.pop(pos_destino))
                arbol_minimo.append((origen, destino, peso))

        contiene_yoda = any('Yoda' in arbol for arbol in bosque)
        return arbol_minimo, contiene_yoda

    def max_episodios_compartidos(self):
        max_episodios = 0
        personajes = (None, None)

        for nodo in self.elements:
            for adyacente in nodo['aristas']:
                if adyacente['peso'] > max_episodios:
                    max_episodios = adyacente['peso']
                    personajes = (nodo['value'], adyacente['value'])

        return personajes, max_episodios


 
grafo = Graph(dirigido=False)
personajes = [
    'Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 'C-3PO', 'Leia', 
    'Rey', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8'
]

for personaje in personajes:
    grafo.insert_vertice(personaje)


grafo.insert_arista('Luke Skywalker', 'Darth Vader', 4)
grafo.insert_arista('Luke Skywalker', 'Yoda', 2)
grafo.insert_arista('Luke Skywalker', 'Leia', 5)
grafo.insert_arista('Luke Skywalker', 'Han Solo', 3)
grafo.insert_arista('Leia', 'Han Solo', 5)
grafo.insert_arista('Leia', 'C-3PO', 6)
grafo.insert_arista('Leia', 'R2-D2', 6)
grafo.insert_arista('Han Solo', 'Chewbacca', 7)
grafo.insert_arista('Han Solo', 'Leia', 5)
grafo.insert_arista('Rey', 'Kylo Ren', 3)
grafo.insert_arista('Rey', 'BB-8', 2)
grafo.insert_arista('R2-D2', 'C-3PO', 6)
grafo.insert_arista('Yoda', 'Chewbacca', 1)
grafo.insert_arista('Boba Fett', 'Darth Vader', 2)


arbol_minimo, contiene_yoda = grafo.kruskal_con_yoda()
print("Árbol de expansión mínimo:", arbol_minimo)
print("Contiene a Yoda:", contiene_yoda)


personajes_max_episodios, max_episodios = grafo.max_episodios_compartidos()
print("Personajes con el máximo de episodios compartidos:", personajes_max_episodios)
print("Número máximo de episodios compartidos:", max_episodios)