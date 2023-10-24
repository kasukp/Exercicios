# Beecrowd não suporta numpy
# import numpy as np

var = input().split(" ", maxsplit=3)

# Exercício exige 32-bits float
# var[1] = np.float32(var[1])
var[1] = float(var[1])

print(f"{var[0]}{var[1]:6f}{var[2]}{var[3]}")
print(f"{var[0]}\t{var[1]:.6f}\t{var[2]}\t{var[3]}")
print(f"{var[0]:>10}{var[1]:>10.6f}{var[2]:>10}{var[3]:>10}")