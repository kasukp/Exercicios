code, quantity = [int(i) for i in input().split()]
price = [0.0, 4.0, 4.5, 5.0, 2.0, 1.5]
print(f"Total: R$ {(price[code] * quantity):.2f}")