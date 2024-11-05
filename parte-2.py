

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, character):
        if character not in self.vertices:
            self.vertices[character] = {}

    def add_edge(self, from_character, to_character, episodes):
        self.add_vertex(from_character)
        self.add_vertex(to_character)
        self.vertices[from_character][to_character] = episodes
        self.vertices[to_character][from_character] = episodes  # Grafo no dirigido

    def minimum_spanning_tree(self):
        if not self.vertices:
            return []

        start_vertex = next(iter(self.vertices))
        visited = set([start_vertex])
        edges = []

        while len(visited) < len(self.vertices):
            min_edge = (None, None, float('inf'))
            for vertex in visited:
                for adjacent, weight in self.vertices[vertex].items():
                    if adjacent not in visited and weight < min_edge[2]:
                        min_edge = (vertex, adjacent, weight)
            if min_edge[0] is not None:
                edges.append(min_edge)
                visited.add(min_edge[1])

        return edges

    def has_character(self, character):
        return character in self.vertices

    def max_episodes_shared(self):
        max_count = 0
        characters = (None, None)

        for char1, neighbors in self.vertices.items():
            for char2, count in neighbors.items():
                if count > max_count:
                    max_count = count
                    characters = (char1, char2)

        return characters, max_count


# Crear grafo y agregar personajes y relaciones
star_wars_graph = Graph()
star_wars_graph.add_edge('Luke Skywalker', 'Darth Vader', 5)
star_wars_graph.add_edge('Luke Skywalker', 'Yoda', 3)
star_wars_graph.add_edge('Darth Vader', 'Yoda', 4)
star_wars_graph.add_edge('Boba Fett', 'Darth Vader', 2)
star_wars_graph.add_edge('C-3PO', 'Leia', 4)
star_wars_graph.add_edge('Leia', 'Yoda', 2)
star_wars_graph.add_edge('Rey', 'Kylo Ren', 3)
star_wars_graph.add_edge('Chewbacca', 'Han Solo', 5)
star_wars_graph.add_edge('R2-D2', 'BB-8', 1)
star_wars_graph.add_edge('Han Solo', 'Leia', 6)
star_wars_graph.add_edge('Kylo Ren', 'Darth Vader', 2)
star_wars_graph.add_edge('Luke Skywalker', 'R2-D2', 3)

# a) Mostrar el grafo
print("Grafo de personajes de Star Wars:")
for character, connections in star_wars_graph.vertices.items():
    print(f"{character}: {connections}")

# b) Hallar el árbol de expansión mínimo
mst = star_wars_graph.minimum_spanning_tree()
print("\nÁrbol de expansión mínimo:")
for edge in mst:
    print(f"{edge[0]} <--> {edge[1]} (Episodios: {edge[2]})")

# Determinar si contiene a Yoda
contains_yoda = star_wars_graph.has_character('Yoda')
print("\n¿Contiene a Yoda en el árbol de expansión mínimo?:", contains_yoda)

# c) Determinar el número máximo de episodios que comparten dos personajes
shared_characters, max_episodes = star_wars_graph.max_episodes_shared()
print("\nNúmero máximo de episodios que comparten dos personajes:")
print(f"{shared_characters[0]} y {shared_characters[1]}: {max_episodes} episodios")