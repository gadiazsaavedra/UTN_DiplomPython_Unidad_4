"""Crear una función lambda que
sea equivalente a la siguiente función

def sumar(valor1,valor2):
    res = valor1+valor2
    return res

Este código define una función lambda llamada sumar
que toma dos valores como entrada y devuelve
la suma de esos valores. Luego, se llama a
la función lambda con dos valores de entrada (1 y 4)
y se imprime el resultado en la consola.
"""
sumar = lambda valor1, valor2: valor1 + valor2
print(sumar(1, 4))
