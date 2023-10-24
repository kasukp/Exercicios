quant = int(input())
weight = [2, 3, 5]

for i in range(quant):
    values = [float(i) for i in input().split()]
    weighted_values = [i * weight[idx] for idx, i in enumerate(values)]
    average = round(sum(weighted_values) / sum(weight), 1)
    print(average)
