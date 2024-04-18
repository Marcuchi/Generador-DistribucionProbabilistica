import pandas as pd
import random
import matplotlib.pyplot as plt

# lista = []
# random.seed(0)
# for i in range(0,10):
#     i = round(random.random(),2)
#     lista.append(i)
# print(lista)

# n_max = max(lista)
# n_min = min(lista)

# rango = round((n_max - n_min)/5,2)

# lista_graficar = [[],[],[]]
# for i in range(0, 5):
#     val_sup = n_min + rango
#     lista_graficar[0].append(i + 1)
#     lista_graficar[1].append(n_min)
#     lista_graficar[2].append(val_sup)
#     n_min += rango
#     print(val_sup)


# frec = [0] * len(lista_graficar[2])
# for i in range(0,10):
#      for o in range(0,5):
#         if lista[i] < lista_graficar[2][o]:
#           frec[o] += 1
#           break
# print(frec)     
lista = [1.2,2.3,4]
lista_a_copiar = "\n".join(map(str,lista))
print(lista_a_copiar)

#[[1, 0.04, 0.22], [2, 0.22, 0.4], [3, 0.4, 0.5800000000000001], [4, 0.5800000000000001, 0.76], [5, 0.76, 0.94]]