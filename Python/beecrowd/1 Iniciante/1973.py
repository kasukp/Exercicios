### Tempo > 0.5s
totalEstrelas = int(input())
carneiros = [int(i) for i in input().split()]

count = 0
for idx, i in enumerate(carneiros):
    if i == 1:
        count += 1
    if not i & 0b1: # se carneiros[idx] não for ímpar
        print(idx + 1, sum(carneiros) - (idx + 1 + idx - count))
        exit()
print(totalEstrelas, sum(carneiros) - totalEstrelas)