"""
Nombre de la función:
eliminar_todos(lista, elemento)
Objetivo:
Eliminar todas las ocurrencias de un elemento en la lista.
Tarea:
Modificar la lista original, removiendo todos los elementos iguales al valor recibido.
No es necesario retornar un valor (solo modificar la lista).

Ejemplo: Si la lista es [4, 8, 4, 4, 10] y se eliminan todas las instancias de 4, la lista resultante será [8, 10].
"""
def eliminar_todos(lista, elemento):
    while elemento in lista:
        lista.remove(elemento) 
    return lista
# Ejemplo de uso
lista = [4, 8, 4, 4, 10]
print("Lista original:", lista)
eliminar_todos(lista, 4)
print("Lista después de eliminar todas las instancias de 4:", lista)
