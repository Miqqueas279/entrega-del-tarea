"""
Nombre de la función:
obtener_indice(lista, elemento)
Objetivo:
Encontrar el índice de la primera ocurrencia de un elemento en la lista.
Tarea:
Buscar en la lista el elemento recibido y retornar su posición (índice).
Si el elemento no existe en la lista, retornar -1.

"""
# Definición de la función
def obtener_indice(lista: list, elemento: str | int | float) -> int:
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
elemento_buscado = 3
indice_encontrado = obtener_indice(mi_lista, elemento_buscado)
print("El elemento", elemento_buscado, "se encuentra en la posición", indice_encontrado)