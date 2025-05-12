"""
Nombre de la función:
eliminar(lista)
Objetivo:
Eliminar el último elemento de la lista y retornarlo.
Tarea:
Modificar la lista original, removiendo su último elemento.
Retornar el elemento eliminado.
Ejemplo: Si la lista es ["a", "b", "c"], al llamar a eliminar(), se retorna "c" y la lista queda ["a", "b"].
"""

def eliminar(lista: list) -> any:
    """
    Elimina el último elemento de una lista y lo devuelve.
    """
    elemento_eliminado = lista[-1]
    del lista[-1]
    return elemento_eliminado

# Ejemplo de uso
if __name__ == "__main__":
    lista = ["a", "b", "c"]
    print("Lista original:", lista)
    elemento = eliminar(lista)
    print("Elemento eliminado:", elemento)
    print("Lista después de eliminar el último elemento:", lista)