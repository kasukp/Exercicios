import math

a, b, c = [float(i) for i in input().split()]

delta = b ** 2 - 4 * a * c
if delta < 0.0 or a == 0.0:
    print("Impossivel calcular")
    exit()

def BhaskaraFormula(deltaSqrt):
    return round((-b + deltaSqrt) / (2 * a), 5)

print("R1 =", BhaskaraFormula(math.sqrt(delta)))
print("R2 =", BhaskaraFormula(-math.sqrt(delta)))