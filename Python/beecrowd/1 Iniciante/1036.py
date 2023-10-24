import math

a, b, c = [float(i) for i in input().split()]

delta = b ** 2 - 4 * a * c
if delta < 0.0 or a == 0.0:
    print("Impossivel calcular")
    exit()


def bhaskara_formula(delta_sqrt):
    return round((-b + delta_sqrt) / (2 * a), 5)

print("R1 =", bhaskara_formula(math.sqrt(delta)))
print("R2 =", bhaskara_formula(-math.sqrt(delta)))