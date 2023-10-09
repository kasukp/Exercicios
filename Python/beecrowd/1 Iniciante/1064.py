values = [j for i in range(6) if (j := float(input())) > 0]
print(f"{len(values)} valores positivos")
print(f"{sum(values) / len(values):.1f}")