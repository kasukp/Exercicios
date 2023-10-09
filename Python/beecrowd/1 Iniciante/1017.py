horasViagem =  int(input())
velocidadeMedia = int(input())

minimoLitros = velocidadeMedia * horasViagem / 12

print("{:.3f}".format(minimoLitros))