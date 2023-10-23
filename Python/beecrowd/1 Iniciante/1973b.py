# Este código retorna Time Limit Exceeded no beecrowd

## Tempo > 2s
totalEstrelas = int(input())
carneiros = [int(i) for i in input().split()]

pos = 0
estrelasRoubadas = set()
while pos >= 0 and pos < totalEstrelas:
    if carneiros[pos] % 2 == 1:
### if carneiros[pos] & 0b1: # Tempo > 1.9s
        move = 1
    else:
        move = -1

    if carneiros[pos] > 0:
        carneiros[pos] -= 1
        estrelasRoubadas.add(pos)
    pos += move

print(len(estrelasRoubadas), sum(carneiros))