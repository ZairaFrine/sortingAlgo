# autor: Zaira Acosta
# Descripción: Programa que utiliza el algoritmo Quick Sort, para ordenar 500 números decimales random,
# 1000 números enteros y finalmente 10,000 números enteros
# Parámetros: no recibe parámetros de entrada, las listas de números son creadas de forma aleatoria
# utilizando la librería random. Hace uso de la librería time para estimar el tiempo de procesamiento
# debido a las capacidades del equipo donde se ejecute, este puede variar.

import random
import time

# Función bubbles
# Parámetros: numArr, es el arreglo sobre el cual itera para acomodar los números
# Descripción: itera sobre un arreglo de números, compara el número que se lee en la iteración actual con un número en la 
# posición siguiente, si es mayor, intercambia lugar con este número. en la siguiente iteración, vuelve a comparar hasta que
# termine de recorrer el arreglo; una variable de control indica si hubo cambios durante el recorrido del arreglo.
# Cuando termina el recorrido, revisa si la variable de control indica cambios, si hubo cambios quiere decir que puede haber mas.
# Recorre tantas veces sea necesario el arreglo hasta que la variable de control no indica cambios y se concluye que se han
# ordenado todos los números


# Se programó una propuesta encontrada en:
# Sharma, V. (2015). A new approach to improve worst case efficiency of Bubble Sort. International Research Journal of Computer Science (IRJCS), 2(6), 54–58. https://www.researchgate.net/publication/313647211_A_New_Approach_to_Improve_Worst_Case_Efficiency_of_Bubble_Sort
# En escencia se propone un una preparación de la lista de datos y luego se aplica el método de burbuja convencional.
# Revisando esta propuesta acorta notablemente el tiempo de ejecución de los algoritmos

def preOrderBubble(arrPO):
  arrPO = arrPO[::-1]  # Se invierte la Lista
  front = 0
  last = len(arrPO) - 1

  while front < last:  # tomar el primer elemento y el último del arreglo y compararlos.
    if arrPO[front] > arrPO[last]: # Si el primero es mayor que el último intercambia
        arrPO[front], arrPO[last] = arrPO[last], arrPO[front]
    
    front += 1 # Avanza en el siguiente elemento
    last -= 1 # Retrocede al anterior elemento
    #Se cicla hasta que se llega a los elementos centrales

  return arrPO


def bubbles( numArr ):
  ctrl = 1
  while ctrl > 0:
    ctrl = 0
    for i in range(len(numArr) - 1):
      if numArr[i] > numArr[i+1]:
        numArr[i], numArr[i+1] = numArr[i+1], numArr[i]
        ctrl = 1
  return numArr


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



# Se ejecuta bubles en los 3 arreglos:
#CASO 1
t0 = time.time()
ordenado = bubbles(arrC1)
tf = time.time()
print(f"\nTiempo total Caso 1 Burbuja Normal: {tf - t0:.5f} segundos")
print("Arreglo ordenado:"); print(ordenado[:20], "...")

t0 = time.time()
preOrd = preOrderBubble(arrC1)
ordenado = bubbles(preOrd)
tf = time.time()
print(f"\nTiempo total Caso 1 Burbuja Modificada: {tf - t0:.5f} segundos")
print("Arreglo ordenado:"); print(ordenado[:20], "...")


#CASO 2
t0 = time.time()
ordenado = bubbles(arrC2)
tf = time.time()
print(f"\nTiempo total Caso 2 Burbuja Normal: {tf - t0:.5f} segundos")
print("Arreglo ordenado:"); print(ordenado[:20], "...")

t0 = time.time()
preOrd = preOrderBubble(arrC2)
ordenado = bubbles(arrC2)
tf = time.time()
print(f"\nTiempo total Caso 2 Burbuja Modificada: {tf - t0:.5f} segundos")
print("Arreglo ordenado:"); print(ordenado[:20], "...")


#CASO 3
t0 = time.time()
ordenado = bubbles(arrC3)
tf = time.time()
print(f"\nTiempo total Caso 3 Burbuja Normal: {tf - t0:.5f} segundos")
print("Arreglo ordenado:"); print(ordenado[:20], "...")

t0 = time.time()
preOrd = preOrderBubble(arrC3)
ordenado = bubbles(arrC3)
tf = time.time()
print(f"\nTiempo total Caso 3 Burbuja Modificada: {tf - t0:.5f} segundos")
print("Arreglo ordenado:"); print(ordenado[:20], "...")
