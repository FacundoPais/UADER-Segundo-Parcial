class Pokemon:
    def __init__(self, numero, nombre, tipos):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos

    def __repr__(self):
        return f"Pokemon({self.numero}, {self.nombre}, {self.tipos})"


class Node:
    def __init__(self, key, other_value=None):
        self.key = key
        self.other_value = other_value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, key, other_value=None):
        if self.root is None:
            self.root = Node(key, other_value)
        else:
            self._insert_node(self.root, key, other_value)

    def _insert_node(self, node, key, other_value):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, other_value)
            else:
                self._insert_node(node.left, key, other_value)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, other_value)
            else:
                self._insert_node(node.right, key, other_value)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorden(self):
        return self._inorden(self.root)

    def _inorden(self, node):
        if node:
            return self._inorden(node.left) + [node.other_value] + self._inorden(node.right)
        return []

    def contar_super_heroes(self):
        return self._contar_super_heroes(self.root)

    def _contar_super_heroes(self, node):
        if node is None:
            return 0
        return 1 + self._contar_super_heroes(node.left) + self._contar_super_heroes(node.right)


class PokemonBinaryTree(BinaryTree):
    def search_by_proximity(self, key):
        results = []
        self._search_proximity(self.root, key, results)
        return results

    def _search_proximity(self, node, key, results):
        if node:
            if key.lower() in node.other_value.nombre.lower():
                results.append(node.other_value)
            self._search_proximity(node.left, key, results)
            self._search_proximity(node.right, key, results)



pokemons_data = [
    Pokemon(1, "Bulbasaur", ["Planta", "Veneno"]),
    Pokemon(2, "Ivysaur", ["Planta", "Veneno"]),
    Pokemon(3, "Venusaur", ["Planta", "Veneno"]),
    Pokemon(4, "Charmander", ["Fuego"]),
    Pokemon(5, "Charmeleon", ["Fuego"]),
    Pokemon(6, "Charizard", ["Fuego", "Volador"]),
    Pokemon(7, "Squirtle", ["Agua"]),
    Pokemon(8, "Wartortle", ["Agua"]),
    Pokemon(9, "Blastoise", ["Agua"]),
    Pokemon(10, "Caterpie", ["Bicho"]),
    Pokemon(11, "Metapod", ["Bicho"]),
    Pokemon(12, "Butterfree", ["Bicho", "Volador"]),
    Pokemon(13, "Jolteon", ["Eléctrico"]),
    Pokemon(14, "Lycanroc", ["Roca"]),
    Pokemon(15, "Tyrantrum", ["Roca", "Dragón"]),
    Pokemon(16, "Pikachu", ["Eléctrico"]),
    Pokemon(17, "Raichu", ["Eléctrico"]),
    Pokemon(18, "Gardevoir", ["Psíquico", "Hada"]),
    Pokemon(19, "Gengar", ["Fantasma", "Veneno"]),
    Pokemon(24, "Lucario", ["Lucha", "Acero"]),
    Pokemon(20, "Dragonite", ["Dragón", "Volador"])
]


tree_by_number = PokemonBinaryTree()
tree_by_name = PokemonBinaryTree()
tree_by_type = {}


for pokemon in pokemons_data:
    tree_by_number.insert_node(pokemon.numero, other_value=pokemon)
    tree_by_name.insert_node(pokemon.nombre, other_value=pokemon)

    for tipo in pokemon.tipos:
        if tipo not in tree_by_type:
            tree_by_type[tipo] = PokemonBinaryTree()
        tree_by_type[tipo].insert_node(pokemon.numero, other_value=pokemon)



def buscar_pokemon_por_numero(tree, numero):
    pokemon_node = tree.search(numero)
    if pokemon_node:
        return pokemon_node.other_value
    return None


def buscar_pokemon_por_nombre(tree, nombre):
    return tree.search_by_proximity(nombre)


def mostrar_pokemons_por_tipo(tipo):
    if tipo in tree_by_type:
        return tree_by_type[tipo].inorden()
    return []


def listar_ordenado():
    print(" ")
    print("Listando Pokémon por número:")
    print(tree_by_number.inorden())
    
    print("\nListando Pokémon por nombre:")
    print(tree_by_name.inorden())


def mostrar_pokemons_especificos(nombres):
    for nombre in nombres:
        pokemon_node = tree_by_name.search(nombre)
        if pokemon_node:
            print(pokemon_node.other_value)


def contar_pokemons_por_tipo(tipo):
    if tipo in tree_by_type:
        return tree_by_type[tipo].contar_super_heroes()
    return 0



print("Búsqueda de Pokémon que contienen 'bul':", buscar_pokemon_por_nombre(tree_by_name, "bul"))

print("Pokémon de tipo Agua:", mostrar_pokemons_por_tipo("Agua"))

listar_ordenado()

print("Mostrando datos de Pokémon específicos:")
mostrar_pokemons_especificos(["Jolteon", "Lycanroc", "Tyrantrum"])

print("Número de Pokémon de tipo Eléctrico:", contar_pokemons_por_tipo("Eléctrico"))
print("Número de Pokémon de tipo Acero:", contar_pokemons_por_tipo("Acero"))  
