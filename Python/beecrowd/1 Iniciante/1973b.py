## Total runtime > 1.8s
# Este código, no beecrowd, ocasionalmente retorna Time Limit Exceeded
total_estrelas = int(input())
carneiros = [int(i) for i in input().split()]

pos = 0
estrelas_roubadas = set()
while pos >= 0 and pos < total_estrelas:
    move = 1 if carneiros[pos] & 0b1 else -1

    if carneiros[pos] > 0:
        carneiros[pos] -= 1
        estrelas_roubadas.add(pos)
    pos += move

print(len(estrelas_roubadas), sum(carneiros))