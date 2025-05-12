"""
Nombre de la función:
eliminar_primer_instancia(lista, elemento)
Objetivo:
Eliminar la primera ocurrencia de un elemento en la lista y retornarlo.
Tarea:
Buscar la primera aparición de elemento en la lista, eliminarla y retornar el elemento eliminado.
Si el elemento no existe, retornar None y dejar la lista sin cambios.
Ejemplo: Si la lista es [5, 3, 5, 7] y se elimina 5, la lista queda [3, 5, 7] y se retorna 5.
"""
def eliminar_primer_instancia(lista: list, elemento: any) -> any:
    """
    Elimina la primera instancia de un elemento en una lista y lo devuelve.
    """
    try:
        indice = lista.index(elemento)
        elemento_eliminado = lista[indice]
        del lista[indice]
        return elemento_eliminado
    except ValueError:
        return None
# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 3, 5, 7]
    print("Lista original:", lista)
    elemento = eliminar_primer_instancia(lista, 5)
    print("Elemento eliminado:", elemento)
    print("Lista después de eliminar la primera instancia de 5:", lista)
    