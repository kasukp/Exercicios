quant = int(input())
values = [j for i in range(quant) if (j := int(input())) >= 10 and j <= 20]
print(f"{len(values)} in")
print(f"{quant - len(values)} out")