"""Este código define una lista de números llamada lista
y luego ordena los elementos de la lista utilizando
la función sorted. La función sorted toma la lista como entrada
y devuelve una nueva lista ordenada en orden ascendente.
Luego, se imprime la lista ordenada en la consola.
"""


lista = [3, 44, 21, 78, 5, 56, 9, 0, 1]
"""Esta línea se ordena la lista utilizando la función sorted.
La función sorted toma la lista como entrada y devuelve una
nueva lista ordenada en orden ascendente. 
La sintaxis key=lambda x: x indica que se debe ordenar
la lista utilizando los valores de los elementos de la lista.
Si la lista está vacía, se crea una lista con un solo elemento
que es el número 0.
"""
lista_ordenada = sorted(lista, key=lambda x: x) if lista else [0]
print(lista_ordenada)
