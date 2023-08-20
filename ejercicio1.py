"""
Este código solicita al usuario que ingrese un número
y luego verifica si el número es par o no utilizando
una función lambda. La función lambda es_par toma
un número como entrada y devuelve True si el número es par
(es decir, divisible por 2) y False en caso contrario.
El número de entrada se pasa a la función lambda
utilizando la variable check_numero, y el resultado
se imprime en la consola. Si el número es par,
la salida será True, de lo contrario será False.
"""
check_numero = int(input("Check si el número es par: "))
es_par = lambda num: num % 2 == 0
print(es_par(check_numero))
