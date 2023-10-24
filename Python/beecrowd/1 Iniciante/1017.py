horas_viagem =  int(input())
velocidade_media = int(input())

minimo_litros = velocidade_media * horas_viagem / 12

print(f"{minimo_litros:.3f}")