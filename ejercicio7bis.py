"""
Se toma una lista llamada lista que contiene elementos
de diferentes niveles de anidamiento.
Luego, se define una función lambda llamada recorre_lista
que toma dos argumentos: item y nivel.
Esta función se encarga de recorrer la lista de manera recursiva
y mostrar cada elemento con el nivel de anidamiento correspondiente.
Dentro de la función recorre_lista, se interpreta la lista para
iterar sobre cada elemento de la lista item.
Si el elemento es una lista, se llama a la función
recorre_lista de manera recursiva con el elemento y el nivel de
anidamiento incrementado en 1. Si el elemento no es una lista,
se imprime el elemento con el nivel de anidamiento correspondiente
utilizando la expresión " " * nivel.
Finalmente, se llama a la función recorre_lista con la lista lista
como argumento para mostrar todos los elementos de la lista con
el nivel de anidamiento correspondiente.
"""
lista = [
    "elemento1n1",
    "elemento2n1",
    "elemento3n1",
    [
        "elemento1n2",
        "elemento2n2",
        "elemento3n2",
        ["elemento1n3", "elemento2n3", "elemento3n3"],
    ],
]

recorre_lista = lambda item, nivel=0: [
    recorre_lista(x, nivel + 1) if isinstance(x, list) else print("  " * nivel + x)
    for x in item
]

recorre_lista(lista)
