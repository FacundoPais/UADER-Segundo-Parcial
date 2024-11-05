from heap import HeapMin

class Graph:
    def __init__(self, dirigido=False):
        self.vertices = {}
        self.dirigido = dirigido

    def insert_vertice(self, nombre):
        if nombre not in self.vertices:
            self.vertices[nombre] = {'aristas': {}}

    def insert_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen]['aristas'][destino] = peso
            if not self.dirigido:
                self.vertices[destino]['aristas'][origen] = peso

    def kruskal(self):
        def find_set(bosque, buscado):
            for index, arbol in enumerate(bosque):
                if buscado in arbol:
                    return index
            return None

        bosque = [[v] for v in self.vertices]
        aristas = HeapMin()
        
        for vertice, datos in self.vertices.items():
            for adj, peso in datos['aristas'].items():
                aristas.arrive((vertice, adj, peso), peso)

        arbol_minimo = []
        while len(bosque) > 1 and len(aristas.elements) > 0:
            _, (origen, destino, peso) = aristas.atention()
            pos_origen = find_set(bosque, origen)
            pos_destino = find_set(bosque, destino)
            if pos_origen is not None and pos_destino is not None and pos_origen != pos_destino:
                arbol_minimo.append((origen, destino, peso))
                bosque[pos_origen].extend(bosque.pop(pos_destino))
        return arbol_minimo

    def contiene_personaje(self, personaje):
        return personaje in self.vertices

    def maximo_compartido(self):
        max_peso = 0
        personajes = ()
        for vertice, datos in self.vertices.items():
            for adj, peso in datos['aristas'].items():
                if peso > max_peso:
                    max_peso = peso
                    personajes = (vertice, adj)
        return max_peso, personajes

    def show_graph(self):
        print("\nNodos:")
        for vertice, datos in self.vertices.items():
            print(f"{vertice}")
            print("    Aristas:")
            for arista, peso in datos['aristas'].items():
                print(f"    Destino: {arista} - Episodios: {peso}")


grafo = Graph(dirigido=False)


personajes = [
    "Luke Skywalker",
    "Darth Vader",
    "Yoda",
    "Boba Fett",
    "C-3PO",
    "Leia",
    "Rey",
    "Kylo Ren",
    "Chewbacca",
    "Han Solo",
    "R2-D2",
    "BB-8"
]

for personaje in personajes:
    grafo.insert_vertice(personaje)


grafo.insert_arista("Luke Skywalker", "Darth Vader", 6)
grafo.insert_arista("Luke Skywalker", "Yoda", 5)
grafo.insert_arista("Yoda", "Darth Vader", 3)
grafo.insert_arista("Yoda", "Leia", 4)
grafo.insert_arista("Leia", "Han Solo", 4)
grafo.insert_arista("Rey", "Kylo Ren", 4)
grafo.insert_arista("Chewbacca", "Han Solo", 6)
grafo.insert_arista("C-3PO", "R2-D2", 8)
grafo.insert_arista("BB-8", "Rey", 3)
grafo.insert_arista("Luke Skywalker", "Chewbacca", 5)
grafo.insert_arista("Darth Vader", "Leia", 5)


grafo.show_graph()


arbol_expansion = grafo.kruskal()
print("\nÁrbol de expansión mínimo:")
for origen, destino, peso in arbol_expansion:
    print(f"{origen} <-> {destino} (Episodios: {peso})")


yoda_en_arbol = any(origen == "Yoda" or destino == "Yoda" for origen, destino, _ in arbol_expansion)
print(f"\nYoda está en el árbol de expansión mínimo? {'Sí' if yoda_en_arbol else 'No'}")


max_episodios, personajes_max = grafo.maximo_compartido()
print(f"\nMáximo de episodios compartidos: {max_episodios} entre {personajes_max[0]} y {personajes_max[1]}.")
