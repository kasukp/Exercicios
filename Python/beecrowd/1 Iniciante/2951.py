quant_runes, min_friendship = [int(i) for i in input().split()]
runes = {i: int(j) for k in range(quant_runes) for i, j in [input().split()]}

# Valor desnecessário
input()

total = sum(runes[i] for i in input().split())
print(total)

if total >= min_friendship:
    print("You shall pass!")
else:
    print("My precioooous")