"""
Eliminar todas las instancias
Nombre de la función:
eliminar_todos(lista, elemento)
Objetivo:
Eliminar todas las ocurrencias de un elemento en la lista.
Tarea:
Modificar la lista original, removiendo todos los elementos iguales al valor recibido.
No es necesario retornar un valor (solo modificar la lista#).
Ejemplo: Si la lista es [4, 8, 4, 4, 10] y se eliminan todas las instancias de 4, la lista resultante será [8, 10].
""" 
def eliminar_todos (lista: list, elemento: str | int | float) -> None:
    """
    Elimina todas las ocurrencias de un elemento en una lista
    """
    while elemento in lista:    
        for i in range(len(lista)):
            del [i]

lista_ejemplo = [2, 1, 2, 3]
elemento_buscar = 2

eliminar_todos(lista_ejemplo, elemento_buscar)
print(lista_ejemplo)

lista_ejemplo.remove()