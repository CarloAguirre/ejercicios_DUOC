import random
import numpy as np

# Crear un arreglo de 3x3 con elementos aleatorios entre 0 y 100
arreglo = np.random.randint(0, 101, size=(3, 3))

# Mostrar el arreglo
print("Arreglo 3x3:")
print(arreglo)

#promedio de los elementos
suma_total = 0
contador = 0
for i in range(3):
    for j in range(3):
        suma_total += arreglo[i][j]
        contador += 1

promedio = suma_total / contador
print("\nPromedio de los elementos:", promedio)

print("Suma de los elementos:", suma_total)

#encontrar el elemento mayor
elemento_mayor = arreglo[0][0]
for i in range(3):
    for j in range(3):
        if arreglo[i][j] > elemento_mayor:
            elemento_mayor = arreglo[i][j]

print("Elemento mayor:", elemento_mayor)

#encontrar el elemento menor
elemento_menor = arreglo[0][0]
for i in range(3):
    for j in range(3):
        if arreglo[i][j] < elemento_menor:
            elemento_menor = arreglo[i][j]

print("Elemento menor:", elemento_menor)

#mostrar los elementos de la diagonal principal
print("Elementos de la diagonal principal:")
for i in range(3):
    print(arreglo[i][i])

import numpy as np

# Crear un arreglo de 3x3 con ceros
arreglo = np.zeros((3, 3), dtype=int)

# Colocar los valores 1, 2 y 3 en la diagonal principal
arreglo[0][0] = 1
arreglo[1][1] = 2
arreglo[2][2] = 3

# Mostrar el arreglo
print("Arreglo 3x3:")
print(arreglo)

