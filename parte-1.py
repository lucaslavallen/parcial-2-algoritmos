
class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos


class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None


def insertar_en_arbol(raiz, pokemon, clave):
    if raiz is None:
        return NodoArbol(pokemon)
    elif getattr(pokemon, clave) < getattr(raiz.dato, clave):
        raiz.izq = insertar_en_arbol(raiz.izq, pokemon, clave)
    else:
        raiz.der = insertar_en_arbol(raiz.der, pokemon, clave)
    return raiz


def buscar_por_numero(raiz, numero):
    if raiz is None:
        return None
    if raiz.dato.numero == numero:
        return raiz.dato
    elif numero < raiz.dato.numero:
        return buscar_por_numero(raiz.izq, numero)
    else:
        return buscar_por_numero(raiz.der, numero)


def buscar_por_nombre_proximidad(raiz, texto):
    resultados = []
    if raiz:
        if texto.lower() in raiz.dato.nombre.lower():
            resultados.append(raiz.dato)
        resultados.extend(buscar_por_nombre_proximidad(raiz.izq, texto))
        resultados.extend(buscar_por_nombre_proximidad(raiz.der, texto))
    return resultados


def listar_por_tipo(raiz, tipo):
    resultados = []
    if raiz:
        if tipo in raiz.dato.tipos:
            resultados.append(raiz.dato.nombre)
        resultados.extend(listar_por_tipo(raiz.izq, tipo))
        resultados.extend(listar_por_tipo(raiz.der, tipo))
    return resultados


def listar_ordenado_por_numero(raiz):
    if raiz:
        return listar_ordenado_por_numero(raiz.izq) + [raiz.dato] + listar_ordenado_por_numero(raiz.der)
    return []


def contar_por_tipo(raiz, tipo):
    contador = 0
    if raiz:
        if tipo in raiz.dato.tipos:
            contador += 1
        contador += contar_por_tipo(raiz.izq, tipo)
        contador += contar_por_tipo(raiz.der, tipo)
    return contador


def mostrar_datos_pokemones(raiz, nombres):
    datos = []
    if raiz:
        if raiz.dato.nombre in nombres:
            datos.append(raiz.dato)
        datos.extend(mostrar_datos_pokemones(raiz.izq, nombres))
        datos.extend(mostrar_datos_pokemones(raiz.der, nombres))
    return datos

# emplo 
# crear lista de pokemon
pokemons = [
    Pokemon("Bulbasaur", 1, ["Planta", "Veneno"]),
    Pokemon("Charmander", 4, ["Fuego"]),
    Pokemon("Squirtle", 7, ["Agua"]),
    Pokemon("Jolteon", 135, ["Eléctrico"]),
    Pokemon("Lycanroc", 745, ["Roca"]),
    Pokemon("Tyrantrum", 697, ["Roca", "Dragón"]),
    
]

#crear arboles 
arbol_por_nombre = None
arbol_por_numero = None
arbol_por_tipo = None

for p in pokemons:
    arbol_por_nombre = insertar_en_arbol(arbol_por_nombre, p, "nombre")
    arbol_por_numero = insertar_en_arbol(arbol_por_numero, p, "numero")
    arbol_por_tipo = insertar_en_arbol(arbol_por_tipo, p, "tipos")


# buscar por número
print("Búsqueda por número (ejemplo, número 1):")
print(buscar_por_numero(arbol_por_numero, 1).__dict__)

# buscar por proximidad en nombre
print("\nBúsqueda por proximidad de nombre ('bul'):")
print([p.__dict__ for p in buscar_por_nombre_proximidad(arbol_por_nombre, "bul")])

# listar Pokémon por tipo específico
print("\nPokémon de tipo Agua:")
print(listar_por_tipo(arbol_por_tipo, "Agua"))

# listar en orden ascendente por número
print("\nListado en orden ascendente por número:")
print([p.__dict__ for p in listar_ordenado_por_numero(arbol_por_numero)])

# mostrar datos específicos de ciertos Pokémon
print("\nDatos de Jolteon, Lycanroc y Tyrantrum:")
print([p.__dict__ for p in mostrar_datos_pokemones(arbol_por_nombre, ["Jolteon", "Lycanroc", "Tyrantrum"])])

# contar Pokémon de un tipo específico
print("\nCantidad de Pokémon de tipo Eléctrico:")
print(contar_por_tipo(arbol_por_tipo, "Eléctrico"))

print("\nCantidad de Pokémon de tipo Acero:")
print(contar_por_tipo(arbol_por_tipo, "Acero"))
