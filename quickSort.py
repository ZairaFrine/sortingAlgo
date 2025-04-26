# autor: Zaira Acosta
# Descripción: Programa que utiliza el algoritmo Quick Sort, para ordenar 500 números decimales random,
# 1000 números enteros y finalmente 10,000 números enteros
# Parámetros: no recibe parámetros de entrada, las listas de números son creadas de forma aleatoria
# utilizando la librería random. Hace uso de la librería time para estimar el tiempo de procesamiento
# debido a las capacidades del equipo donde se ejecute.
import random
import time

# Función quicksort
# Parámetros: numArr, es el arreglo sobre el cual itera para acomodar los números
# Descripción: Selecciona un pivote desde el cual se compararán el resto de los números: pivote = numArr[0]
# Si el resto de los elementos son menores o mayores al pivote se almacenan en dos listas diferentes: menores y mayores.
# Utilizando recursividad, el programa itera sobre la lista menores y la lista mayores, escogiendo un nuevo pivote en ambas
# listas y volviendo a ordenar hasta que los arreglos menor y mayor respectivamente, tengan solo 1 elemento o estén vacías.
# la funciona regresa una lista concatenando la lista de números menores al pivote, el pivote, y la lista de números mayores al pivote.
def quicksort(numArr):
  if len(numArr) <= 1:
      return numArr
  else:
    pivote = numArr[0]
    menores = []
    mayores = []
    for x in numArr[1:]:  # Itera sobre el resto del arreglo excepto el pivote
      if x <= pivote:  
        menores.append(x)  # lista de menores
      if x > pivote:  
        mayores.append(x)  # lista de mayores
  finalArr = quicksort(menores) + [pivote] + quicksort(mayores)
  return finalArr

#Caso 1. Lista de números tipo float de longitud igual a 500, es decir, 500 números decimales.
arrC1 = [random.uniform(1, 1000) for _ in range(500)]

#Caso 2. Lista de números enteros y decimales de longitud igual a 1000.
arrC2 = []
for i in range(1000):
    if random.choice([True, False]):  
        arrC2.append(random.randint(1, 1000))
    else:
        arrC2.append(random.uniform(1, 1000))
        
#Caso 3. Lista de números enteros y decimales de longitud igual a 10,000.
arrC3 = []
for i in range(10000):
    if random.choice([True, False]):  
        arrC3.append(random.randint(1, 10000))
    else:
        arrC3.append(random.uniform(1, 10000))

# Se ejecuta quicksort en los 3 arreglos:
#CASO 1
t0 = time.time()
ordenado = quicksort(arrC1)
tf = time.time()
print(f"\nTiempo total Caso 1: {tf - t0:.5f} segundos")
print("Arreglo ordenado:"); print(ordenado[:20], "...")

#CASO 2
t0 = time.time()
ordenado = quicksort(arrC2)
tf = time.time()
print(f"\nTiempo total Caso 2: {tf - t0:.5f} segundos")
print("Arreglo ordenado:"); print(ordenado[:20], "...")

#CASO 3
t0 = time.time()
ordenado = quicksort(arrC3)
tf = time.time()
print(f"\nTiempo total Caso 3: {tf - t0:.5f} segundos")
print("Arreglo ordenado:"); print(ordenado[:20], "...")


