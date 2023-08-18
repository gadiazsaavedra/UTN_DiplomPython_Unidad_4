"""Este código define una función lambda llamada
escribir_al_reves que toma una cadena de texto
como entrada y devuelve la cadena de texto invertida.
Luego, se llama a la función lambda con una cadena de
texto (por ej."hola") y se imprime el resultado en la consola.
"""

escribir_al_reves = lambda frase: frase[::-1]

print(escribir_al_reves("hola"))
