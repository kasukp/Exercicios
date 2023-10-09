a, b, c = [float(length) for length in input().split()]
if a + b > c and b + c > a and c + a > b:
    print(f"Perimetro = {a + b + c}")
else:
    print(f"Area = {((a + b) * c) / 2}")