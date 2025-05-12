"""
1 Agregar
Nombre de la función:
agregar(lista, elemento)

Objetivo:
Agregar un elemento al final de la lista.
Tarea:
Modificar la lista original, añadiendo elemento como su último elemento.
No es necesario retornar un valor (solo modificar la lista).
"""
# Definición de la función
def agregar(lista: list, elemento: str | int | float) -> None:
    lista.append(elemento)

# Ejemplo de uso
mi_lista = [1, 2, 3]
print("Lista antes de agregar:", mi_lista)

agregar(mi_lista, 4)

print("Lista después de agregar:", mi_lista)
