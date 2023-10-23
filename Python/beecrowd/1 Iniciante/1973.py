## Total runtime > 0.5s
total_estrelas = int(input())
carneiros = [int(i) for i in input().split()]

count = 0
for idx, i in enumerate(carneiros):
    if i == 1:
        count += 1
    if not i & 0b1:
        print(idx + 1, sum(carneiros) - (idx + 1 + idx - count))
        exit()
print(total_estrelas, sum(carneiros) - total_estrelas)