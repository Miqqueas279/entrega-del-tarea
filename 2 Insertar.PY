"""
Nombre de la función:
insertar(lista, elemento, indice)
Objetivo:
Insertar un elemento en una posición específica de la lista.
Tarea:
Modificar la lista original, colocando elemento en la posición indicada por indice.
Si el índice es mayor al tamaño de la lista, el elemento se agrega al final.
Ejemplo: Si la lista es [10, 20, 30] y se inserta 5 en el índice 1, la lista resultante será [10, 5, 20, 30].

"""
def insertar(lista, elemento : str | int | float, indice ) -> list :
    if indice > len(lista):
        lista.append(elemento)
    else:
        lista.insert(indice, elemento)
    return lista   

mi_lista = [10, 20, 30]
insertar(mi_lista, 5, 1)
print(mi_lista)  # Resultado: [10, 5, 20, 30]
