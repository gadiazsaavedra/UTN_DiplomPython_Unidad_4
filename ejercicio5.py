"""
Este código solicita al usuario que ingrese su edad
y luego define una función lambda llamada
imprimir_anios_cumplidos que toma la edad como entrada
y muestra en la consola todos los años desde el 1 hasta
la edad en forma ascendente y descendente
"""
# Usando Func.Lambda #
edad = int(input("Cuantos años tiene Ud..?? : "))
"""
La función lambda se define utilizando
la palabra clave lambda, seguida de los parámetros
de entrada (en este caso, edad) y luego de los dos puntos
hay tuplas de expresiones que se ejecutan en secuencia.
Cada expresión es una llamada a la función print que muestra
una cadena de texto que se construye utilizando
la función join y la función range.
"""
imprimir_anios_cumplidos = lambda edad: (
    print("Estos son todos los anios en forma ascendente"),
    print(", ".join(str(i) for i in range(1, edad + 1))),
    print("Estos son todos los anios en forma descendente"),
    print(", ".join(str(i) for i in range(edad, 0, -1))),
)
imprimir_anios_cumplidos(edad)
